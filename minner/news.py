from summa.summarizer import summarize
import importlib
class new():
    def __init__(self,title=None,link=None,newspaper=None,date=None,topic=None,subtopics=None):
        self.topic = topic
        self.title = title
        self.link = link
        self.newspaper = "".join(newspaper.lower().split(" "))
        self.date = date
        self.sub_topic = subtopics
        self.scraper = importlib.import_module(f"scrapers.{self.newspaper}")
        self.text = self.scraper.procesar(self.link)["contenido"]
        
    def make_sumary(self)->str:
        return summarize(self.text,language="spanish")

#a = new()
#resumen = a.make_sumary('''Cuando Frank Esteban Gómez Arias se dirigía hacia Girardota, donde trabajaba como operario en una empresa textil, fue asesinado.
#El homicidio ocurrió durante la madrugada del jueves, 9 de diciembre. El hombre, de 27 años de edad, salió de su residencia, ubicada en la vereda La Chorrera de Barbosa, sobre las 5:00 de la mañana. Bajó caminando por la vía principal que de ese municipio conduce a Concepción, alumbrando con una linterna.
#Minutos más tarde, cuando se encontraba en el sector conocido popularmente como Los Lavaderos, fue interceptado por un hombre que iba en una motocicleta, quien se bajó y le disparó. Frank Esteban falleció en el sitio a causa de una lesión en la cabeza.
#Las razones y los responsables del crimen se desconocen y se encuentran en investigación por parte de las autoridades. Por el momento están buscando testigos y revisando cámaras de seguridad para obtener pistas. Q’HUBO conoció que el occiso no tenía amenazas y tampoco anotaciones judiciales en el Sistema Penal Oral Acusatorio.
#El crimen fue rechazado por los vecinos de la víctima, quienes indicaron que era un muchacho muy trabajador, servicial y colaborativo con todos los habitantes de la vereda. Justamente el pasado sábado se había reunido con ellos para colaborar en la pavimentación de la vía principal del sector.
#''')
#print(resumen)


