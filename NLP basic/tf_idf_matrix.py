import pandas as pd
import re
import math

tf_matrix = {}
list_of_docs = []

########################################
def get_docs():
    global documents
    global name_of_docs
    
    while True:
        print("Please input the DOCUMENT you want to IMPORT: ")
        print("(1. Input 'over' if no more documents; 2.Input 'demo' to use example documents)\n")
        doc_name = input()
        if doc_name == 'demo':
            documents = demo_documents
            print("Input documents are: ",documents,'\n')
            for i in documents:
                file_name = re.split('\.',i)[0]
                name_of_docs.append(file_name)
            return
        elif doc_name == 'over':
            print("Input documents are: ",documents)
            for i in documents:
                file_name = re.split('\.',i)[0]
                name_of_docs.append(file_name)
            return
        else:
            documents.append(doc_name)

def sentence_tokenize(sentence, stopwords_available=False):
  # words = re.split(r"sentence|(?\s.)",sentence)
  words = re.split('\s|\.|,',sentence)
  tokens = words
  if stopwords_available == True:
    tokens = list(i for i in tokens if i.lower() not in stopwords)

  # for l in range(len(words)):    
  #   while re.match(r"^(?:,|\.|\'|'|\"|_|`|@|&|!|“|”|=|-|\+|\t|\s|\(|\)|\[|\]|\{|\}|<|>|;|:).*", words[l]):
  #     words[l] = words[l][1:]
  #   while re.match(r".*(?:,|\.|\'|'|\"|_|`|@|&|!|“|”|=|-|\+|\t|\s|\(|\)|\[|\]|\{|\}|<|>|;|:)$", words[l]):
  #     words[l] = words[l][:-1]
  #   words[l] = ss.stem(words[l])
  #   if not re.match(r"^(?:[0-9]|\$|£|€|-|–|—).*", words[l]) and words[l] != '' and words[l] not in stopword:
  #     token.append(words[l])
  return tokens

stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

def sum_and_tf(tokens, remove_low_frequency=False, low_frequency=1):
  dictionary = {}
  sentence_length = len(tokens)

  for i in tokens:
    if i in dictionary:
      dictionary[i] = dictionary[i] + 1
    else:
      dictionary[i] = 1

  matrix = pd.DataFrame.from_dict(dictionary, orient='index', columns=['sum'])
  matrix = matrix.sort_values(by=['sum'])

  matrix['tf'] = matrix['sum']/sentence_length

  if remove_low_frequency == True:
    matrix = matrix[matrix['sum']>low_frequency]

  return matrix

class Document():

  def __init__(self, tokens):
    self.tokens = tokens


  def sum_and_tf(self, remove_low_frequency=False, low_frequency=1):
    dictionary = {}
    sentence_length = len(self.tokens)

    for token in self.tokens:
      if token in dictionary:
        dictionary[token]['sum'] = dictionary[token]['sum'] + 1
        dictionary[token]['tf'] = dictionary[token]['tf'] + 1/sentence_length
      else:
        dictionary[token] = {}
        dictionary[token]['sum'] = 1
        dictionary[token]['tf'] = 1/sentence_length
        

    matrix = dictionary
    # matrix = pd.DataFrame.from_dict(dictionary, orient='index', columns=['sum'])
    # matrix = matrix.sort_values(by=['sum'])

    # matrix['tf'] = matrix['sum']/sentence_length

    # if remove_low_frequency == True:
    #   matrix = matrix[matrix['sum']>low_frequency]

    return matrix

def get_documents(path_of_docs, list_of_docs):
  document_dictionary = {}
  for doc in list_of_docs:
    name_of_doc = doc
    file_path = path_of_docs + '/' + doc
    f = open(file_path, "r")
    document_dictionary[doc] = f.read()
  return document_dictionary

list_of_docs_new = ['test.txt']
path_of_docs = '/content/drive/MyDrive'
get_documents(path_of_docs, list_of_docs)

def build_tf_matrix(path_of_docs, list_of_docs):
  # get documents for build the tf matrix
  document_dictionary = get_documents(path_of_docs, list_of_docs)

  for doc_name, doc_content in document_dictionary.items():
    tokens = sentence_tokenize(doc_content)
    tf_matrix[doc_name] = Document(tokens).sum_and_tf()

  return tf_matrix

tf_matrix = {**tf_matrix, **build_tf_matrix(path_of_docs, list_of_docs_new)}
list_of_docs = list_of_docs + list_of_docs_new
tf_matrix

def tf_idf_matrix():
  tf_idf_matrix = dict()
  for doc_name, doc_tf_matrix in tf_matrix.items():
    tf_idf_matrix[doc_name] = pd.DataFrame.from_dict(doc_tf_matrix, orient='index')
    
  tf_idf_matrix = pd.concat(tf_idf_matrix, axis=1).fillna(0.0)
  tf_idf_matrix['idf']= 0.0

  N = len(list_of_docs)
  for token in tf_idf_matrix.index:
    cnt = 0
    for doc_name in list_of_docs:
      if tf_idf_matrix.loc()[token][doc_name]['sum'] != 0:
        cnt = cnt + 1
    tf_idf_matrix['idf'][token] = math.log(N/cnt)

  return tf_idf_matrix

