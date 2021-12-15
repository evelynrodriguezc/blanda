import re
import site
import os
import requests
from GoogleNews import GoogleNews
site.addsitedir(os.path.dirname(os.path.abspath(__file__)))
from news import new
noise_words = ["es","article","es-co","noticias","articulo","noticia","news","deporte-total","espanol","spa","top","fotogalerias","mas-deportes","seleccion","respuestas","tendencias","nota","notas","item","campaigns","tutoriales","columnistas","los40","los40classic"]
noise_extensions = ["html","aspx"]

class minner():
    news = []
    def __init__(self,topic):
        self.client = GoogleNews(lang="es",period="1d",encode="utf-8",region="col")
        self.topic = topic
    
    def search(self):
        self.client.get_news(self.topic)
        raw_news = self.client.result()
        i = 0
        m = 150
        while i <= m:
            print(i)
            try:
                n = raw_news[i]
            except IndexError:
                break
            destination = requests.get(f"https://{n['link']}").url
            metadata = self.get_link_info(destination)
            cleaned_metadata = {}
            if metadata != []:
                cleaned_metadata = self.analyze_metadata(metadata)
                if cleaned_metadata["date"] == "":
                    cleaned_metadata["date"] = self.analyze_link(destination)
            else:
                cleaned_metadata["date"] = self.analyze_link(destination)
            cleaned_metadata["link"] = destination
            cleaned_metadata["title"] = n["title"]
            cleaned_metadata["newspaper"] = n["site"]
            cleaned_metadata["topic"] = self.topic
            try:
                aux_new = new(**cleaned_metadata)
                self.news.append(aux_new)
            except ModuleNotFoundError:
                print(f"falta el periodico {cleaned_metadata['newspaper']}")
            finally:
                i += 1

    def get_link_info(self,link):
        aux = link.split("/")[3:]
        metada = [a for a in aux 
        if a != "" and 
        a.count("-") <= 3 and 
        self.topic != a and 
        a not in noise_words and 
        a.split(".")[-1] not in noise_extensions
        ]
        return metada

    def analyze_metadata(self,metadata):
        aux = {"date":"",
        "subtopics":[]
        }
        if len(metadata) == 3:
            try:
                date = f"{int(metadata[2])}-{int(metadata[1])}-{int(metadata[0])}"
                aux["date"]=date
            except ValueError:
                pass
        for m in metadata:
            if len(m.split("-")) == 3:
                aux["subtopics"].append(m)
                continue
            if self.topic in m:
                continue
            try:
                int(m)
                continue
            except ValueError:
                aux["subtopics"].append(m)
        return aux

    @staticmethod
    def analyze_link(link):
        regex = re.compile(r"[0-9]{2}-[0-9]{2}-[0-9]{4}")
        out = regex.search(link)
        try:
            return str(out.group())
        except AttributeError:
            return ""

a = minner("deportes")
print("busqueda inicial")
a.search()
print("extras")
for n in a.news:
    print(n.link,n.sub_topic)
    print(n.make_sumary())
