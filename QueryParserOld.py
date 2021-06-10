class QueryParser: 
    def __init__(self): 
        self.__queries = []
        self.__components = []
        pass
    
    # given a boolean query, parses and returns a tree querycomponents
    # representing the query 
    def parseQuery(self, query): 
        # splits query based on its type 
        # check if there is + --> OR query 
       
        # while(len(query) != 0 ):
        # if "\'" in query or "+" in query: 
        #     self.findNextSubQuery(query)
        # isNextQuery = True
        while(query != ""):
            query = self.findNextSubQuery(query)
        
        print('queries are: ', self.__queries)


        
        


    def findNextSubQuery(self,query): 
        if '+' in query: 
            # split this with the at the +
            # it is a OR query 
            # shakes + smoothies mango   --> [shakes, smoothies mango] --> [shakes or (smoothies and mango)]
            q = query.split('+')
            print(q)
            self.__queries.append(q[0])
            # self.__components.append(OrQuery(q[0]))
            if len(q) >= 1:
                query = " ".join(q[1:])
                print('query: ', query)
        
        if "\'" in query:
            q = query.split("\'")
            print('q ', q)
            self.__queries.append(q[0])
            if len(q) >= 1: 
                query=" ".join(q[1:])
            
            # shakes "jamba juice "  --> [shakes, "jamba juices"]--> [shakes and "jamba juices"]
        else:
            self.__queries.append(query)
            return ""

        # print(self.__queries) 
        return query

    def findNextLiteral(): 
        pass
    




# test 
from nltk.tokenize import word_tokenize

query = "shakes + drink + smoothies 'jamb juice' "

# token = word_tokenize(query)
# for t in token: 
#     print(t)
    # if t == "\`":
    #     print("..")
# if '+' in query: 
#     sub = query[0:query.find('+')]
#     print(sub)
# start = 0
# end = len(query)
# lis = []
# while('+' in query):
#     # if '+' in query:
#     sub = query[start:query.find('+')]
#     lis.append(sub)
#     start = query.find('+')+1
#     print(start)
#     query = query[start:]
#     print(sub)


qp = QueryParser()
qp.parseQuery(query)