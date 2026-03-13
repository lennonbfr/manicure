import os
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from datetime import datetime

def atualizar_logs_producao():
    print(f"--- Iniciando Coleta de Dados Reais: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ---")

    # 1. SETUP GOOGLE SHEETS
    try:
        creds_dict = json.loads(os.environ['GOOGLE_CREDS'])
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
        client = gspread.authorize(creds)
        
        spreadsheet = client.open_by_key(os.environ['SPREADSHEET_ID'])
        sheet = spreadsheet.worksheet("Manicure")
        print("✅ Conectado ao Google Sheets.")
    except Exception as e:
        print(f"❌ Erro Google Sheets: {e}")
        return

    # 2. SETUP META ADS
    try:
        FacebookAdsApi.init(access_token=os.environ['META_TOKEN'])
        # ID da conta da Escola de Manicure
        account = AdAccount('act_921481527260894')
        print("✅ Autenticado no Meta Ads.")
    except Exception as e:
        print(f"❌ Erro Meta API: {e}")
        return

    # 3. BUSCA DE INSIGHTS (Lógica hoje -> ontem)
    fields = ['campaign_name', 'spend', 'inline_link_clicks', 'impressions']
    
    # Tenta buscar hoje
    print("📡 Buscando dados de HOJE...")
    insights = account.get_insights(fields=fields, params={'date_preset': 'today'})
    
    # Se hoje estiver vazio, busca ontem
    if not insights:
        print("⚠️ Sem dados hoje. Buscando dados de ONTEM...")
        insights = account.get_insights(fields=fields, params={'date_preset': 'yesterday'})

    if not insights:
        print("ℹ️ Nenhuma métrica encontrada em ambos os períodos. Campanha pode estar em aprendizado.")
        return

    # 4. ESCRITA NA PLANILHA
    data_log = datetime.now().strftime('%d/%m/%Y %H:%M')
    
    for insight in insights:
        nome = insight.get('campaign_name', 'N/A')
        gasto = insight.get('spend', '0.00')
        cliques = insight.get('inline_link_clicks', '0')
        impressoes = insight.get('impressions', '0')
        
        linha = [data_log, "REAL", nome, gasto, cliques, impressoes]
        
        try:
            sheet.append_row(linha)
            print(f"🚀 Enviado: {nome} | Gasto: R${gasto}")
        except Exception as e:
            print(f"❌ Erro ao escrever linha: {e}")

    print("--- Processo Finalizado ---")

if __name__ == "__main__":
    atualizar_logs_producao()
