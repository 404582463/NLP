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
