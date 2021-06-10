'''
Index: contains PositionalInvertedIndex and BiwordIndex 
TODO: add more Index
'''

from PositionalInvertedIndex import PositionalInvertedIndex 
from BiwordIndex import BiwordIndex 
from Corpus import Corpus
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

class Index: 
    def __init__(self, directory):
        # invertedIndex = 'InvertedIndex'
        self.__index = []
        self.__directory = directory
        self.__corpus = self.buildCorpus()

    def PositionalInvertedIndexer(self):
        # stemming
        ps = PorterStemmer()
        # create InvertedIndex obj
        positionalInvertedIndex = PositionalInvertedIndex()
        corpus = self.__corpus
        for docId in corpus: 
            position = 1
            doc = corpus[docId] 
            content = doc.getContent()
            # tokenize 
            tokens = word_tokenize(content)
            for token in tokens:
                token = token.lower()
                # apply stemming 
                token = ps.stem(token)
                
                # add to positionalInvertedIndex 
                positionalInvertedIndex.addTerm(token, docId, position)
                position +=1
        
        return positionalInvertedIndex


    def BiwordIndexer(self):
        # stemming
        ps = PorterStemmer()
        biwordIndex = BiwordIndex()
        corpus = self.__corpus
        for docId in corpus: 
            doc = corpus[docId] 
            content = doc.getContent()
            # tokenize 
            tokens = word_tokenize(content)
            prevToken = tokens[0]
            for i in range(1,len(tokens)):
                token = tokens[i]
                token = token.lower()
                # apply stemming 
                token = ps.stem(token)
                word = prevToken + " "+ token
                prevToken = token
                # add to Biword Index text = [I love coffee] --> "I love" and "love coffee"
                biwordIndex.addTerm(word, docId) 
        
        return biwordIndex
        

    # build the corpus for the search engine app
    def buildCorpus(self):
        corpus = Corpus() 
        return corpus.buildCorpus(self.__directory)
    
    def buildIndex(self): 
        return self.PositionalInvertedIndexer(), self.BiwordIndexer()

    def getCorpus(self):
        return self.__corpus 


