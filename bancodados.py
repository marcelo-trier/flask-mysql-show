import mysql.connector as meubanco
import pandas

# abaixo configuracao do banco de dados!!
dbconfig = {
  'host': 'localhost',
  'user': 'bob',
  'password': 'b0b',
  'database': 'myflaskdb',
}

mysql = meubanco.connect(**dbconfig)
conexao = mysql.cursor()

def capturar_nome_tabelas():
  comando = 'SHOW TABLES'
  conexao.execute(comando)
  lista_nomes = []
  for registro in conexao:
    lista_nomes.append(registro[0])

  return lista_nomes


def captura_registros(nome_tab):
  comando = f'SELECT * from {nome_tab}'
  conexao.execute(comando)
  tabela_total = conexao.fetchall()
  df = pandas.DataFrame(tabela_total, columns=conexao.column_names)

  return df
