<h1>Tennis Match Outcome Prediction:

  The US Open Men's Singles 2013 Match Statistics Analysis</h1>

<h2>Description</h2>
The project involves implementing a predictive model for Tennis US Open Men's Singles 2013 match outcomes based on player statistics. The focus is on key metrics such as 1st Serve Percentage, 1st Serve Won, Break Points Won, Number of Double Faults, and Number of Unforced Errors. Three classification models were built for forecasting: Logistic Regression, K-Nearest Neighbors, and Random Forest.
<br />

<h2>Programs Used </h2>

- <b>Python</b>

<h2>Project walk-through</h2>

<p align="center">
Background: <br />
  
According to Jeffrey Ruth's article, "The Five Most Important Statistics in Men's Tennis," he discusses that First-serve percentage and Break Points converted are two cruicial factors in Men's Tennis statistics.
I decided to look into five important statistics that may predict the match outcome by adding First Serve Won, Double Faults committed, and Unforced Errors committed.<br/>

<br />
<br />
<p align="center">
Problem Statement:  <br/>

Develop predictive models to predict the tennis match outcome based on player’s:
- 1st Serve %
- 1st Serve Won
- Break points won
- Number of Double Faults
- Number of Unforced Errors
<br />
Built 3 classification models for forecasting methods: <br/>

- Logistic Regression: A statistical method used for modeling the probability of a binary outcome by fitting a logistic curve to the data.
- K-Nearest Neighbors: A simple, non-parametric method used for classification and regression by identifying the classification of a data point based on the majority of its k-nearest neighboring data points.
- Random Forest: An ensemble method that constructs multiple decision trees during training and outputs the mode of the classes (classification) or the average prediction (regression) of the individual trees.

<br />
<br />
<p align="center">
Data Exploration:  <br/>

(1) Variables used:
- FSP - First Serve %
- FSW - First Serve Won
- ACE - Ace
- DBF - Double Faults
- BPC - Break Points Created
- BPW - Break Points Won

(2) Data Cleaning:
- Separate player 1 and player 2
<img src="https://imgur.com/I6Tshug.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>

- Create a new column named ‘outcome’:
Winner = 1, Loser = 0
<img src="https://imgur.com/I6Tshug.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>

(3) Train and Test Datasets:
- 80% training data
- 20% testing data
Correlation:
Identify correlations between each variable and see how one another affect the outcome

<p align="center">
Code Used:  <br/>


<p align="center">
Results:  <br/>

<p align="center">
Conclusion:  <br/>

(1) Comparing Models:
Based on the results, the Logistic Regression model outperformed the K-Nearest Neighbor and the Random Forest models. 

(2) Match outcome prediction from Logistic Regression Model (Variable Odds Ratio):
- Each additional first serve percentage point increase, +14% odds of winning
- Each additional ace a player hits, +6.7% odds of winning
- Each additional break point created by a player, +87% odds of winning
- Each additional total point win by a player, +7% odds of winning
<img src="https://imgur.com/I6Tshug.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
</p>

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
