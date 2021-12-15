import requests
from lxml import html

def procesar(link):
    salida = {}
    data = requests.get(link)
    data = data.text
    loaded_html = html.fromstring(data)
    encabezado = loaded_html.xpath('//div[@class="ArticleHeader"]/div/div/text()')
    contenido = loaded_html.xpath('//p/text()')
    salida["contenido"] = str(encabezado[0] + " ".join(contenido)).lower().strip()
    return salida
