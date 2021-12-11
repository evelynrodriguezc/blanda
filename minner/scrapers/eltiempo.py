import requests
from lxml import html

def procesar(link):
    salida = {}
    data = requests.get(link)
    data = data.text
    loaded_html = html.fromstring(data)
    contenido = ""
    contenido = loaded_html.xpath('//div/p[@class="contenido"]/text()')
    salida["contenido"] = " ".join(contenido)
    return salida

