'''
    Corpus Index: 
    contain list of file corresponds with its id and fileName 
'''

import os
from Document import TextFileDocument, JsonFileDocument


class Corpus: 
    def __init__(self): 
        self.__corpus = {}
        self.__index = 1
        
    def buildCorpus(self, directory):
        for filename in os.listdir(directory):
            title = filename
            filePath = os.path.join(directory,filename)
            if filename.endswith(".txt"):     
                textFile = TextFileDocument(self.__index, filePath, filename)
                self.__corpus[self.__index] = textFile
                self.__index +=1

            elif filename.endswith('.json'):
                jsonFile = JsonFileDocument(self.__index, filePath, filename)
                self.__corpus[self.__index] = jsonFile
                self.__index +=1
                
            else: 
                print("the document format is not supported!")
            
        return self.__corpus
        

    

