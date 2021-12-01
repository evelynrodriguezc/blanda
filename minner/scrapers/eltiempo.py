import requests
from lxml import html

def procesar(link):
    salida = {}
    data = requests.get(link)
    data = data.text
    loaded_html = html.fromstring(data)
    contenido = ""
    titulo = loaded_html.xpath("//h1[@itemprop]/text()")
    contenido = loaded_html.xpath('//div/p[@class="contenido"]/text()')
    salida["titulo"] = titulo[0]
    salida["contenido"] = " ".join(contenido)
    return salida

