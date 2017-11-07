Logistic <- function(x) { 
    1/(1+exp(-x))
}

Competitive <- function(x0, x1, x2) {
    inputs <- c(x0, x1, x2)
    competitive <- array(0, 3)
    maximal_index <- which.max(inputs)
    competitive[maximal_index] <- 1
    competitive
}

expression <- function(leftSensor, middleSensor, rightSensor) {

    scaled_leftSensor<-2*(leftSensor-15)/(99-15)-1
    scaled_middleSensor<-2*(middleSensor-15)/(100-15)-1
    scaled_rightSensor<-2*(rightSensor-15)/(100-15)-1
    principal_component_1<-(-0.568097*scaled_leftSensor-0.38326*scaled_middleSensor-0.72827*scaled_rightSensor)
    principal_component_2<-(-0.490633*scaled_leftSensor+0.868203*scaled_middleSensor-0.0741767*scaled_rightSensor)
    principal_component_3<-(-0.660716*scaled_leftSensor-0.315174*scaled_middleSensor+0.681264*scaled_rightSensor)
    y_1_1<-Logistic(0.225678
    -2.17922*principal_component_1
    -0.420003*principal_component_2
    -1.34683*principal_component_3)
    y_1_2<-Logistic(-1.00165
    -0.824412*principal_component_1
    -1.03951*principal_component_2
    +0.040233*principal_component_3)
    y_1_3<-Logistic(0.0917531
    -0.737465*principal_component_1
    +1.45949*principal_component_2
    +0.659674*principal_component_3)
    y_1_4<-Logistic(0.945305
    -0.997259*principal_component_1
    -0.0237861*principal_component_2
    -0.288011*principal_component_3)
    y_1_5<-Logistic(0.0910642
    -1.27746*principal_component_1
    -0.394568*principal_component_2
    +0.891995*principal_component_3)
    y_1_6<-Logistic(-1.32016
    +1.07384*principal_component_1
    +1.64251*principal_component_2
    -0.838776*principal_component_3)
    y_1_7<-Logistic(0.660819
    +0.158385*principal_component_1
    +0.566139*principal_component_2
    -0.438408*principal_component_3)
    y_1_8<-Logistic(-0.592492
    +0.197014*principal_component_1
    -0.660254*principal_component_2
    -0.760429*principal_component_3)
    y_1_9<-Logistic(0.259619
    +1.05812*principal_component_1
    +0.280889*principal_component_2
    -0.127117*principal_component_3)
    y_1_10<-Logistic(-0.229888
    -0.205174*principal_component_1
    -1.57074*principal_component_2
    -0.00919839*principal_component_3)
    scaled_left<-Logistic(0.052154
    +2.29141*y_1_1
    +0.911288*y_1_2
    -1.20842*y_1_3
    -0.38984*y_1_4
    -0.48245*y_1_5
    -0.475876*y_1_6
    +0.21654*y_1_7
    +0.719741*y_1_8
    +1.43298*y_1_9
    +0.244705*y_1_10)
    scaled_forward<-Logistic(-1.01392
    -0.0908923*y_1_1
    +0.486223*y_1_2
    -1.39093*y_1_3
    +1.28594*y_1_4
    +1.86026*y_1_5
    -0.696549*y_1_6
    +0.256352*y_1_7
    +0.498931*y_1_8
    +0.178832*y_1_9
    +0.27267*y_1_10)
    scaled_right<-Logistic(0.0549042
    -0.532252*y_1_1
    -0.958275*y_1_2
    -0.667797*y_1_3
    +0.0160754*y_1_4
    -0.848434*y_1_5
    -0.32858*y_1_6
    -0.984049*y_1_7
    +1.52949*y_1_8
    +0.364267*y_1_9
    +0.295826*y_1_10)
    outputs <- Competitive(non_probabilistic_left,non_probabilistic_forward,non_probabilistic_right)
    outputs 
} 
