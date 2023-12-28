import pandas as pd
import mysql.connector
import pymysql

conexao_vendas_2= pymysql.connect(
    host= 'localhost',
    user= 'root',
    password= '00214023vV#',
    database= 'vendas_fix',
)
cursor_vendas_2 = conexao_vendas_2.cursor()

conexao_estoque_2= pymysql.connect(
    host= 'localhost',
    user= 'root',
    password= '00214023vV#',
    database= 'bd_controle_estoque',
)
cursor_estoque = conexao_estoque_2.cursor()

df_query_vendas= "SELECT * FROM vendas"
df_query_estoque= "SELECT * FROM controle"

df_vendas= pd.read_sql(df_query_vendas, conexao_vendas_2)
df_estoque= pd.read_sql(df_query_estoque, conexao_estoque_2)

# print(df_vendas)
# print(df_estoque)

#Adicione o sort_values lá no código PYTHON da página principal !

#renomeando as colunas
df_vendas= df_vendas.rename(columns= {"number" : "numeração"})
df_vendas= df_vendas.rename(columns= {"quantidade_pecas": "quantidade"})
df_vendas= df_vendas.rename(columns= {'tipo_peca' : 'Tipo de roupa'})
df_vendas= df_vendas.rename(columns={'valor' : 'Total Vendido'})

df_estoque= df_estoque.rename(columns= {"quantidade_pecas" : "quantidade"})
df_estoque= df_estoque.rename(columns= {"tipo_peca" : "modelo"})

#referências mais vendidas
df_ref_vendas= df_vendas.groupby('ref').sum('quantidade')
df_ref_vendas= df_ref_vendas.drop(['numeração'], axis=1)
df_ref_vendas= df_ref_vendas.drop(['id'], axis=1)
df_ref_vendas.sort_values(by='quantidade', ascending=False)
#numerações mais vendidas
df_number_vendas= df_vendas[[ 'numeração', 'quantidade' ]]
df_number_vendas= df_number_vendas.groupby('numeração').sum('quantidade')
df_number_vendas.sort_values(by='quantidade', ascending=False)
#tipo de roupa mais vendidade
df_tipo_vendas= df_vendas.groupby('Tipo de roupa').sum('quantidade')
df_tipo_vendas= df_tipo_vendas[['quantidade']].sort_values(by='quantidade', ascending= False)

#----------------ESTOQUE----------------
#referências em estoque
df_ref_estoque= df_estoque[['ref', 'quantidade', 'modelo']]
df_ref_estoque= df_ref_estoque.groupby("ref").sum('quantidade')
#numerações em estoque
df_tam_estoque= df_estoque[['tamanho', 'quantidade']]
df_tam_estoque= df_tam_estoque.groupby('tamanho').sum('quantidade')
#tipo de roupa estocadas
df_tipo_peca= df_estoque[['modelo', 'quantidade']]
df_tipo_peca= df_tipo_peca.groupby("modelo").sum("quantidade")


#----------------FECHANDO O ESTOQUE----------------
cursor_estoque.close()
conexao_estoque_2.close()

#----------------FECHANDO AS VENDAS----------------
cursor_vendas_2.close()
conexao_vendas_2.close()