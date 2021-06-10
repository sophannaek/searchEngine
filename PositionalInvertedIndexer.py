'''
PositionalInvertedIndexer: main driver app for the InvertedIndex  
'''

# save each file path into a dic
from PositionalInvertedIndex import PositionalInvertedIndex 
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
    positionalInvertedIndex = PositionalInvertedIndex()
    # build the corpus 
    Corp = Corpus()
    corpus = Corp.buildCorpus(directory)
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

            # remove stopwords 
            if token in stopWords:
                continue
            # add to index 
            positionalInvertedIndex.addTerm(token, docId, position)
            position +=1
        
    return positionalInvertedIndex, corpus



indexer, corpus = searchengine(directory)
term ='how long'
#need to normalize the token as well
postlist = indexer.getPostings(term)

print('searching for \"', term, '\"')
print('Found ___ ', term,' ___ in: ')
for p in postlist: 
    print(corpus[p.getDocumentId()].getTitle())
    
# print(len(indexer.getVocabulary()))

