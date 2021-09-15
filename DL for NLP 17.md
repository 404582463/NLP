# [DLHLP 2020] Deep Learning for Human Language Processing (17/32)
Youtube channel for [DLHLP 2020] Deep Learning for Human Language Processing: [Here](https://www.youtube.com/watch?v=tFBrqPPxWzE&list=PLJV_el3uVTsO07RpBYFsXg-bN5Lu0nhdG&index=17)  
Slides can be obtained [Here](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqazZOVnBkZkdCUTkxSFdha0dTaVdmLThZbUlhZ3xBQ3Jtc0tuMGFoVkVVZlBpakJYSnZWaTl2ZS1OSTZwQnVkN2Iza2lyY0Q0UXRyb1FuTmh3ZktPWFBKOVZITndjd1lNQ1ZSMkdRTkF0ZEM3dDEwWkl6bUNGRlZkY284RUdZdnVNSDRnYll1bHNTeFhQbmR1SGhEQQ&q=http%3A%2F%2Fspeech.ee.ntu.edu.tw%2F%7Etlkagk%2Fcourses%2FDLHLP20%2FTaskShort%2520%28v9%29.pdf)  

## Category
input -> token  output -> one class  
input -> token  output -> classes for each token  
input -> text  output -> text  (encoder->decoder + attention)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;copy mechanism is expected sometimes  
&nbsp;  
case: multiple sequences as input
![image](https://user-images.githubusercontent.com/48316842/133383897-9840356a-2e17-4ff8-89c4-52894fcd5556.png)
two ways to solve that problem:  
simply concatenate them as one input(a more popular method)  
add attention to each sequence and use a integrate model to deal with them  
&nbsp;  
![image](https://user-images.githubusercontent.com/48316842/133384181-5f9ae4ab-3ab2-4843-a464-80691141a976.png)

## Preprocessing
### POS(part-of-speech) Tagging
preprocessing for down-stream task  
Recently, powerful model like BERT has the ability of POS tagging to some extent. So this preprocessing is not always necessary.  

### Word Segmentation
for Chinese: binary classification to detemine if the character is the boundry or not  
Similarily, model like BERT may have learned how to conduct word segmetation, so it is not necessary.

