# Example: Name of file start.py
from tfidf import *
doc_list = []
path = ''
get_docs()

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

def yield_demo_documents():
  yield
  delete


tf_idf = Tfidf(doc_list = xx, path = xx).tf_idf_matrix()
