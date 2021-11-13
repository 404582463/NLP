class CosineSimilarity():
  """
  Return a the similarity of two vectors by calculating the cosine.

  Paramenters
  -----------
  vector_a, vector_b : numeric array.
    The two vectors to be measured.

  Examples
  --------
  Get cosine similarity of two vectors.

  >>> a = [1,2]
  >>> b = [3,4]
  >>> CosineSimilarity(a,b).cosine_similarity()
  0.9838699100999074
  """

  def __init__(
    self,
    vector_a,
    vector_b
    ):
    self.vector_a = vector_a
    self.vector_b = vector_b

  def dot(self, x, y):
    """Dot product as sum of list comprehension doing element-wise multiplication"""
    return sum(x_i*y_i for x_i, y_i in zip(x, y))

  def vector_length(self, x):
    """Euclidean distance between initial point and terminal point of a vector"""
    return math.sqrt(sum(x_i**2 for x_i in x))
  
  def cosine_similarity(self):
    dot_product = self.dot(self.vector_a, self.vector_b)
    vector_a_ed = self.vector_length(self.vector_a)
    vector_b_ed = self.vector_length(self.vector_b)
    cosine_similarity = dot_product/(vector_a_ed * vector_b_ed)

    return cosine_similarity
