#!/usr/bin/python

from math import exp
def Logistic (x) : 
    return (1/(1+exp(-x))) 

from math import exp
def Softmax (x0, x1, x2) :
    inputs = [x0, x1, x2]
    softmax = [0 for i in range(3)]
    sum = 0
    for i in range(3) :
        sum += exp(inputs[i])
    for i in range(3) :
        softmax[i] = exp(inputs[i])/sum
    return softmax

def expression (leftSensor, middleSensor, rightSensor) : 

    scaled_leftSensor=2*(leftSensor-15)/(100-15)-1
    scaled_middleSensor=2*(middleSensor-15)/(100-15)-1
    scaled_rightSensor=2*(rightSensor-15)/(100-15)-1
    y_1_1=Logistic(0.80834
    -0.617777*scaled_leftSensor
    -0.210957*scaled_middleSensor
    +0.412133*scaled_rightSensor)
    y_1_2=Logistic(0.737848
    +0.0947942*scaled_leftSensor
    +0.477919*scaled_middleSensor
    +0.864969*scaled_rightSensor)
    y_1_3=Logistic(-0.533762
    +0.853152*scaled_leftSensor
    +0.102886*scaled_middleSensor
    +0.86684*scaled_rightSensor)
    y_1_4=Logistic(-0.0111862
    +0.105137*scaled_leftSensor
    +0.878258*scaled_middleSensor
    +0.599291*scaled_rightSensor)
    y_1_5=Logistic(0.628277
    +0.188995*scaled_leftSensor
    +0.314402*scaled_middleSensor
    +0.9906*scaled_rightSensor)
    y_1_6=Logistic(0.871703
    -0.350917*scaled_leftSensor
    +0.748619*scaled_middleSensor
    +0.178313*scaled_rightSensor)
    y_1_7=Logistic(0.275542
    +0.518647*scaled_leftSensor
    +0.550843*scaled_middleSensor
    +0.58982*scaled_rightSensor)
    y_1_8=Logistic(-0.474431
    +0.208758*scaled_leftSensor
    -0.0588716*scaled_middleSensor
    -0.666091*scaled_rightSensor)
    y_1_9=Logistic(0.590981
    +0.730171*scaled_leftSensor
    +0.746043*scaled_middleSensor
    +0.328829*scaled_rightSensor)
    y_1_10=Logistic(-0.175035
    +0.223961*scaled_leftSensor
    +0.193798*scaled_middleSensor
    +0.291203*scaled_rightSensor)
    non_probabilistic_left=Logistic(0.077113
    -0.703316*y_1_1
    +0.158043*y_1_2
    -0.934073*y_1_3
    +0.401821*y_1_4
    +0.0363013*y_1_5
    +0.665218*y_1_6
    +0.0300982*y_1_7
    -0.774704*y_1_8
    -0.02038*y_1_9
    +0.0206981*y_1_10)
    non_probabilistic_forward=Logistic(-0.903001
    +0.628703*y_1_1
    -0.230683*y_1_2
    +0.275313*y_1_3
    -0.0957552*y_1_4
    -0.712036*y_1_5
    -0.173844*y_1_6
    -0.505935*y_1_7
    -0.186467*y_1_8
    -0.965087*y_1_9
    +0.435193*y_1_10)
    non_probabilistic_right=Logistic(0.147442
    +0.625894*y_1_1
    +0.165365*y_1_2
    -0.106515*y_1_3
    -0.0452772*y_1_4
    +0.99033*y_1_5
    -0.882554*y_1_6
    -0.851479*y_1_7
    +0.281533*y_1_8
    +0.19456*y_1_9
    -0.554795*y_1_10)
    (left,forward,right) = Softmax(non_probabilistic_left,non_probabilistic_forward,non_probabilistic_right)
    
    return left, forward, right 
