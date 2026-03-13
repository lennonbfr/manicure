import os
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from datetime import datetime

def atualizar_logs():
    print(f"--- Iniciando Automação: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ---")

    # 1. SETUP GOOGLE SHEETS
    try:
        creds_dict = json.loads(os.environ['GOOGLE_CREDS'])
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
        client = gspread.authorize(creds)
        
        # Conectando pelo ID da planilha e aba específica
        spreadsheet = client.open_by_key(os.environ['SPREADSHEET_ID'])
        sheet = spreadsheet.worksheet("Manicure")
        print("✅ Google Sheets: Conexão e aba 'Manicure' validadas.")
    except Exception as e:
        print(f"❌ Erro Google Sheets: {e}")
        return

    # 2. SETUP META ADS
    try:
        FacebookAdsApi.init(access_token=os.environ['META_TOKEN'])
        # ID da conta da Escola de Manicure
        account = AdAccount('act_921481527260894')
        print("✅ Meta Ads API: Autenticação realizada.")
    except Exception as e:
        print(f"❌ Erro Meta API (Auth): {e}")
        return

    # 3. BUSCA DE DADOS (Insights)
    fields = ['campaign_name', 'spend', 'inline_link_clicks', 'impressions']
    
    # Tenta hoje, se vazio, tenta ontem
    periodos_para_testar = ['today', 'yesterday']
    insights = None
    periodo_final = ""

    for periodo in periodos_para_testar:
        print(f"📡 Solicitando dados do Meta para: {periodo}...")
        dados = account.get_insights(fields=fields, params={'date_preset': periodo})
        if dados:
            insights = dados
            periodo_final = periodo
            break
    
    if not insights:
        print("⚠️ Resultado: Nenhuma métrica encontrada para hoje ou ontem. Verifique se as campanhas estão ativas.")
        return

    # 4. ESCRITA NA PLANILHA
    print(f"📊 Processando {len(insights)} linhas de dados de '{periodo_final}'...")
    data_execucao = datetime.now().strftime('%d/%m/%Y %H:%M')

    for insight in insights:
        nome_campanha = insight.get('campaign_name', 'N/A')
        gasto = insight.get('spend', '0.00')
        cliques = insight.get('inline_link_clicks', '0')
        impressoes = insight.get('impressions', '0')
        
        # Estrutura da linha: Data | Período | Campanha | Gasto | Cliques | Impressões
        linha = [data_execucao, periodo_final, nome_campanha, gasto, cliques, impressoes]
        
        try:
            sheet.append_row(linha)
            print(f"🚀 Log enviado: {nome_campanha} | R${gasto}")
        except Exception as e:
            print(f"❌ Erro ao inserir linha na planilha: {e}")

    print("--- Fim da Execução com Sucesso ---")

if __name__ == "__main__":
    atualizar_logs()
