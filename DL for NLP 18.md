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
![image](https://user-images.githubusercontent.com/48316842/133560128-295366cf-441e-40ae-bf2f-2ba6149a53b8.png)
 review of NLP tasks:
 Input: one sentence; multiple sentences
 Output: one class; class for each token; copy from input; general sequence

### How to deal with input (multiple sentences)

### How to deal with outptu(one class; class for each token; copy from input; general sequence)


#### General sequence
Use a pre-train model as decoder. What we need to do is to design a task specific model as decoder. However, usually we don't have too much labeled data. Meanwhile, the decoder do not have the pretrainned knowledge. (Version 1.0)  
Use the input sentense to generate a embedding. Then feed this embedding to the task specific model and get a new embedding (generated word). This generated embedding (word) will be the new input for the specific model to get the next embedding. In this case, the pretrained model is also used as a decoder.

### How to fine-tune

some tags: [SEP] <EOS>
#### method 1 
 use a fixed pre-trained model as a feature extractor, then feed extracted features to the taxk-specific model to fine-rune (only task-specific part is trained).  
#### method 2  
 joint pre-trained model with task-specific model to get a gigantic one. Fine-tune it and then use it for down-stream tasks.  
 parameters in pre-trained model are not randomly initialized (whereas parameters in task-specific model are), so overfitting is reduced.  
generally, method 2 performs better than method 1.
 
### How to fine-tune gigantic model
