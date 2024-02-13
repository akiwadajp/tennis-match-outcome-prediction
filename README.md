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
I decided to look into five important statistics that may predict the match outcome. On top of these two variables, I decided to add First Serve Won, Double Faults committed, and Unforced Errors committed.

Dataset from https://archive.ics.uci.edu/dataset/300/tennis+major+tournament+match+statistics<br/>

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

(1) Variables:
- FSP - First Serve %
- FSW - First Serve Won
- ACE - Ace
- DBF - Double Faults
- BPC - Break Points Created
- BPW - Break Points Won

(2) Data Cleaning:
- Separate player 1 and player 2
<img src="https://i.imgur.com/jYrHeAI.png">

- Create a new column named ‘outcome’:
Winner = 1, Loser = 0
<img src="https://i.imgur.com/GeJojWM.png">

(3) Train and Test Datasets:
- 80% training data
- 20% testing data
Correlation:
Identify correlations between each variable and see how one another affect the outcome
<br/>
<br/>
<br/>
<p align="center">
Code Used:  <br/>
<br/>
(1) Logistic Regression:
<br/>
<br/>
<img src="https://i.imgur.com/nNTBM2d.png">
<img src="https://i.imgur.com/HYRFeIV.png">


Firstly, imported Logistic Regression to trained the model,
lm.fit(X_train, y_train)
The model is trained on the training set (X_train and y_train) using the fit method. This step involves adjusting the model's parameters to minimize the difference between predicted and actual outcomes.
Made predictions using
y_pred_lm = lm.predict(X_test)
The trained model is used to make predictions on the test set (X_test). The predicted values are stored in the y_pred_lm variable.
Then, evaluated Model Performance,
score_test_lm = lm.score(X_test, y_test)
score_train_lm = lm.score(X_train, y_train)
The score method is used to calculate the accuracy of the model on both the training and test sets. Accuracy is a common metric that measures the proportion of correctly classified instances.

Addtion to the test and train accuracy scores, added Confusion Matrix and Additional Metrics to gather more information about the model.
cm_lm = confusion_matrix(y_test, y_pred_lm)
precision_lm = precision_score(y_test, y_pred_lm, average='macro')
recall_lm = recall_score(y_test, y_pred_lm, average='macro')
accuracy_lm = accuracy_score(y_test, y_pred_lm)
The confusion matrix is calculated using the confusion_matrix function, and precision, recall, and accuracy are computed using their respective functions from scikit-learn. These metrics provide more detailed insights into the model's performance, especially in multi-class classification problems.

<img src="https://i.imgur.com/4t5ZMYK.png">
This code plots an ROC curve for a logistic regression model, assessing its ability to distinguish between positive and negative classes. The closer the ROC curve is to the top-left corner, the better the model performance. A curve that nearly touches the top-left corner indicates a model with high sensitivity (true positive rate) and low false positive rate, approaching an ideal or perfect classification.

<br/>
<br/>
(2) K-Nearest Neighbors Classifier
<br/>
<br/>
(3) Random Forest Classifier


<br/>
<br/>
<br/>
<br/>

<p align="center">
Results:  <br/>

<p align="center">
Conclusion:  <br/>

(1) Comparing Models:
Based on the results, the Logistic Regression model outperformed the K-Nearest Neighbor and the Random Forest models. 

<img src="https://i.imgur.com/a5lt4vg.png">

<img src="https://i.imgur.com/FdDowj8.png">

<br />

(2) Match outcome prediction:
Used the Logistic Regression Models to produce variable odd ratio:
<img src="https://i.imgur.com/jpru5nI.png">

- Each additional first serve percentage point increase, +14% odds of winning
- Each additional ace a player hits, +6.7% odds of winning
- Each additional break point created by a player, +87% odds of winning
- Each additional total point win by a player, +7% odds of winning
<img src="https://i.imgur.com/L93RJkQ.png">
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
