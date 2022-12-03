from flask import Flask, render_template
app = Flask(__name__)

import bancodados
import mylib
import pandas



@app.route('/')
def hello_world():
    msg = '''
        <h1>hello world</h1>
        <a href="/listar_pandas">Listar Pandas</a>
    '''
    return msg


@app.route('/listar_pandas')
def listar_pandas():
    lista = bancodados.capturar_nome_tabelas()

    lista_pandas = []
    lista_tabs = ''

    for nome in lista:
        df = bancodados.captura_registros(nome)
        df.columns = ['id', 'prod', 'cli', 'qtde', 'preco']
        lista_pandas.append(df)
    
    df = pandas.concat(lista_pandas, ignore_index=True)
    df = df[['prod', 'cli', 'qtde', 'preco']]
    lista_tabs = df.to_html(index=False)

    return render_template('meucodigo.html', conteudo=lista_tabs)

if __name__ == "__main__":
    app.run(debug=True, use_debugger=False, use_reloader=False)
