'''
QueryParser class parse query into different types of boolean queries: ANDs, ORs, Phrase literal, and NEAR operator 
NEAR Query: [baseball NEAR/2 angels]
Phrase Query: input with quote ""
Expanded Query: DNF query 

'''

from BooleanQuery import AndQuery, OrQuery, PhraseLiteral, TermLiteral, NearLiteral
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

class QueryParser: 
    def __init__(self, index): 
        self.__components = []
        self.__index = index
    

    '''
    Given a boolean query, parses and returns a tree querycomponents
    representing the query
    ''' 
    def parseQuery(self, query):
        ps = PorterStemmer()
        allsubqueries = [] 
    
        tokens = word_tokenize(query)
        # print('tokens ', tokens)
        terms = []
        for token in tokens:
            token = token.lower() 
            terms.append(ps.stem(token))
        query = ' '.join(terms)
        

        if '[' in query: 
            # it is near query 
            query = query.replace('[','')
            query = query.replace(']','')
            query = query.split('near/')
            # print(query)
            offset = query[1].split(' ')
            
            # print(offset)
            literals = []
            literals.append(self.cleanText(query[0]))
            literals.append(self.cleanText(offset[1]))
            offset = int(offset[0])
            # literal = ' '.join(literals)
            print('near query ', literals)
            return NearLiteral(literals,self.__index[0], offset)

        while (query != ""):
            nextSubquery, query  = self.findNextSubQuery(query)
            # print("next subquery ...", nextSubquery)
            # break nextSubquery down into literals if any 
            # while(nextSubquery != '' or nextSubquery != ' ' or nextSubquery != None ):
            subqueryLiterals = []
            while(nextSubquery or nextSubquery != "" or nextSubquery ==" "):
                
                nextSubquery, literal = self.findNextLiteral(nextSubquery)

                # print("literal ==> ", literal)
                subqueryLiterals.append(literal)
                if nextSubquery == "" or nextSubquery == " ":
                    break

            # print('subqueryLiterals ...', subqueryLiterals)
            if len(subqueryLiterals) == 1:
                allsubqueries.append(subqueryLiterals[0])
            else: 
                allsubqueries.append(AndQuery(subqueryLiterals, self.__index[0]))


        # only contain one literal 
        if len(allsubqueries) == 1:
            return allsubqueries[0]
        elif len(allsubqueries) > 1: 
            return OrQuery(allsubqueries, self.__index[0])
        else: 
            return None

   
    def findNextLiteral(self, subquery):
        # print("inside nextLiteral ...", subquery)
        literal = ""
        start = 0
        lengthOut = 0
        length = len(subquery)
        char = subquery[start]
        while(start < length and char == " "):
            start += 1
            char = subquery[start]
       
        # Phrase Literal
        if char == '\"':
            print("startIndex ..", start)
            # nextQuote = subquery[start+1:].find('\"')
            nextQuote = subquery.find('\"', start+1, len(subquery))
            # print("nextquote ..",nextQuote, subquery[nextQuote])
            if nextQuote > 0 :
                print("1")
                text = self.cleanText(subquery[start+1:nextQuote])
                literal = PhraseLiteral(text, self.__index[1])
                subquery = subquery[nextQuote+ 1:]
            else: 
                # no next quote 
                print('2')
                literal = PhraseLiteral(subquery[start+1:], self.__index[1])
                subquery = ""
        else:
            # Locate space to find the end of tis literal 
            # print('finding nextpace')
            nextSpace = subquery.find(' ', start+1, len(subquery))
            # no more literals in this subquery
            if nextSpace < 0: 
                literal = TermLiteral(subquery[start:], self.__index[0])
                subquery = ""
                print('3')
            else: 
                literal = TermLiteral(subquery[start:nextSpace+1],self.__index[0])
                if nextSpace + 1 < length: 
                    subquery = subquery[nextSpace+1:]
                    print('4')
                else: 
                    subquery = ""
                    print('5')
        
        return subquery, literal



    '''
    Locates the start index and length of the next subquery in the given query 
    '''
    def findNextSubQuery(self, query):
        nextSubquery = ""
        start = 0
        length = len(query)
        
        char = query[start]
        while ( char == ' ' or char == '+' ):
            start += 1
            char = query[start]

        # find nextPlus sign
        nextPlus = query[start:].find('+')
        # This is final subquery 
        if nextPlus < 0:
            nextSubquery = query[start:]
            query=''
        else: 
            # There is another + sign, then the length of this subquery goes to the next + sign 
            nextSubquery = query[start:nextPlus]
            query = query[nextPlus+1:]

        return nextSubquery, query
    


    def cleanText(self,text):
        text = text.split(' ')
        while ('' in text):
            text.remove('')
        text = ' '.join(text)

        return text






# # test cases
'''
query: shakes "Jamba Juice" ==> Q1 with 2 positive literals (shakes and "Jamba Juice")
query: shakes + smoothies mango
==> Q1 = shakes and Q2 = smoothies mango 
query = 'love + shakes + smoothies "jamba juice" '
==> love OR shakes OR (smoothies AND "jamba juice")
query = ' "french vanilla" shakes + favorite drink'
===> ("french vanilla" AND shakes) OR (favorite AND drink )

query = 'smoothies (mango + banana) + "vanilla shakes" 
===> (smoothies mango OR smoothies banana) OR "vanilla shakes 
'''
