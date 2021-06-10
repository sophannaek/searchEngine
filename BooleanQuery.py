
'''

Process: 
- Boolean operators: AND, OR , NOT , NEAR query 
- Note: postings lists are in increasing order by docId
- retrieve postings for X, for Y 
- Intersect postings 
- Repeat

'''
from nltk.tokenize import word_tokenize
from Postings import PositionalPostings
import math


'''
AndQuery
'''
class AndQuery:
    def __init__(self, literals, index):
        self.__literals = literals 
        self.__index = index
        
    def getQueryToken(self, query:str):
        # query = query.lower()
        # self.__tokens = word_tokenize(query)
        return self.__literals


    def getPostings(self):
        queries = self.__literals
        result = queries[0].getPostings()
        for i in range (1, len(queries)): 
            postingList = queries[i].getPostings()
            result = self.AndMerge(result, postingList)

        return result 

    # Do AndQuery Merge -- Intersecting the resulting postings 
    def AndMerge(self, PostingsList1, PostingsList2):
        result = []
        position1 = 0
        position2 = 0
        # print('doing andMerge....')
        # print('posting1...', PostingsList1)
        # print('posting2...', PostingsList2)


        while ( position1 < len(PostingsList1) and position2 < len(PostingsList2)):
            first = PostingsList1[position1]
            second = PostingsList2[position2]
            if first.getDocumentId() == second.getDocumentId() :
                result.append(PostingsList1[position1])
                position1 += 1
                position2 += 1

            elif ( first.getDocumentId() < second.getDocumentId()):
                position1 += 1 
            else: 
                position2 += 1 

        return result 


    def print(self):
        print(self.__literals)
        
   


'''
OrQuery 
'''
class OrQuery: 
    def __init__(self, literals, index): 
        self.__literals = literals
        self.__index = index
    
    '''
     Retrieves a list of postings for the query component, using an Index as the source.
    '''
    def getPostings(self): 
        queries = self.__literals
        # print("vocab ", index.getVocabulary())
        # result = queries[0].getPostings(self.__index)
        result = queries[0].getPostings()
        self.printDocId(result)
        print('first query...',queries[0], queries[0].getQueryToken())
        print('result ...', result)
        for i in range(1, len(queries)): 
            postingList = queries[i].getPostings()
            self.printDocId(postingList)
            # postingList = index.getPostings(q)
            result = self.OrMerge(result, postingList)

        return result 
    
    # merge two posting lists -- Or Merge 
    def OrMerge(self, PostingsList1, PostingsList2):
        print('inside ormerge...',PostingsList1)
        result = []
        position1 = 0
        position2 = 0
        while ( position1 < len(PostingsList1) and position2 < len(PostingsList2)):
            first = PostingsList1[position1]
            second = PostingsList2[position2]
            if first.getDocumentId() == second.getDocumentId() :
                result.append(first)
                position1 += 1
                position2 += 1

            elif ( first.getDocumentId() < second.getDocumentId()):
                result.append(first)
                position1 += 1 
            else: 
                result.append(second)
                position2 += 1 
       
        # take care the left over postingsList 
        if position1 < len(PostingsList1):
            result.append(PostingsList1[position1])
            position1 += 1
        if position2 < len(PostingsList2):
            result.append(PostingsList2[position2])
            position2 += 1

        return result 
        

    def print(self):
        for lit in self.__literals: 
            print(lit)
            lit.print()

    def printDocId(self,postingList): 
        for p in postingList: 
            print(p.getDocumentId())


    def getComponent(self):
        return self.__literals


'''
PhraseLiteral: Liteal object to support Phrase query 
'''
class PhraseLiteral: 
    def __init__(self, literals, index):
        self.__literals = literals
        self.__index = index 

    def getPostings(self):
        queries = self.__literals
        return self.__index.getPostings(queries)
        
    def print(self):
        print(self.__literal)






'''
NearLiteral: Literal object to support NEAR query
'''
class NearLiteral: 
    def __init__(self,literals, index, offset:int):
        self.__literals = literals 
        self.__index = index 
        self.__offset = offset 

    def getPostings(self):
        queries = self.__literals 
        postingList1 = self.__index.getPostings(self.__literals[0])
        postingList2 = self.__index.getPostings(self.__literals[1])
        result = self.PositionalMerge(postingList1, postingList2, self.__offset)
        return result 


    '''
    program this method. Retrieve the postings for the individual terms in the phrase,
            // and positional merge them together.
    Order of the term appearance matter Baseball Near/2 Angels --> Baseball must appear before Angels 
    '''   
    def PositionalMerge(self,PostingsList1, PostingsList2, offset):
        mergeResult = []
        mergeDict = {}
        postlist = []
        position1 = 0
        position2 = 0
        while ( position1 < len(PostingsList1) and position2 < len(PostingsList2)):
            first = PostingsList1[position1]
            second = PostingsList2[position2]
           
            if first.getDocumentId() == second.getDocumentId() :
                result=[]
                pos1 = first.getPositions() 
                pos2 = first.getPositions() 
            
                l1= l2 = 0
                while(l1 < len(pos1)):
                    while (l2 < len(pos2)):
                        # terms appear near each other within the k offset 
                        if abs(pos1[l1] - pos2[l2]) <= offset: 
                            # add this position 
                            result.append(pos2[l2])
                        elif(pos2[l2] > pos1[l1]):
                            break
                        l2 += 1

                    # left over position in pos1                         
                    while((len(result) != 0) & (abs(result[0] - pos1[l1]) > offset)):
                        result.remove(result[0])
                    
                    if first.getDocumentId() in mergeDict: 
                    
                        postings = mergeDict[first.getDocumentId()]
                        positionslist = postings.getPositions()
                        for pos in result: 
                            if pos not in positionslist: 
                                positionslist.append(pos)
                        postings.setPositions(positionslist)
                        mergeDict[first.getDocumentId()] = postings

                    else: 
                        postings = PositionalPostings(first.getDocumentId())
                        postings.setPositions(result)
                        mergeDict[first.getDocumentId()] = postings 
                    
                    postings.setPositions(result)
                    l1 += 1
                    if (len(result) != 0):
                        if first.getDocumentId() not in postlist: 
                            postlist.append(first.getDocumentId())

                    position1 += 1
                    position2 += 1

            elif ( first.getDocumentId() < second.getDocumentId()):
                position1 += 1 
            else: 
                position2 += 1 
        
        for docId in mergeDict.keys(): 
            mergeResult.append(mergeDict[docId])

        return mergeResult
    


'''
TermLiteral: 
'''
class TermLiteral: 
    def __init__(self, literal, index):
        print('initialize termLiteral....', literal)
        literal = literal.replace(' ','')
        self.__term = literal
        self.__index = index 


    def getPostings(self):
        print('Getting postings in termLiteral...', self.getQueryToken())
        term = self.getQueryToken()    
        return self.__index.getPostings(term)

    def print(self):
        print(self.__term)

    def getQueryToken(self):
        print('getquerytoken: \"', self.__term,'\"')
        return self.__term




'''
Wildcard queries
'''
class WildcardLiteral: 
    def __init__(self, literal, index):
        self.__literal = literal
        self.__index = index 

    def getPostings(self):
        pass

