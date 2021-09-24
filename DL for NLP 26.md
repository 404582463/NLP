 # DL for Coreference Resolution
 
 ##  Winograd Schema Challenge
 A test similar to Turing Test  
 
 ## MENTION
 If two mention corefer the same entity, They are the referring the same thing.
  
 ## Main tasks in Coreference Resolution
 ![image](https://user-images.githubusercontent.com/48316842/134625099-25a2c451-1841-49b4-8aa2-c3b7c35cc2d2.png)
 
 ### Find all mentions
 Use a binary classifier to judge if the given token sequence is a mention or not.
 All N(N-1) possible spans will be judged by the classifier.

### Group mentions into clusters
Another binary classifier is applied to judge if two mentions are in the same class or not.  

### Build a end-to-end model (binary classifier)
Output is yes if:
- Both inputs are mentions
- They refer to the same entity!
[image](https://user-images.githubusercontent.com/48316842/134632889-845b5b7c-c6d2-45b4-b3a0-b28249316f15.png)

### Span feature extraction
1. start token
2. end token
3. attention (weighted sum): a extra model for determining the weight of each token is needed  
**Cost for training such a model is O(n^4)**, n is the number of tokens.  
To solve this problem, use mention dectector to filiter out those non-mentions can reduce the caculation cost.  
Another method is to give a span length constraint.  
Find out the K mention candidates, then the cost is reduced to O(K^4).  

### Advanced Tipics (unsolved yet)
- Global information:lack of global information may results in contradiction
- How to do this with unspervided method: someone is doing this by predicting masked token with bert
