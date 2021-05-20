'''
InvertedIndexer: main driver app for the InvertedIndex  
'''

# save each file path into a dic

from InvertedIndex import InvertedIndex 
from Corpus import Corpus
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

directory = './MobyDick10Chapters'

def searchengine(directory):
    stopWords = set(stopwords.words("english"))
    # stemming
    ps = PorterStemmer()

    # create InvertedIndex obj
    invertedIndex = InvertedIndex()
    # build the corpus 
    Corp = Corpus()
    corpus = Corp.buildCorpus(directory)
    for docId in corpus: 
        doc = corpus[docId] 
        content = doc.getContent()
        # tokenize 
        tokens = word_tokenize(content)
        
        for token in tokens:
            token = token.lower()
            # apply stemming 
            token = ps.stem(token)

            # remove stopwords 
            if token in stopWords:
                continue
            # add to index 
            invertedIndex.addTerm(token, docId)
        
    return invertedIndex, corpus



indexer, corpus = searchengine(directory)
term ='find'
#need to normalize the token as well
postlist = indexer.getPostings(term)

print('searching for \"', term, '\"')
print('Found ___ ', term,' ___ in: ')
for p in postlist: 
    print(corpus[p.getDocumentId()].getTitle())

print(len(indexer.getVocabulary()))
    