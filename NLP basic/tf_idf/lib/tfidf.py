import pandas as pd
import math

class Tfidf():
  """
  Get a dataframe of tf-idf from given documents.

  Paramenters
  -----------
  tokens : a list of strings.
    This is the tokenized documents.

  remove_low_frequency : Bool, default False.
    Remove tokens with low frequency or not.
    Low frequency words are considered as importand in tf-idf method.
    But for some words with low frequency, for example, only apper once in documents, 
    the importance may be considered higer than it should be and cause estimation error.
    It depends on use to determine activate this option or not.
  
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
      document_dictionary,
      remove_low_frequency = False,
      low_term_frequency = 1
  ):
    self.document_dictionary = document_dictionary
    self.remove_low_frequency = remove_low_frequency
    self.low_term_frequency = low_term_frequency

    matrix = {}
  
  def sum_and_tf(
      self,
      tokens, 
      remove_low_frequency=False, 
      low_frequency=1
    ):
    """ Calculate the sum and normalized term frequency of each token from a given documents. """
      
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

  def build_tf_matrix(self):
    """
    Calculate the term sum and term frequency in a document,
    and return a dictionary contains these information
    """

    # get documents for build the tf matrix
    document_dictionary = self.document_dictionary
    tf_matrix = {}

    for doc_name, doc_content in document_dictionary.items():
      tokens = doc_content
      tf_matrix[doc_name] = self.sum_and_tf(tokens)

    return tf_matrix

  def build_idf_matrix(self):
    idf_matrix = dict()
    tf_matrix = self.build_tf_matrix()
 
    for doc_name, doc_tf_matrix in tf_matrix.items():
      idf_matrix[doc_name] = doc_tf_matrix
      
    idf_matrix = pd.concat(idf_matrix, axis=1).fillna(0.0)
    idf_matrix['idf'] = 0.0
    idf_matrix['sum'] = 0

    N = len(self.document_dictionary)

    for token in idf_matrix.index:
      cnt = 0
      sum = 0
      for doc_name in self.document_dictionary:
        if idf_matrix.loc()[token][doc_name]['sum'] != 0:
          sum = sum + idf_matrix.loc()[token][doc_name]['sum']
          cnt = cnt + 1
    
      idf_matrix.at[token, 'sum'] = sum
      
      # the denominator is set as (cnt+1) but not cnt to avoid being 0
      # this is because for a new query, there may be words/tokens are new to the exist words/tokens dictionary
      # then the cnt will be 0, and error occurs when calculating log(N/cnt) 
      # this is a common method for solving such kind of issues
      idf_matrix.at[token, 'idf'] = math.log(N/cnt)

    return idf_matrix

  def prune_matrix(self, tf_idf_matrix):
    tf_idf_matrix = tf_idf_matrix
    tf_idf_matrix = tf_idf_matrix[tf_idf_matrix['sum']>self.low_term_frequency]
    return tf_idf_matrix

  def tf_idf_matrix(self):
    tf_idf_matrix = self.build_idf_matrix()
    for token in tf_idf_matrix.index:
      for doc_name in self.document_dictionary:
        tf_idf_matrix.at[token,(doc_name,'tf_idf')] = tf_idf_matrix.loc()[token][doc_name]['tf'] * tf_idf_matrix['idf'][token]

    if self.remove_low_frequency == True:
      tf_idf_matrix = self.prune_matrix(tf_idf_matrix)

    return tf_idf_matrix
