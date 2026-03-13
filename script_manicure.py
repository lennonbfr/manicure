import os
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from datetime import datetime

# 1. SETUP GOOGLE SHEETS (Usando a Secret GOOGLE_CREDS)
try:
    creds_dict = json.loads(os.environ['GOOGLE_CREDS'])
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(os.environ['SPREADSHEET_ID']).worksheet("Manicure")
    print("✅ Conectado ao Google Sheets")
except Exception as e:
    print(f"❌ Erro Google Sheets: {e}")

# 2. SETUP META ADS (Usando a Secret META_TOKEN)
try:
    FacebookAdsApi.init(access_token=os.environ['META_TOKEN'])
    # ID da conta que registramos anteriormente
    account = AdAccount('act_921481527260894')
    print("✅ Conectado ao Meta Ads")
except Exception as e:
    print(f"❌ Erro Meta API: {e}")

def atualizar_logs():
    # Puxando métricas de hoje
    fields = ['campaign_name', 'spend', 'inline_link_clicks', 'impressions']
    params = {'date_preset': 'today'}
    
    insights = account.get_insights(fields=fields, params=params)
    
    data_hoje = datetime.now().strftime('%d/%m/%Y %H:%M')

    for insight in insights:
        # Preparando a linha para a planilha
        nome_campanha = insight.get('campaign_name', 'N/A')
        gasto = insight.get('spend', '0')
        cliques = insight.get('inline_link_clicks', '0')
        impressoes = insight.get('impressions', '0')
        
        linha = [data_hoje, nome_campanha, gasto, cliques, impressoes]
        
        # Adiciona no final da planilha aba "Manicure"
        sheet.append_row(linha)
        print(f"🚀 Log enviado: {nome_campanha} | Gasto: R${gasto}")

if __name__ == "__main__":
    atualizar_logs()
