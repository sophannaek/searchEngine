'''
    Corpus Index: 
    * contain list of file corresponds with its id and fileName 
    * currently supports text and JSON files
'''

import os
from Document import TextFileDocument, JsonFileDocument


class Corpus: 
    def __init__(self): 
        self.__corpus = {}
        self.__counter = 1
        
    def buildCorpus(self, directory):
        for filename in os.listdir(directory):
            title = filename
            filePath = os.path.join(directory,filename)
            if filename.endswith(".txt"):     
                textFile = TextFileDocument(self.__counter, filePath, filename)
                self.__corpus[self.__counter] = textFile
                self.__counter +=1

            elif filename.endswith('.json'):
                jsonFile = JsonFileDocument(self.__counter, filePath, filename)
                self.__corpus[self.__counter] = jsonFile
                self.__counter +=1
                
            else: 
                print("the document format is not supported!")
            
        return self.__corpus
        

    

