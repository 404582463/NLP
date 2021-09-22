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

Some common tags in NLP tasks: [SEP] <EOS>  
#### method 1 
 Use a fixed pre-trained model as a feature extractor, then feed extracted features to the taxk-specific model to fine-rune (only task-specific part is trained).  
#### method 2  
 Joint pre-trained model with task-specific model to get a gigantic one. Fine-tune it and then use it for down-stream tasks.  
 Parameters in pre-trained model are not randomly initialized (whereas parameters in task-specific model are), so overfitting is reduced.  
Generally, method 2 performs better than method 1.
 
### How to fine-tune gigantic model
#### Adaptor
We don't need to train every parameter in a model. Use extra Apt layer to limit which part to train.
Similarly, when saving the model, we just need to save the unmodified part of the original model and those Apt layers(may be multiple for different tasks).

#### Weighted features
 Give weight to the output from each layer, then get the weighted sum.
 The weight could be treated as parameter of task-specific model and they will be trained in the same time.
 
#### Why do we fine-tune
modle train by fine-tune method usually has lower training loss rate than train the whole model. In another word, time is saved.
 
![image](https://user-images.githubusercontent.com/48316842/134266997-7857653f-f85e-46de-8f08-d6448bead141.png)
the graph in right side is easier to generalize (the gradient of the area around the local minimum(end point) is more gentle for the right side. Generally, a basin is better than a valley)  
 
 
