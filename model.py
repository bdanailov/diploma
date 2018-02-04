#!/usr/bin/python

from math import exp
def Logistic (x) : 
    return (1/(1+exp(-x))) 

from math import tanh

def Competitive (x0, x1, x2) :
    inputs = [x0, x1, x2]
    competitive = [0 for i in range(3)]
    maximal_index = inputs.index(max(inputs))
    competitive[maximal_index] = 1
    return competitive

def expression (leftSensor, middleSensor, rightSensor) : 

    scaled_leftSensor=2*(leftSensor-15)/(97-15)-1
    scaled_middleSensor=2*(middleSensor-15)/(99-15)-1
    scaled_rightSensor=2*(rightSensor-15)/(100-15)-1
    y_1_1=tanh(-2.58653
    -0.821485*scaled_leftSensor
    -4.44383*scaled_middleSensor
    +1.77469*scaled_rightSensor)
    y_1_2=tanh(-0.102155
    +2.42519*scaled_leftSensor
    +0.247888*scaled_middleSensor
    -2.7778*scaled_rightSensor)
    y_1_3=tanh(2.49503
    +0.641001*scaled_leftSensor
    -0.185343*scaled_middleSensor
    +4.23045*scaled_rightSensor)
    y_1_4=tanh(-0.664989
    +1.89917*scaled_leftSensor
    -0.437722*scaled_middleSensor
    -2.75387*scaled_rightSensor)
    y_1_5=tanh(-3.56383
    -4.75629*scaled_leftSensor
    +0.19515*scaled_middleSensor
    +0.67261*scaled_rightSensor)
    y_2_1=Logistic(1.69033
    +4.00578*y_1_1
    -0.802717*y_1_2
    -0.840404*y_1_3
    -1.87241*y_1_4
    +4.63682*y_1_5)
    y_2_2=Logistic(-0.656675
    +4.09741*y_1_1
    +3.27937*y_1_2
    -3.55432*y_1_3
    +1.86753*y_1_4
    -0.498308*y_1_5)
    non_probabilistic_left=Logistic(-3.39828
    -2.6465*y_2_1
    +7.38589*y_2_2)
    non_probabilistic_forward=Logistic(3.82746
    -8.22819*y_2_1
    -8.01118*y_2_2)
    non_probabilistic_right=Logistic(-3.63228
    +8.11129*y_2_1
    -6.94174*y_2_2)
    (left,forward,right) = Competitive(non_probabilistic_left,non_probabilistic_forward,non_probabilistic_right)
    
    return left, forward, right 
