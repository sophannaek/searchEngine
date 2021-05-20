'''
Building  an inverted index: 
1. collect the documents to be indexed 
2. tokenize the text 
3. do linguistic processing (normalization)
4. for each token, add the documentID to the term's postings list 
'''


from Postings import Postings

class InvertedIndex: 
    def __init__(self): 
        self.__dic = {}
    
    def addTerm(self, term:str, docId:int):
        # if term is in the dic
        if term in self.__dic: 
            postingList = self.__dic[term]
            # add new posting with the docId if the docId is not the same 
            lastPost = postingList[len(postingList)-1]
            if (docId != lastPost.getDocumentId()):
                postingList.append(Postings(docId))
            
        else: 
            posting = Postings(docId)
            postingList = []
            postingList.append(posting)
            self.__dic[term] = postingList

    
    def getPostings(self, term:str):
        postingList = []
        if term in self.__dic: 
            postingList = self.__dic[term]

        return postingList
    

    def getVocabulary(self):
        # need to sort 
        vocabulary = self.__dic.keys()
        
        return sorted(vocabulary)

