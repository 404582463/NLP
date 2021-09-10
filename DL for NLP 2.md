# [DLHLP 2020] Deep Learning for Human Language Processing (2/32)
Youtube channel for [DLHLP 2020] Deep Learning for Human Language Processing: [Here](https://www.youtube.com/watch?v=AIKu43goh-8&list=PLJV_el3uVTsO07RpBYFsXg-bN5Lu0nhdG&index=2)  
Slides can be obtained [Here](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbDZ4cmlKYzZScDNPWnJGWWp0R0ZEWnE2dHFwUXxBQ3Jtc0tsQVQwWHRkNTlHS2FvOTdNd0dnMlVsM2pKbnBtZUZuanhCVFJ3d1dSSzVJdTlrdGx0RTlIOXQtdkcyNG1GdnNjN2Joc3BoTm1oZ3RNTHBYUDN0ZVg2cmJoZFExd2NIX0xLLXdoWHhBTENFVFBtUENTYw&q=http%3A%2F%2Fspeech.ee.ntu.edu.tw%2F%7Etlkagk%2Fcourses%2FDLHLP20%2FASR%2520%28v12%29.pdf)  

## Speech Recognition
![image](https://user-images.githubusercontent.com/48316842/132788262-ee2bed1b-7031-4c40-aac0-c6c324eaf321.png)

## Token
**Phoneme**: unit of a sound  (external **lexicon** that record the relation between word and phonemes is **needed**)  
**Grapheme**: smallest unit of a writing system (**lexicon free**)  
(26 alphabet + space + puctuation marks for English)  
(about 4000 common characters for Chinese)  
**Word**: For some language, number of words can be very large, so use word as a token may not be a good method  
**Morpheme**: the smallest meaningful unit  
(e.g., unbreakable -> un + break + able)  
To know the morphemes in a language, refer to linguistic or statistic.  
**Byte**: Any character can be represented by using the UTF-8 code. And this system can be language independent. (V is always 256)
![image](https://user-images.githubusercontent.com/48316842/132790238-a6f3244c-9565-46d9-becd-4172dd631306.png "Partition of the four main methods in three main conference in 2019")  
![image](https://user-images.githubusercontent.com/48316842/132791093-1cc97075-c8fe-4972-8980-88e2ad5e7554.png)
