import pandas as pd
from sqlalchemy import create_engine

df_lojas = pd.read_csv('./Lojas.csv')
df_produtos = pd.read_csv('./Produtos.csv')
df_clima = pd.read_csv('./Clima.csv')
df_chocolate = pd.read_csv('./Chocolate.csv')
df_vendas = pd.read_csv('./Vendas.csv')

 
usuario = 'postgres'
senha = '1234'
host = 'localhost'  # ou IP do servidor
porta = '5432'
banco = 'dbDevops'
 
engine = create_engine(f'postgresql+psycopg2://{usuario}:{senha}@{host}:{porta}/{banco}')
 
 
df_lojas.to_sql('lojas', engine, if_exists='replace', index=False)
df_produtos.to_sql('produtos', engine, if_exists='replace', index=False)
df_clima.to_sql('clima', engine, if_exists='replace', index=False)
df_chocolate.to_sql('chocolate', engine, if_exists='replace', index=False)
df_vendas.to_sql('vendas', engine, if_exists='replace', index=False)
 
print("Dados inseridos com sucesso!")