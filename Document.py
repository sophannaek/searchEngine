import json


class TextFileDocument: 
    def __init__(self, mDocumentId:int, filePath:str, fileName:str): 
        self.__mDocumentId = mDocumentId
        self.__mFilePath = filePath
        self.__mFileName = fileName

    def getFilePath(self): 
        return self.__mFilePath

    def getId(self): 
        return self.__mDocumentId
    
    def getContent(self): 
        content = ''
        # read the file content 
        with open(self.__mFilePath) as file: 
            content = file.read()
            
        return content     

    def getTitle(self): 
        return self.__mFileName.replace('.txt','')

    def loadTextFileDocument(self, filePath:str, documentId:int, fileName:str):
        return TextFileDocument(documentId, filePath, fileName)




class JsonFileDocument: 
    def __init__(self, mDocumentId:int, filePath:str, fileName:str): 
        self.__mDocumentId = mDocumentId
        self.__mFilePath = filePath
        self.__mFileName = fileName

    def getFilePath(self): 
        return self.__mFilePath
    
    def getId(self): 
        return self.__mDocumentId

    def getContent(self): 
        with open(self.__mFilePath) as file:
            content = json.load(file)

        return content['content']
        

    def getTitle(self): 
        return self.__mFileName.replace('.json','')
    
    def loadJsonFileDocument(self,filePath:str, documentId:int):
        return JsonFileDocument(documentId,filePath)
        