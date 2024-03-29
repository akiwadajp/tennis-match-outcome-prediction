

# Mount google drive

from google.colab import drive
drive.mount('/content/gdrive/',force_remount=True)
# Right click on the BANA6350>Data folder and copy the folder path by click "Copy Path". Then paste that inside the code below to link your folder where all the data will reside

import os

path = "/content/gdrive/MyDrive"

os.chdir(path)




import pandas as pd
pd.read_csv('USOpen-men-2013.csv').head()

import pandas as pd

# Load your dataset into a pandas DataFrame
tennis_data = pd.read_csv('USOpen-men-2013.csv')

# Select columns related to Player 1
player_1_cols = [col for col in tennis_data.columns if col.endswith('.1') or col == 'Player 1' or col == 'Result']
player_1_data = tennis_data[player_1_cols]

# Rename the columns to remove the '.1' suffix for Player 1
player_1_data.columns = player_1_data.columns.str.replace('.1', '')

# Select columns related to Player 2
player_2_cols = [col for col in tennis_data.columns if col.endswith('.2') or col == 'Player 2' or col == 'Result']
player_2_data = tennis_data[player_2_cols]

# Rename the columns to remove the '.2' suffix for Player 2
player_2_data.columns = player_2_data.columns.str.replace('.2', '')

# Create 'outcome' column for Player 1 data
player_1_data['outcome'] = player_1_data['Result'].apply(lambda x: 1 if x == 1 else 0)

# Create 'outcome' column for Player 2 data
player_2_data['outcome'] = player_2_data['Result'].apply(lambda x: 0 if x == 1 else 1)

# Show combined data with the 'outcome' column
combined_data = pd.concat([player_1_data, player_2_data]).reset_index(drop=True)
print("Combined Data with Outcome Column:")
print(combined_data)

import matplotlib.pyplot as plt

plt.rcParams['lines.linewidth'] = 3
plt.rcParams['figure.figsize'] = [14.0, 6.0]
plt.rcParams['font.size']= 18
plt.style.available   # Check what styles are available for Chart formats by visiting : https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
plt.style.use('fivethirtyeight')       # Assigning the FiveThirtyEight format, you can choose any of the names from the above link

# Commented out IPython magic to ensure Python compatibility.
# if for some reason your sns plots are not visible, run this line of code in Colab

# %matplotlib inline

!pip install prince
!pip install yellowbrick

import math
from pathlib import Path
import pandas as pd
import numpy as np

from scipy import stats
from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
from scipy.stats import multivariate_normal

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import from_levels_and_colors
import seaborn as sns

from statsmodels.stats import power
import prince

import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.metrics import confusion_matrix, precision_score, recall_score, accuracy_score

combined_data.info()

# Load dataset as X and y

X = combined_data[['FSP', 'FSW', 'ACE', 'DBF', 'BPC', 'BPW', 'TPW']]
y = combined_data['outcome']

# We often work with Binary outcomes (Yes/No, Purchased/Not Purchased, PaidOff/Defaulted etc.). Confirm within you y (outcome variable) that you have a binary outcome variable.

# You can convert a non-binary outcome variable using sklearn.preprocessing Binarizer (https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.binarize.html)

y.unique()

#Let's convert the Malignant Tumors (M) = 1, and Benign Tumors , (B) = 0

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y_encoded = le.fit_transform(y)
print(y_encoded)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.3, random_state=0)

sns.pairplot(X_train)

combined_data.boxplot(column=['FSP', 'FSW', 'ACE', 'DBF', 'BPC', 'BPW', 'TPW'], grid=False)

# Mapping outcomes to colors
color_map = {1: 'blue', 0: 'red'}

# Creating a list of colors based on the 'outcome' column
colors = combined_data['outcome'].map(color_map)

# Plotting the scatter plot with specific colors for each outcome
plt.scatter(combined_data['FSW'], combined_data['BPW'], c=colors)

# Add labels and title
plt.xlabel('First Serve Won')
plt.ylabel('Break Points Won')
plt.title('Tennis Match Dataset')

# Show plot
plt.show()

# Create 2D scatterplot : This is a good technique for classification problems, where you will color code the dots based on your classes (here 1, 2, 3)
# and use X and Y axis with two of your variables

plt.scatter(combined_data['FSW'], combined_data['BPW'], c=pd.factorize(combined_data['outcome'])[0])
# Add labels and title
plt.xlabel('First Serve Won')
plt.ylabel('Break Points Won')
plt.title('Tennis Match Dataset')
# Show plot
plt.show()

# Create 2D scatterplot : This is a good technique for classification problems, where you will color code the dots based on your classes (here 1, 2, 3)
# and use X and Y axis with two of your variables

plt.scatter(combined_data['ACE'], combined_data['DBF'], c=pd.factorize(combined_data['outcome'])[0])
# Add labels and title
plt.xlabel('Aces')
plt.ylabel('Double Faults')
plt.title('Tennis Match Dataset')
# Show plot
plt.show()

# Define colors for each outcome class
color_map = {1: 'blue', 0: 'red'}

# Map the 'outcome' column to the defined colors
colors = combined_data['outcome'].map(color_map)

# Plot the scatter plot with colors corresponding to each outcome class
plt.scatter(combined_data['ACE'], combined_data['DBF'], c=colors)

# Add labels and title
plt.xlabel('Aces')
plt.ylabel('Double Faults')
plt.title('Tennis Match Dataset')

# Show plot
plt.show()

# Commented out IPython magic to ensure Python compatibility.
# Create 3D scatterplot : This is a good technique for classification problems, where you will color code the dots based on your classes (here 1, 2, 3)
# and use X and Y axis with two of your variables

#pip install plotly

# %matplotlib inline

import plotly.express as px

# Create 3D scatter plot
fig = px.scatter_3d(combined_data, x='FSP', y='FSW', z='BPW', color='outcome', size_max=14)
# Show plot
fig.show()

##################################################
# Create a logistic regression classifier model : Call it LM
##################################################

LM = LogisticRegression(random_state=0)

# Fit the model on the train set
LM.fit(X_train, y_train)

# Perform prediction on the test set
y_pred = LM.predict(X_test)

# Calculate the accuracy of the model
score_test = LM.score(X_test, y_test)
score_train = LM.score(X_train, y_train)

print("Accuracy Train:", score_train)
print("Accuracy Test:", score_test)
print("Predictions:", y_pred)

# Create a logistic regression classifier object
lm = LogisticRegression(random_state=0)

# Fit the model on the train set
lm.fit(X_train, y_train)

# Perform prediction on the test set
y_pred_lm = lm.predict(X_test)

# Calculate the accuracy of the model
score_test_lm= lm.score(X_test, y_test)
score_train_lm= lm.score(X_train, y_train)

print("Accuracy Train_lm:", score_train_lm)
print("Accuracy Test_lm:", score_test_lm)
print("Predictions_lm:", y_pred_lm)

# Calculate the confusion matrix
cm_lm = confusion_matrix(y_test, y_pred_lm)

# Calculate the precision, recall, and accuracy

precision_lm = precision_score(y_test, y_pred_lm, average='macro')
recall_lm = recall_score(y_test, y_pred_lm, average='macro')
accuracy_lm = accuracy_score(y_test, y_pred_lm)

# Print the confusion matrix, precision, recall, and accuracy
print('Confusion Matrix_lm:\n', cm_lm)
print('Precision_lm:', precision_lm)
print('Recall_lm:', recall_lm)
print('Accuracy_lm:', accuracy_lm)

# Visualize confusion matrix using seaborn

sns.heatmap(cm_lm, annot=True)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()

y_pred_lm_df = pd.DataFrame(y_pred_lm, columns=['LM_Pred'])
y_pred_lm_df

y_test

y_test_df = pd.DataFrame(y_test,columns=['Orig'])
y_test_df

y_test_df['LM_Pred'] = y_pred_lm_df
y_test_df

# Get the odds ratio

import numpy as np
odds_ratio_lm = np.exp(lm.coef_)

print("Odds Ratio:", odds_ratio_lm)    # but this one does not look nice

# Create a pandas dataframe with the variable names and the odds ratio
df_lm = pd.DataFrame({'Variable': ['FSP', 'FSW', 'ACE', 'DBF', 'BPC', 'BPW', 'TPW'], 'Odds Ratio': odds_ratio_lm[0]})

df_lm

####################################
# ROC Curve Construction
####################################

# compute TPR = True Positive Rate and FPR=False Positive Rate for various thresholds

from sklearn.metrics import roc_curve, auc

fpr, tpr, thresholds = roc_curve(y_test, y_pred_lm)

# compute AUC
roc_auc = auc(fpr, tpr)

# plot ROC curve
plt.figure()
plt.plot(fpr, tpr,label='Logistic Regression (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], 'k--') # diagonal line for reference
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve - Tennis Match Statistics Dataset')
plt.legend(loc="lower right")
plt.show()


# The ROC curve below shows a near perfect model since the Blue ROC curve is almost touching the top left corner

from sklearn.metrics import roc_curve, auc, roc_auc_score

auc_lm = roc_auc_score(y_test, y_pred_lm)
auc_lm

from sklearn.neighbors import KNeighborsClassifier

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.3, random_state=0)

# Create a KNN classifier object : this is using a initial guess of k=3 neighbors, you can choose any small number

knn = KNeighborsClassifier(n_neighbors=5)

# Train the classifier on the training set
knn.fit(X_train, y_train)

# Predict the labels of the test set
y_pred = knn.predict(X_test)

# Print the accuracy of the classifier
print('Accuracy:', knn.score(X_test, y_test))

# Now it’s time to improve the model and find out the OPTIMAL k value.

error_rate = []

for i in range(1,40):
 knn = KNeighborsClassifier(n_neighbors=i)
 knn.fit(X_train,y_train)
 pred_i = knn.predict(X_test)
 error_rate.append(np.mean(pred_i != y_test))

plt.figure(figsize=(20,6))
plt.plot(range(1,40),error_rate,color='blue', linestyle='dashed', marker='o',markerfacecolor='red', markersize=10)
plt.title('Error Rate vs. K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')
print("Minimum error:-",min(error_rate),"at K =",error_rate.index(min(error_rate))+1)

# you see that the smallest error is at K=10

# see the error_rate visually

error_rate

acc = []

# Will take some time

from sklearn import metrics

for i in range(1,40):
    neigh = KNeighborsClassifier(n_neighbors = i).fit(X_train,y_train)
    yhat = neigh.predict(X_test)
    acc.append(metrics.accuracy_score(y_test, yhat))


plt.figure(figsize=(10,6))
plt.plot(range(1,40),acc,color = 'blue',linestyle='dashed', marker='o',markerfacecolor='red', markersize=10)
plt.title('accuracy vs. K Value')
plt.xlabel('K')
plt.ylabel('Accuracy')
print("Maximum accuracy:-",max(acc),"at K =",acc.index(max(acc))+1)


## we see from the plot that the accuracy is highest at K=10

# see the accuracies visually
acc

## So we will retrain the model with k=10

knn = KNeighborsClassifier(n_neighbors=10)

# Train the classifier on the training set
knn.fit(X_train, y_train)

# Predict the labels of the test set
y_pred_knn = knn.predict(X_test)

# Print the accuracy of the classifier
print('Accuracy_knn:', knn.score(X_test, y_test))

# Calculate the accuracy of the model
score_test_knn = knn.score(X_test, y_test)
score_train_knn = knn.score(X_train, y_train)

print("Accuracy Train_knn:", score_train_knn)    # here it is going to be 100% accurate, proving that the RF model over fitted the train dataset
print("Accuracy Test_knn:", score_test_knn)      # here it will be 97% accurate
print("Predictions_knn:", y_pred_knn)

y_pred_knn

y_pred_knn_df = pd.DataFrame(y_pred_knn,columns=['KNN_Pred'])
y_pred_knn_df

y_test_df['KNN_Pred'] = y_pred_knn_df
y_test_df

####################################
# ROC Curve Construction
####################################

# compute TPR = True Positive Rate and FPR=False Positive Rate for various thresholds

from sklearn.metrics import roc_curve, auc

fpr, tpr, thresholds = roc_curve(y_test, y_pred_knn)

# compute AUC
roc_auc = auc(fpr, tpr)

# plot ROC curve
plt.figure()
plt.plot(fpr, tpr,label='Logistic Regression (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], 'k--') # diagonal line for reference
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve - Tennis Matches Statistics')
plt.legend(loc="lower right")
plt.show()

from sklearn.metrics import roc_curve, auc, roc_auc_score

auc_knn = roc_auc_score(y_test, y_pred_knn)
auc_knn

from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming y_test is the actual test labels and y_pred_knn are the predicted labels from KNN

# Create the confusion matrix for KNN
conf_matrix_knn = confusion_matrix(y_test, y_pred_knn)

# Display the confusion matrix as a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix_knn, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix for K-Nearest Neighbors (KNN)')
plt.show()

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score

# Create the KNN classifier with k=10
knn = KNeighborsClassifier(n_neighbors=10)

# Train the classifier on the training set
knn.fit(X_train, y_train)

# Predict the labels of the test set
y_pred_knn = knn.predict(X_test)

# Calculate the accuracy of the model
accuracy_knn = accuracy_score(y_test, y_pred_knn)

# Calculate the confusion matrix for KNN
cm_knn = confusion_matrix(y_test, y_pred_knn)

# Calculate precision and recall for KNN
precision_knn = precision_score(y_test, y_pred_knn, average='macro')
recall_knn = recall_score(y_test, y_pred_knn, average='macro')

print('Accuracy for KNN:', accuracy_knn)
print('Confusion Matrix for KNN:\n', cm_knn)
print('precision_knn:', precision_knn)
print('recall_knn:', recall_knn)

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# Create a Linear Discriminant Analysis object
lda = LinearDiscriminantAnalysis()

# Train the classifier on the training set
lda.fit(X_train, y_train)

# Predict the labels of the test set
y_pred_lda = lda.predict(X_test)

# Calculate the accuracy of the model
score_test_lda = lda.score(X_test, y_test)
score_train_lda = lda.score(X_train, y_train)

print("Accuracy Train_lda:", score_train_lda)    # here it is going to be 100% accurate, proving that the RF model over fitted the train dataset
print("Accuracy Test_lda:", score_test_lda)      # here it will be 97% accurate
print("Predictions_lda:", y_pred_lda)

y_pred_lda_df = pd.DataFrame(y_pred_lda,columns=['LDA_Pred'])

y_test_df['LDA_Pred'] = y_pred_lda_df
y_test_df

from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming y_test is the actual test labels and y_pred_lda are the predicted labels

# Create the confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred_lda)

# Display the confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()

# Calculate precision, recall, and accuracy for LDA
precision_lda = precision_score(y_test, y_pred_lda, average='macro')
recall_lda = recall_score(y_test, y_pred_lda, average='macro')
accuracy_lda = accuracy_score(y_test, y_pred_lda)

# Calculate the confusion matrix for LDA
cm_lda = confusion_matrix(y_test, y_pred_lda)

# Print the confusion matrix, precision, recall, and accuracy for LDA
print('Confusion Matrix for LDA:\n', cm_lda)
print('Precision for LDA:', precision_lda)
print('Recall for LDA:', recall_lda)
print('Accuracy for LDA:', accuracy_lda)

####################################
# ROC Curve Construction
####################################

# compute TPR = True Positive Rate and FPR=False Positive Rate for various thresholds

from sklearn.metrics import roc_curve, auc

fpr, tpr, thresholds = roc_curve(y_test, y_pred_lda)

# compute AUC
roc_auc = auc(fpr, tpr)

# plot ROC curve
plt.figure()
plt.plot(fpr, tpr,label='Logistic Regression (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], 'k--') # diagonal line for reference
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve - Tennis Match Statistic Dataset')
plt.legend(loc="lower right")
plt.show()

from sklearn.metrics import roc_curve, auc, roc_auc_score

auc_knn = roc_auc_score(y_test, y_pred_lda)
auc_knn

from sklearn.ensemble import RandomForestClassifier

# Build the random forest model
rfc = RandomForestClassifier(n_estimators=100, random_state=42)
rfc.fit(X_train, y_train)

# Evaluate the model
print('Accuracy_rfc:', rfc.score(X_test, y_test))

# Predict the labels of the test set
y_pred_rfc = rfc.predict(X_test)

# Calculate the accuracy of the model
score_test_rfc = rfc.score(X_test, y_test)
score_train_rfc = rfc.score(X_train, y_train)

print("Accuracy Train_rfc:", score_train_rfc)    # here it is going to be 100% accurate, proving that the RF model over fitted the train dataset
print("Accuracy Test_rfc:", score_test_rfc)      # here it will be 97% accurate
print("Predictions_rfc:", y_pred_rfc)

y_pred_rfc_df = pd.DataFrame(y_pred_rfc,columns=['RF_Pred'])

y_test_df['RF_Pred']= y_pred_rfc_df
y_test_df

from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming y_test is the actual test labels and y_pred_rfc are the predicted labels

# Create the confusion matrix
conf_matrix_rfc = confusion_matrix(y_test, y_pred_rfc)

# Display the confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix_rfc, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix for Random Forest Classifier')
plt.show()

# Calculate precision, recall, and accuracy for RFC
precision_rfc = precision_score(y_test, y_pred_rfc, average='macro')
recall_rfc = recall_score(y_test, y_pred_rfc, average='macro')
accuracy_rfc = accuracy_score(y_test, y_pred_rfc)

# Calculate the confusion matrix for RFC
cm_rfc = confusion_matrix(y_test, y_pred_rfc)

# Print the confusion matrix, precision, recall, and accuracy for RFC
print('Confusion Matrix for RFC:\n', cm_rfc)
print('Precision for RFC:', precision_rfc)
print('Recall for RFC:', recall_rfc)
print('Accuracy for RFC:', accuracy_rfc)

####################################
# ROC Curve Construction
####################################

# compute TPR = True Positive Rate and FPR=False Positive Rate for various thresholds

from sklearn.metrics import roc_curve, auc

fpr, tpr, thresholds = roc_curve(y_test, y_pred_rfc)

# compute AUC
roc_auc = auc(fpr, tpr)

# plot ROC curve
plt.figure()
plt.plot(fpr, tpr,label='Logistic Regression (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], 'k--') # diagonal line for reference
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve - Tennis Match Statistic Dataset')
plt.legend(loc="lower right")
plt.show()

from sklearn.metrics import roc_curve, auc, roc_auc_score

auc_knn = roc_auc_score(y_test, y_pred_rfc)
auc_knn

from xgboost import XGBClassifier

# Build the XGBoost model
xgb_model = XGBClassifier(objective='binary:logistic', random_state=42)
xgb_model.fit(X_train, y_train)

# Evaluate the model
print('Accuracy_xgb:', xgb_model.score(X_test, y_test))

# Predict the labels of the test set
y_pred_xgb = xgb_model.predict(X_test)

# Calculate the accuracy of the model
score_test_xgb = xgb_model.score(X_test, y_test)
score_train_xgb = xgb_model.score(X_train, y_train)

print("Accuracy Train_xgb:", score_train_xgb)    # here it is going to be 100% accurate, proving that the RF model over fitted the train dataset
print("Accuracy Test_xgb:", score_test_xgb)      # here it will be 97% accurate
print("Predictions_xgb:", y_pred_xgb)

print("*******************************************")
print("********* Accuracy during Training ********")
print("*******************************************")
print("                                           ")
print("Accuracy Train_lm.   :", score_train_lm)
print("Accuracy Train_knn.  :", score_train_knn)
print("Accuracy Train_rfc.  :", score_train_rfc)


print("                                           ")
print("*******************************************")
print("********* Accuracy during Testing ********")
print("*******************************************")
print("                                           ")
print("Accuracy Test_lm    :", score_test_lm)
print("Accuracy Test_knn.  :", score_test_knn)
print("Accuracy Test_rfc.  :", score_test_rfc)



# Here you discuss which model performed best during Testing, that is basically your best model
# Talk about the models that outperformed during Training significantly relative to Testing, those are models that sufferred from overfitting (e.g., RFC, XGBoost)

