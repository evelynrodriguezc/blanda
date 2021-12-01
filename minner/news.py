from dataclasses import dataclass
from os import stat
from re import sub
 
class new():
    def __init__(self,title=None,link=None,newspaper=None,date=None,topic=None,subtopics=None):
        self.topic = topic
        self.title = title
        self.link = link
        self.newspaper = newspaper
        self.date = date
        self.sub_topic = subtopics

    @staticmethod
    def sumarize(texto:str)->str:
        '''aqui va el algoritmo de textrank'''
        pass 

a = new()
resumen = a.sumarize("este es mi texto de entrada")
print(resumen)
