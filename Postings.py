
'''
Posting store term and its position in each document
<term, docId, docId>
'''
class Postings:
    def __init__(self, documentId:int):
        self.__documentId = documentId
        self.__frequency = 0
        self.__positions = []
    
    def setTermFrequency(self,freq:int):
        self.__frequency = freq

    def getDocumentId(self): 
        return self.__documentId




# <PositionalPosting2: <docId, [pos1, pos2...]>, <docId, [pos1, pos2...]>...>

class PositionalPostings: 
    def __init__(self, documentId:int):
        self.__documentId = documentId
        self.__frequency = 0
        self.__positions = []
    
    def setTermFrequency(self,freq:int):
        self.__frequency = freq
    
    def getPositions(self): 
        return self.__positions
    
    def getDocumentId(self): 
        return self.__documentId
    
    def insertIndex(self,ind: int):
        self.__positions.append(ind)

    def resetPositions(self): 
        self.__positions = []
    