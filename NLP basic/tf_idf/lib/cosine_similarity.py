class CosineSimilarity():
  def __init__(
    self,
    query,
    document
    ):
    self.query = query
    self.document = document

  def dot(self, x, y):
    """Dot product as sum of list comprehension doing element-wise multiplication"""
    return sum(x_i*y_i for x_i, y_i in zip(x, y))

  def eculidean_distance(self, x):
    return math.sqrt(sum(x_i**2 for x_i in x))
  
  def cosine_similarity(self):
    # query = self.query
    # document = self.document
    dot_product = self.dot(self.query, self.document)
    query_ed = self.eculidean_distance(self.query)
    document_ed = self.eculidean_distance(self.document)
    cosine_similarity = dot_product/(query_ed * document_ed)

    return cosine_similarity
