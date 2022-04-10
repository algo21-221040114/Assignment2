# Assignment2

## Introduction

This assignment refer to a paper, 'Stock Price Prediction Using Support Vector Machine Approach',
published by International Academic Conference on Management and Economics.
You can access to the paper through https://www.dpublication.com/wp-content/uploads/2019/11/24-ME.pdf.
The main proposal is to predict the up or down direction of stock prices in different holding periods, with SVM.
All research result is based on the data of APPLE and SP500, you can adjust parameters according to different stocks.

## Environment

Pycharm (Professional Edition)
Python 3.7

## Requirements

Numpy
Pandas
Sklearn

## Model Elaboration

Compared with the traditional model only using the single stock data to predict (detailed in SVM_1.py), 
combining the index data into SVM model can enhance the prediction accuracy from around 50% to around 65%.

Radial Basis Function performs better than linear separation in this prediction mission. 
And the punishment part C is slightly be decreased to 0.8, in order to make this model more general.

In terms of different prediction intervals (M) and how much previous data should utilize (N1, N2), several tests have been conducted.
It is found that this model always perform better in relative shorter periods, like 5-days, 10-days or 20-days.
And when the length of previous data used is similar to the prediction interval, the model performs better.
The best prediction result is using 20-days previous price data to predict the up or down in the next 20 days.
The accuracy in training set is about 68%, in test set is about 67%. 

## Back Test

Back testing is conducted with the optimal parameters mentioned above.
The back_test rule is to trade every 20 days.
Every 20 days, the system will automatically close last position with current close price, 
and conduct the signal the next day.
When the signal is 1, the system will buy with the next day close price, 
since current close price also is used as input data for prediction.
When the signal is -1, the system will sell with the next day close price.

The back_test period is from 2015.01 to 2020.12. The annualized return is about 33%, 
Sharpe ratio is 1.03, the max draw down is 25.97%.