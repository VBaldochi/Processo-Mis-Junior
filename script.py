import sqlite3
import pandas as pd

# Conectar ao banco de dados
path_db_original = 'Dataset/DB_ORIGEM_DESTINO_SP.sqlite'
conn = sqlite3.connect(path_db_original)

# Lista de tabelas no banco de dados
query = "SELECT name FROM sqlite_master WHERE type='table';"
tables = pd.read_sql_query(query, conn)
print("Tabelas encontradas no banco de dados:")
print(tables)

# Carregar a tabela 'dados_gerais'
df_dados_gerais = pd.read_sql_query("SELECT * FROM dados_gerais", conn)

# Fechar a conexão com o banco original
conn.close()

# Remover colunas que estão completamente nulas
df_dados_gerais = df_dados_gerais.dropna(axis=1, how='all')

# Verificar e tratar valores da coluna 'RENDA_FA'
df_dados_gerais.fillna({'RENDA_FA': df_dados_gerais['RENDA_FA'].median()}, inplace=True)

# Converter coluna 'IDADE' para inteiro
df_dados_gerais['IDADE'] = df_dados_gerais['IDADE'].astype(int)

# Converter coluna 'RENDA_FA' para float
df_dados_gerais["RENDA_FA"] = df_dados_gerais["RENDA_FA"].astype(float)

# Criar uma nova coluna faixa etária
bins = [0, 18, 30, 45, 60, 100]
labels = ['0-18', '19-30', '31-45', '46-60', '60+']
df_dados_gerais['FAIXA_ETARIA'] = pd.cut(df_dados_gerais['IDADE'], bins=bins, labels=labels, right=False)

# Converter a coluna DATA ( DDMMYYYY para YYYY-MM-DD)
df_dados_gerais['DATA'] = pd.to_datetime(df_dados_gerais['DATA'], format='%d%m%Y')

# Exportar o DataFrame transformado para um arquivo CSV
df_dados_gerais.to_csv('dados_tratados.csv', index=False, float_format='%.2f')

print("\nNovos dados tratados e exportados para 'dados_tratados.csv'")


