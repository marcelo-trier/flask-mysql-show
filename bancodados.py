# docs e referencias:
# https://dev.mysql.com/doc/connector-python/en/connector-python-examples.html
# https://realpython.com/python-mysql/

# abaixo instalacao da biblioteca mysql do python
# pip3 install mysql-connector-python

# abaixo comando para verificar se o servidor está acessível
# ping 10.21.81.248

import mysql.connector as meubanco
import pandas

# abaixo configuracao do banco de dados!!
dbconfig = {
  'host': 'localhost',
  'user': 'bob',
  'password': 'b0b',
  'database': 'myflaskdb',
}

def pegainfo():
  mysql = meubanco.connect(**dbconfig)
  conexao = mysql.cursor()

  comando = '''
    SELECT * from myflaskdbteste
  '''

  conexao.execute(comando)
  lista = []
  for resp in conexao:
    lista.append(resp)

  conexao.close()

  return lista


def pegainfo_pandas():
  mysql = meubanco.connect(**dbconfig)
  conexao = mysql.cursor()

  comando = '''
    SELECT * from tbWil
  '''

  conexao.execute(comando)
  tabela_total = conexao.fetchall()
  df = pandas.DataFrame(tabela_total, columns=conexao.column_names)

  return df

