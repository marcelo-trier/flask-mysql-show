from flask import Flask, render_template
app = Flask(__name__)

import bancodados
import mylib






@app.route('/')
def hello_world():
    msg = "<h1>hello world</h1>"
    msg += '<a href="/listar1">Listar1</a><br>'
    msg += '<a href="/listar2">Listar2</a><br>'
    msg += '<a href="/listar3">Listar3</a><br>'
    msg += '<a href="/listar_pandas1">Listar Pandas - 1</a><br>'
    msg += '<a href="/listar_pandas2">Listar Pandas - 2</a>'
    return msg



@app.route('/listar1')
def listar_banco1():
    lista = bancodados.pegainfo()

    pag = '''
    <html>
        <head>
            <link rel="stylesheet" href="/static/estilo.css">
        </head>
        <body>
            <h1>Informações do banco</h1>
            <a href="/">voltar</a>
            <br>
    '''

    mytab = ''
    for elem in lista:
        myline = ''
        for info in elem:
            myline += '<td>'+ str(info) + '</td>'

        mytab += '<tr>' + myline + '</tr>'

    pag += '<table>' + mytab + '</table>'
    pag += '</body></html>'
    return pag


@app.route('/listar2')
def listar_banco2():
    mypag = '''
        <html>
            <head>
                <link rel="stylesheet" href="/static/estilo.css">
            </head>
            <body>
                <h1>Informações do banco</h1>
                <a href="/">voltar</a>
                <br>
                <MY--TABLE>
                <br>
                <p> outras informacoes...</p>
            </body>
        </html>
    '''
    lista = bancodados.pegainfo()

    mytr = ''
    for elem in lista:
        myline = ''
        for info in elem:
            myline += '<td>'+ str(info) + '</td>'

        mytr += '<tr>' + myline + '</tr>'

    mytab = '<table>' + mytr + '</table>'
    myrender = mypag.replace('<MY--TABLE>', mytab)
    return myrender


@app.route('/listar3')
def listar_banco3():
    lista = bancodados.pegainfo()
    mytab = mylib.to_html(lista)
    mypag = mylib.my_render('teste.html', mytab)
    return mypag


@app.route('/listar_pandas1')
def listar_pandas1():
    pag = '''
    <html>
        <head>
            <link rel="stylesheet" href="/static/estilo.css">
        </head>
        <body>
            <h1>Informações do banco</h1>
            <a href="/">voltar</a>\n
    '''
    df = bancodados.pegainfo_pandas()
    pag += df.to_html(index=False)
    return pag


@app.route('/listar_pandas2')
def listar_pandas2():
    df = bancodados.pegainfo_pandas()
    myvar = df.to_html(index=False)
    return render_template('meucodigo.html', conteudo=myvar)



if __name__ == "__main__":
    app.run(debug=True, use_debugger=False, use_reloader=False)
