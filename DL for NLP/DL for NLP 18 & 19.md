# [DLHLP 2020] Deep Learning for Human Language Processing (18/32)
Youtube channel for [DLHLP 2020] Deep Learning for Human Language Processing: [Here for 18](https://www.youtube.com/watch?v=1_gRK9EIQpc&list=PLJV_el3uVTsO07RpBYFsXg-bN5Lu0nhdG&index=18)&nbsp;and&nbsp;
[Here for 19](https://www.youtube.com/watch?v=Bywo7m6ySlk&list=PLJV_el3uVTsO07RpBYFsXg-bN5Lu0nhdG&index=19)  
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

Some common tags in NLP tasks: "SEP" "EOS" "CLS"
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
 
### contextualize embedding -- Context Vector(CoVe)
Method: Translation (not unsupervised method)
![image](https://user-images.githubusercontent.com/48316842/134268414-90549cea-6a1b-4e87-9808-c47f387319d2.png)
Assign attention to the output of enconder, then give it to the decoder.  
Large amount of sentence pairs are needed for training. This is the limitation.  
To deal with the problem, self-supervised(unsupervised) learning is being used in recent years.
 
#### Explaination of self-supervised learning
The system learns to predict part of its input from other parts of its input.
![image](https://user-images.githubusercontent.com/48316842/134269552-2a630d65-77c6-4767-ab8f-e51e4842f27f.png)
 
#### How to achieve self-supervised learning in NLP
Use a token to predict the next one.
![image](https://user-images.githubusercontent.com/48316842/134270015-9a363440-c247-4f4a-85c8-b9f1fcac531c.png)
Some models at an early stage use LSTM as the basic such as ELMO and ULMFiT(Universal Language Model Fine-tuning).  
Nowadays, people use a self-attention model instead of LSTM. (GPT series, Megatron, Turing NLG)  
Be careful about the area that attention mechanism covers, only part of the positions are accessible actually (position of and before present token). 

#### model of ELMO
![image](https://user-images.githubusercontent.com/48316842/134271841-f3c5fcec-949e-4ecd-8d9e-b9d3d475c2f7.png)
The left part of the model and the right part of the model are independent to each other, and has no effect to the prediction by the opposite side.  

### BERT
BERT can solve this limitation by using a mask token. However, no limitation on the area of self-attention.
CBOW (model of about 10 years ago) use a similar mechanism as BERT.

#### Masking input
**Whole word masking**  
mainly for English because a word consists of multiple tokens.
**Phrase-level & entity-level**  
Enhanced representation through knowledge integration(ERNIE)
**SpanBert**
Randomly mask a sequence of tokens.  
SBO(span boundary objective) is a training method introduced in SpanBert.  
![image](https://user-images.githubusercontent.com/48316842/134287629-04acfcc7-bc3b-405e-951b-59f867f8a1a4.png)
**XLNet**
Transformer-XL is used  
The order of tokens is randomly intialized for prediction, but only left side could be seen (language model view)  
Only part of the whole tokens could be applied for prediction (BERT view)
#### BERT and generation tasks
LM is born for predict the next token, but BERT is not (for predict masked token & tokens besides the masked token can be seen)  
People say BERT is not good at generation tasks. Actually, this is true for autoregressive model (generate from left side to right side) but for non-autoregressive models there is no such limitation.  
Anyhow, usually people do not use a BERT as a pre-train model for seq2seq model in generaion tasks.  
BERT could be used as a encoder but not a decoder because that part is no pre-trained. 

#### How to train a seq2seq model(BART/MASS/UniLM)
corrupted input is necessary. (MASS and BART give some methods)
![image](https://user-images.githubusercontent.com/48316842/134299360-2059d997-d6e6-46ae-ac9b-1ff0603b538f.png)
UniLM is a model that is an encoder, and meanwhile is a decoder and a seq2seq model.  
(encoder: BERT  decoder: GPT  seq2seq:BART/MASS)  

#### Give up prediction--ELECTRA
This is a binary classifier for prediction yes/no, which is much more easier than reconstruction.  
![image](https://user-images.githubusercontent.com/48316842/134301644-7c1fd086-f997-4ff2-a43d-a86a3d198a71.png)

### Sentence level 
Use a representation embedding for the whole sequence instead of a series of representations for each token.  
Two ways to get a sentence embedding: **skip thought** and **quick thought**
![image](https://user-images.githubusercontent.com/48316842/134304291-3e7c4414-6237-47d0-b3fd-784eae1fbda0.png)
NSP(next sentence prediction) is not useful. Maybe the agent could not learn much useful info from training.  
SOP(sentence order prediction) is used in ALBERT and structBERT(Alice)

### T5 -- servy of pre-train methods
Paper: [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/pdf/1910.10683)

### External Knowledge 
ERNIE(enhanced language representation with informative entities)
