import requests
from lxml import html

def procesar(link):
    salida = {}
    data = requests.get(link)
    data = data.text
    loaded_html = html.fromstring(data)
    encabezado = loaded_html.xpath('//div[@class="ArticleHeader"]/div/div/text()')
    aux = loaded_html.xpath('//p')
    print(aux)
    contenido = ""
    for a in aux:
        print(a)
        try:
            contenido += a.text
        except TypeError:
            print(type(a))
            continue
    salida["contenido"] = str(encabezado[0] + "".join(contenido)).lower().strip()
    return salida
