import requests
import pyodbc
# from sqlalchemy.orm import declarative_base, sessionmaker
# from sqlalchemy import create_engine, Column, String, Integer, DateTime
# from datetime import datetime

# URL da API
url = "https://ws.fulltrack2.com/events/all/apiKey/daaaf648667667240bafbd1c1bce713a694ee8b4/secretKey/b4b6aa652445542bf62b49e7f6aa0c9cad06c7e8"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Converter a resposta para JSON

    # Verificar se existe a chave "data" e se é uma lista
    if "data" in data and isinstance(data["data"], list):
        colaboradores = []  # Lista para armazenar os dados filtrados

        # Iterar sobre todos os veículos 
        for item in data["data"]:
            colaboradores.append({
                "ras_eve_latitude": item.get("ras_eve_latitude", ""),
                "ras_eve_longitude": item.get("ras_eve_longitude", ""),
                "ras_eve_data_gps": item.get("ras_eve_data_gps", ""),
                "ras_ras_data_ult_comunicacao": item.get("ras_ras_data_ult_comunicacao", ""),
                "ras_vei_placa": item.get("ras_vei_placa", ""),
                "ras_vei_veiculo": item.get("ras_vei_veiculo", "")
            })

 
else:
    print(f"Erro na requisição: {response.status_code}")


# conexao com o banco de dados

def conecta_ao_banco(driver='{SQL Server Native Client 11.0}', server='SRV-BI', database='SIGIDA', username='sa', password='SnlS3@123'):
    try:
        conn = pyodbc.connect(driver=driver, server=server, database=database, uid=username, pwd=password)
        print("Conexão bem-sucedida!")
        return conn
    except Exception as e:
        print("Erro ao conectar ao banco de dados:", e)

conexao = conecta_ao_banco()


# Chama a função de conexão
if conexao:
    try:
        try:
            cursor = conexao.cursor()

            query = f"INSERT INTO RESTrack 
            (placa, motorista_responsavel ,latitude ,longitude,ultima_comunicacao) 
            VALUES 
            ('?', '?', '?', '?', ? );"

            cursor.executemany(query, colaboradores);
            conn.commit();

            cursor.execute('DELETE FROM Lojas')
            conexao.commit()
            print("Registros existentes na tabela Lojas foram excluídos.")
        except Exception as e:
            print("Erro ao limpar registros existentes na tabela Lojas:", e)

        # Inserir os dados selecionados do DataFrame na tabela Lojas
        try:
            for index, row in df_selecionado.iterrows():
                cursor.execute("INSERT INTO Lojas (ID_Vendedor, Vendedor, Loja, Qtd_Vendida) VALUES (?, ?, ?, ?)", row['ID_Vendedor'], row['Vendedor'], row['Loja'], row['Qtd_Vendida'])
            conexao.commit()
            print("Dados da planilha inseridos com sucesso na tabela Lojas.")
        except Exception as e:
            print("Erro ao inserir dados na tabela Lojas:", e)
    finally:
        # Fecha a conexão com o banco de dados
        conexao.close()
else:
    print("Não foi possível conectar ao banco de dados.")