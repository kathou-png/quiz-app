from turtle import title
from asyncio.windows_events import NULL
from collections import defaultdict
import json


class Question():
 def __init__(self,id, position , title, texte, image, reponses):
    self.id = id
    self.position = position
    self.title = title
    self.texte = texte
    self.image = image
    self.reponses = reponses

 def printAttribute (self):
    print("Attribute:")
    print(self.id)
    print(self.position)
    print(self.title)
    print(self.texte)
    print(self.image)
    print(self.reponses)

 def questionToJSON(self, reponsesData):
     my_dict = {}
     print("reponses questions to json")
     print(reponsesData)
     dict_reponses = []
     for reponse in reponsesData :
        dict_reponses.append({'text': str(reponse[0]),'isCorrect': reponse[1]})
     dict_data = {
         'id' : self.id,
         'position' : self.position,
         'text' : self.texte,
         'title' : self.title,
         'image': self.image,
         'possibleanswers' : dict_reponses,
     }
     my_dict = dict_data
     my_json = json.dumps(my_dict, indent=4)
     print(my_json)
     return my_json


