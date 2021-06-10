from Index import Index
from QueryParser import QueryParser
from nltk.tokenize import word_tokenize

directory = './MobyDick10Chapters'
# directory = './NationalParks'

index = Index(directory)
corpus = index.getCorpus()
positionalInvertedIndex, biwordIndex = index.buildIndex()

# query = 'love + shakes + smoothies "jamba juice" '
# query1 = ' "french vanilla" shakes + favorite drink'


# query=' \"Jamba Juice \"'
# query = ' \"dreary streets\"'
# query = '\"national park\"'
query = '[some NEAR/2 years]'
# query = 'some years'


qp = QueryParser([positionalInvertedIndex, biwordIndex])
queries = qp.parseQuery(query)
postings = queries.getPostings()
print("Found in the following file: ")
if postings: 
    for p in postings: 
        print(corpus[p.getDocumentId()].getTitle())


