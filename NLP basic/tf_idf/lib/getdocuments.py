from os import listdir

list_of_docs = []
path_of_docs = ''
document_dictionary = {}
demo_documents = ["d1.txt", "d2.txt", "d3.txt", "d4.txt", "d5.txt"]


def get_docs():
  list_of_docs = []
  print("Please give the DOCUMENTS you want to ANALYZE: \n")
  print("Please input 'own' if you want to use your own documents\n")
  print("Please input 'demo' to use demo documents\n")
  instruction = input()
  if instruction == 'demo':
    list_of_docs = demo_documents
    path = './demo'
    print("Input documents are: ",list_of_docs,'\n')
    return path_of_docs, list_of_docs
  elif instruction == 'own': 
    print("Please input the path of the folder where documents are in\n")
    print("NOTION: PLEASE BE AWARE THAT ALL DOCUMENTS FOR ANALYZING SHOULD BE PREPARED IN THE SAME FOLDER\n")
    print("For example, you need to input like this: /content/drive/MyDrive/Colab Notebooks\n")
    path_of_docs = input()
    while True:
      print("Please input the file name you want to analyze\n")
      print("For example, you need to input like this: d1.txt\n")
      print("Input 'over' if there is no more documents\n")
      print("You can also input 'all' to get all documents in the given folder\n")
      doc_name = input()
      if doc_name == 'over':
        print("Input documents are: ",list_of_docs)
        return path_of_docs, list_of_docs
      elif doc_name == 'all':
        list_of_docs = listdir(path_of_docs)
      else:
        list_of_docs.append(doc_name)
      
def read_docs():
  for doc in list_of_docs:
    file_path = path_of_docs + '/' + doc
    with open(file_path, "r") as f:
      document_dictionary[doc.split('.')[0]] = f.read()
    return document_dictionary
