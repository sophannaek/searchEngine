'''
Biword index: is a separate inverted index that records biword phrases. 
for each pair of adjacent terms, add an index entry for the pair and the document ID

'''

from Postings import PositionalPostings

class BiwordIndex: 
    def __init__(self):
        self.__Index = {}


    # def getPostings(self, term:str, position:bool):
    def getPostings(self, term:str):
        postingList = []
        print('Getting postings in BiwordIndex.',term,'.')
        if term in self.__Index:
            postingList = self.__Index[term]

        return postingList

    
    def getVocabulary(self): 
        vocabulary = self.__Index.keys()
        return sorted(vocabulary)
    
 
    # def addTerm(self, term:str, docId:int, ind:int):
    def addTerm(self, term:str, docId:int):
        # if term not existed in the dictionary 
        if term not in self.__Index:
            postingList = []
            # create new posting
            new_posting = PositionalPostings(docId)
            # insert the term position in postings 
            postingList.append(new_posting)
            self.__Index[term] = postingList

        else: 
            # if term already exist in the dictionary 
            postingList = self.__Index[term]
            newPostings = PositionalPostings(docId)
            postingList.append(newPostings)
            self.__Index[term] = postingList
            # # if term appear again in the same document
            # if postingList[len(postingList)-1].getDocumentId() == docId: 
            #     posting = postingList[len(postingList)-1]
            #     # add new term position to the existed posting
            #     # posting.insertIndex(ind)
            # else: 
            #     # occur in new document 
            #     new_posting = PositionalPostings(docId)
            #     # new_posting.insertIndex(ind)
            #     # add new posting into the exiting postingList 
            #     postingList.append(new_posting) 

        if term == "Some years":
            print('found!')