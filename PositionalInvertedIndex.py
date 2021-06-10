'''
An index can retrieve postings for a term from a data structure associating terms and 
the documents that contain them. 
<term, <PositionalPosting1>, <PositinalPosting2>....>
<PositionalPosting1: <docId, [pos1, pos2]...>...>
<PositionalPosting2: <docId, [pos1, pos2...]>, <docId, [pos1, pos2...]>...>

'''

'''
Steps: 
 create an index obj 
 build the corpus 
 build the index -- 
 for each doc in corpus 
    --> get content 
    --> add term into the index
'''
from Postings import PositionalPostings

class PositionalInvertedIndex: 
    
    def __init__(self):
        self.__index = {}
        # list of all terms 
        self.__mVocabulary = []
        self.__tokens = {}
        self.__terms = {}

    # def getPostings(self, term:str, position:bool):
    def getPostings(self, term:str):
        postingList = []
        if term in self.__index:
            postingList = self.__index[term]
    
        return postingList

    
    def getVocabulary(self): 
        vocabulary = self.__index.keys()
        return sorted(vocabulary)
    
 
    def addTerm(self, term:str, docId:int, ind:int):
        # if term not existed in the dictionary 
        if term not in self.__index:
            postingList = []
            # create new posting
            new_posting = PositionalPostings(docId)
            # insert the term position in postings 
            new_posting.insertIndex(ind)
            postingList.append(new_posting)
            self.__index[term] = postingList
        else: 
            # if term already exist in the dictionary 
            postingList = self.__index[term]
            # if term appear again in the same document
            if postingList[len(postingList)-1].getDocumentId() == docId: 
                posting = postingList[len(postingList)-1]
                # add new term position to the existed posting
                posting.insertIndex(ind)
            else: 
                # term appears in the new document 
                new_posting = PositionalPostings(docId)
                new_posting.insertIndex(ind)
                # add new posting into the exiting postingList 
                postingList.append(new_posting)
            
    
    
    def setTokens(self, docId:int, count:int):
        tokens[docId] = count

    def getTokenSize(self, docId:int):
        return tokens[docId]

    
    def setTerms(self, docId:int, count:int):
        terms[docId] = count
    
    def termSize(self, docId):
        return terms[docId]
    
    def getTokens(): 
        total = 0
        for count in tokens.keys(): 
            total += count
       
        return total 


