import os
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

def rodar_teste_funcional():
    print(f"--- INICIANDO TESTE FUNCIONAL (MOCK DATA): {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ---")

    # 1. SETUP GOOGLE SHEETS
    try:
        creds_dict = json.loads(os.environ['GOOGLE_CREDS'])
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
        client = gspread.authorize(creds)
        
        spreadsheet = client.open_by_key(os.environ['SPREADSHEET_ID'])
        sheet = spreadsheet.worksheet("Manicure")
        print("✅ Google Sheets: Conexão OK. Aba 'Manicure' localizada.")
    except Exception as e:
        print(f"❌ Erro Google Sheets: {e}")
        return

    # 2. SIMULAÇÃO DE DADOS (MOCK)
    # Como a campanha é nova, criamos dados fictícios para validar o 'append_row'
    print("📡 Simulando dados da API do Meta (Teste de Campanha Recém-Criada)...")
    
    mock_insights = [
        {
            'campaign_name': 'TESTE_SISTEMA_MITOLYN',
            'spend': '0.01',
            'inline_link_clicks': '1',
            'impressions': '10'
        }
    ]

    # 3. ESCRITA NA PLANILHA
    data_execucao = datetime.now().strftime('%d/%m/%Y %H:%M')

    for insight in mock_insights:
        linha = [
            data_execucao, 
            "TESTE_SISTEMA", 
            insight['campaign_name'], 
            insight['spend'], 
            insight['inline_link_clicks'], 
            insight['impressions']
        ]
        
        try:
            sheet.append_row(linha)
            print(f"🚀 SUCESSO: Linha de teste escrita na aba Manicure!")
            print(f"Dados enviados: {linha}")
        except Exception as e:
            print(f"❌ Erro ao escrever na planilha: {e}")

    print("--- FIM DO TESTE: Sistema Validado e Pronto para Dados Reais ---")

if __name__ == "__main__":
    rodar_teste_funcional()
