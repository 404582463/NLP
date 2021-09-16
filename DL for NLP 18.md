# [DLHLP 2020] Deep Learning for Human Language Processing (18/32)
Youtube channel for [DLHLP 2020] Deep Learning for Human Language Processing: [Here](https://www.youtube.com/watch?v=1_gRK9EIQpc&list=PLJV_el3uVTsO07RpBYFsXg-bN5Lu0nhdG&index=18)  
Slides can be obtained [Here](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbkhYcENGYmlNTDQ1cVlPSlpPZjdsdTZVYkxzZ3xBQ3Jtc0ttMlFOdy1udGozOE42TkN5cFpFLTM5TlBRckljSFlFUEZnazJvdkNVUy1OYVlYbG1DU0E2U2FrWjBHdVZBTHo4RlZPRGFaRVhkM3pjOHJUNWdseG11TF9IWUFsZWlvSEhYdG5hZktlSG00SEwxOWc2WQ&q=http%3A%2F%2Fspeech.ee.ntu.edu.tw%2F%7Etlkagk%2Fcourses%2FDLHLP20%2FBERT%2520train%2520%28v8%29.pdf)  

## Pre-train model
Each token hase a corresponding embedding vector  
**Word2vec, Glove**  
English word as token(each character is a token)  
**FastText**
For Chinese characters, the input could be a image of a character, and use a CNN to process it  

### Contextualized Word Embedding
Different from traditional models that get embedding for each token directly, Elmo, BERT caculate embedding after the whole sentence is given as an input(based on context)  
These kind of models are often very deep. Common architechtures are LSTM(Elmo), Self-attention layers(BERT) and Tree-based model().  
BERT model give different embedding for same word with different context:
![image](https://user-images.githubusercontent.com/48316842/133558001-fa63485a-bc9b-40a6-8476-7aa49e91e15f.png)

### BERT variants that are easy to train
Distill BERT; Tiny BERT; Moble BERT; Q8BERT; ALBERT  

#### How to make model smaller
Network compression: Network Pruning; Knowledge Distillation; Parameter Quantization; Architecture Design  
[Reference](http://mitchgordon.me/machine/learning/2019/11/18/all-the-ways-to-compress-BERT.html)
**Network Architecture**:   
Transformer-XL for long seqence (such as a book)  
Reformer and Longformer to reduce the complexity of self-attention

## Fine-tune