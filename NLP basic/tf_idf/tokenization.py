import re
# import stopwords

class Tokenization():
  """
  Return a list of tokens by tokenizing a raw text data.

  Paramenters
  -----------
  documents : Strings
    Raw text data given by user to be cleaned.
  
  remove_stopwords : bool, default True.
    In NLP, stopwords are actually the most common words in any language (like articles, prepositions,
    pronouns, conjunctions, etc) and does not add much information to the text. By activating this option,
    stopwords will be removed. This will help to decrease the noisy in a raw text.
  
  case_sensetive : bool, default False.
    This argument is assigned as True only when case sensetivity is considered necessary.
    For most case, same words with different case are treated as the same tokens.

  Examples
  --------
  Get tokens from given document with considering case sensetivity.

  >>> doc = "This is a test sentence"
  >>> Tokenization(doc, case_sensetive=True).tokenize()
  ['This', 'test', 'sentence']

  """

  def __init__(
      self,
      documents,
      remove_stopwords = True,
      case_sensetive = False
  ):
    self.documents = documents
    self.remove_stopwords = remove_stopwords
    self.case_sensetive = case_sensetive

  def normalize(self):
    normalized_documents = self.documents.lower()
    return normalized_documents

  def split(
        self,
        normalized_documents,
    ):
    words = re.split('\s|\.|,',normalized_documents)
    tokens = words
    return tokens
      

  def tokenize(self):
    if self.case_sensetive == False:
      normalized_documents = self.normalize()
    else:
      normalized_documents = self.documents
    
    tokens = self.split(normalized_documents)
    
    if self.remove_stopwords == True:
      tokens = list(i for i in tokens if i not in stopwords)

    # for l in range(len(words)):    
    #   while re.match(r"^(?:,|\.|\'|'|\"|_|`|@|&|!|“|”|=|-|\+|\t|\s|\(|\)|\[|\]|\{|\}|<|>|;|:).*", words[l]):
    #     words[l] = words[l][1:]
    #   while re.match(r".*(?:,|\.|\'|'|\"|_|`|@|&|!|“|”|=|-|\+|\t|\s|\(|\)|\[|\]|\{|\}|<|>|;|:)$", words[l]):
    #     words[l] = words[l][:-1]
    #   words[l] = ss.stem(words[l])
    #   if not re.match(r"^(?:[0-9]|\$|£|€|-|–|—).*", words[l]) and words[l] != '' and words[l] not in stopword:
    #     token.append(words[l])
    return tokens
