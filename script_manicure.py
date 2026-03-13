import os
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from datetime import datetime

def monitorar_contas_mitolyn():
    print(f"--- Início da Automação Mitolyn: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ---")

    # 1. SETUP GOOGLE SHEETS
    try:
        creds_dict = json.loads(os.environ['GOOGLE_CREDS'])
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open_by_key(os.environ['SPREADSHEET_ID'])
        print("✅ Conectado ao Google Sheets.")
    except Exception as e:
        print(f"❌ Erro Google Sheets: {e}")
        return

    # 2. SETUP META ADS API
    try:
        FacebookAdsApi.init(access_token=os.environ['META_TOKEN'])
        print("✅ Autenticado no Meta Ads.")
    except Exception as e:
        print(f"❌ Erro Meta API: {e}")
        return

    # 3. LISTA DE PRODUTOS E CONTAS
    # Formato: [Nome da Aba, ID da Conta Meta]
    configuracoes = [
        ["Manicure", "act_921481527260894"], # Conta Brasil
        ["Página1", "act_392072550928626"]   # Conta Alemanha (ID extraído do seu print)
    ]

    data_log = datetime.now().strftime('%d/%m/%Y %H:%M')

    for aba_nome, account_id in configuracoes:
        try:
            print(f"📡 Processando dados para: {aba_nome}...")
            sheet = spreadsheet.worksheet(aba_nome)
            account = AdAccount(account_id)
            
            # Métricas solicitadas para o seu Dashboard
            fields = ['campaign_name', 'spend', 'inline_link_clicks', 'impressions', 'ctr', 'cpc', 'cpm']
            
            # Tenta hoje, se vazio (comum de manhã), pega ontem
            insights = account.get_insights(fields=fields, params={'date_preset': 'today'})
            periodo = "Hoje"
            
            if not insights:
                insights = account.get_insights(fields=fields, params={'date_preset': 'yesterday'})
                periodo = "Ontem"

            if insights:
                for ins in insights:
                    # Preparando a linha para a planilha
                    linha = [
                        data_log,
                        periodo,
                        ins.get('campaign_name'),
                        f"R$ {ins.get('spend', '0')}",
                        ins.get('inline_link_clicks', '0'),
                        ins.get('impressions', '0'),
                        f"{float(ins.get('ctr', 0)):.2f}%",
                        f"R$ {ins.get('cpc', '0')}",
                        f"R$ {ins.get('cpm', '0')}"
                    ]
                    sheet.append_row(linha)
                    print(f"✅ {aba_nome}: Linha inserida com sucesso.")
            else:
                print(f"⚠️ {aba_nome}: Sem métricas para os períodos selecionados.")

        except Exception as e:
            print(f"❌ Erro ao processar aba '{aba_nome}': {e}")

    print("--- Automação Concluída com Sucesso ---")

if __name__ == "__main__":
    monitorar_contas_mitolyn()
