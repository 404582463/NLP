# Text Style Transfer

## Introduction
Image/Audio(voice conversion)/Text style transfer

## Text style Transfer
Generator: transfer the style of text
Discriminator: judge the class of an input
Reconstructor: transfer the rewrite text to the original style
The model is like a cycle GAN, because the training goal is to minimize the reconstruction error

## Problem of the model
![image](https://user-images.githubusercontent.com/48316842/134603751-80c1efc5-4e83-499e-9892-99c09582f21d.png)
gradient ascent can not be used for this model because the part circled by the red rectangular is the sampled result from the previous token.
**not sure**(it is just a series of distribution)

## Solutions
- Gumble-Softmax: Change the sampled part to continous one
- contimuous Input for Discriminator: Skip the sampled part and just feed the continous token to discriminator  
However there are still some SERIOUS problems to be unsolved: 
![image](https://user-images.githubusercontent.com/48316842/134604835-f3f497c0-e1f9-4b6e-b1d4-e58ff62711db.png)
Ground truth (sentence wrote by human) generates a one-hot token.  
Generated output by machine gives a vector of certain continous distribution and can never be one-hot.  
Thus the model could learn nothing and just judge the class of a sentence by it is one-hot or not.  
WGAN methon can help to improve this problem.  
- Reinforecement Learning
Reinforcement is helpful with undifferentiable models.  
Give the role of "agent" in RL to Generator; role of "actions" that are taken in RL to sampled tokens.   
Discriminator is the interactive environment and the output scalar is the final reward.  
The problem is the environment (Discriminator model) will change at the same time which will make the training of RL much more difficult.  
