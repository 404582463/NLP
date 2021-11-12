import pandas as pd
import re
import math
import stopwords

tf_matrix = {}
list_of_docs = []

class Tfidf():
  """
  Get a dataframe from given documents.

  Paramenters
  -----------
  documents : a list of strings.
    This is the tokenized documents.

  remove_low_frequency : Bool, default False.
    remove tokens with low frequency or not,
  
  low_term_frequency : int, default 1.
    Define what is a low frequency, and those tokens apper less than this frequency will be removed. 
    For example, user can construct a tf_idf matrix without considering those low frequency tokens 
    since they 

  Examples
  --------
  Get tf-idf from given documents.

  >>>

  """

  def __init__(
      self, 
      path_of_docs,
      list_of_docs,
      remove_low_frequency = False,
      low_term_frequency = 1

  ):

    self.path_of_docs = path_of_docs
    self.list_of_docs = ist_of_docs
  
  # calculate the term sum and term frequency in a document
  # and return a dictionary contains these information
  def sum_and_tf(
      tokens, 
      remove_low_frequency=False, 
      low_frequency=1
  ):
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

  def build_tf_matrix(self.path_of_docs, self.list_of_docs):
    # get documents for build the tf matrix
    document_dictionary = get_documents(path_of_docs, list_of_docs)

    for doc_name, doc_content in document_dictionary.items():
      tokens = sentence_tokenize(doc_content)
      tf_matrix[doc_name] = Document(tokens).sum_and_tf()

    return tf_matrix

  def build_idf_matrix():
    idf_matrix = dict()
    for doc_name, doc_tf_matrix in tf_matrix.items():
      idf_matrix[doc_name] = pd.DataFrame.from_dict(doc_tf_matrix, orient='index')
      
    idf_matrix = pd.concat(idf_matrix, axis=1).fillna(0.0)
    idf_matrix['idf']= 0.0

    N = len(list_of_docs)
    for token in idf_matrix.index:
      cnt = 0
      for doc_name in list_of_docs:
        if idf_matrix.loc()[token][doc_name]['sum'] != 0:
          cnt = cnt + 1
      idf_matrix['idf'][token] = math.log(N/cnt)

    return idf_matrix

  def tf_idf_matrix():
    sum_and_tf()
    build_tf_matrix()

    tf_matrix = {**tf_matrix, **build_tf_matrix(path_of_docs, list_of_docs_new)}
    list_of_docs = list_of_docs + list_of_docs_new

    build_idf_matrix()
    for :
      

    
    return tf_idf_matrix

class TextCleaning():
  """
  Return a cleaned text data from raw text data.



  Paramenters
  -----------
  documents : Strings
    Raw text data given by user to be cleaned.
  
  remove_stopwords : bool, default True.
    In NLP, stopwords are actually the most common words in any language (like articles, prepositions,
    pronouns, conjunctions, etc) and does not add much information to the text. By activating this option,
    stopwords will be removed. This will help to decrease the noisy in a raw text.

  Examples
  --------
  Get tf-idf from given documents.

  >>>

  """

  def __init__(
      self,
      documents,
      remove_stopwords = True
  ):

    self.documents = documents
    self.remove_stopwords = remove_stopwords

  def sentence_tokenize(
      sentence,
      self.remove_stopwords
  ):
    # words = re.split(r"sentence|(?\s.)",sentence)
    words = re.split('\s|\.|,',sentence)
    tokens = words
    
    if remove_stopwords == True:
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
