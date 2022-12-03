

def to_html(mylist):
    mytr = ''
    for elem in mylist:
        myline = ''
        for info in elem:
            myline += '<td>'+ str(info) + '</td>'

        mytr += '<tr>' + myline + '</tr>'

    mytab = '<table>' + mytr + '</table>'
    return mytab


def leia_meu_template(fname):
    with open( fname, encoding='utf-8' ) as myfile:
        var = ''.join(myfile.readlines())
    return var


def my_render(fname, conteudo):
    troca_tag = '<MY--TABLE>'
    mypag = leia_meu_template(fname)
    myrender = mypag.replace(troca_tag, conteudo)
    return myrender

