#!/usr/bin/env python
# coding: utf-8

# In[38]:


#importing libraries 

import pandas as pd
import numpy as np


# In[39]:


#importing Dataset

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/glass/glass.data'
data = pd.read_csv(url, header=None)
data.head()


# # Exploring Dataset:
#     1.shape of dataset
#     2.count of null values 
#     3.uniques values 
#     4.statistics of dataset

# In[40]:


data.shape


# In[41]:


data.isnull().sum()


# In[42]:


data[10].value_counts()


# In[43]:


data.describe()


# # preparing Dataset
# Adding meaningfull column / attribute names

# In[44]:


names = ['Id','RI','Na','Mg','Al','Si','K','Ca','Ba','Fe','glass_type']
data.columns = names
data.head()

Removing Unnecessary Columns
# In[45]:


data = data.drop('Id',1)


# In[46]:


data.head(3)


# # Checking Outlines through Z-score

# In[47]:


from scipy import stats

z = abs(stats.zscore(data))

#np.where(z > 3)

data = data[(z < 3).all(axis=1)]

#data.shape


# # Separating Features and Label

# In[48]:



features = ['RI','Na','Mg','Al','Si','K','Ca','Ba','Fe']
label = ['glass_type']

X = data[features]

y = data[label]


# In[49]:


X.shape


# In[50]:


type(X)


# # Data Visualization

# In[51]:



x2 = X.values

from matplotlib import pyplot as plt
import seaborn as sns
for i in range(1,9):
        sns.distplot(x2[i])
        plt.xlabel(features[i])
        plt.show()


# In[52]:


x2 = pd.DataFrame(X)

plt.figure(figsize=(8,8))
sns.pairplot(data=x2)
plt.show()


# In[53]:


coreleation= X.corr()
plt.figure(figsize=(15,15))
sns.heatmap(coreleation,cbar=True,square=True,annot=True,fmt='.1f',annot_kws={'size': 15},xticklabels=features,yticklabels=features,alpha=0.7,cmap= 'coolwarm')
plt.show()


# In[54]:


## normalizing/Scalling the data  

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
#scaler.fit(X)
#X = scaler.transform(X)
#X = pd.DataFrame(X)


# In[55]:


X.head(2)


# In[56]:


y.head(2)


# # Scallig the features

# In[57]:


from sklearn import preprocessing
X=preprocessing.scale(X)


# # visualizing data after preprocessing

# In[58]:


x2 = X

from matplotlib import pyplot as plt
import seaborn as sns
for i in range(1,9):
        sns.distplot(x2[i])
        plt.xlabel(features[i])
        plt.show()


# # train test split

# In[59]:


from sklearn.model_selection import train_test_split


# In[60]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0,stratify=y)


# In[61]:


## Flattening the array
y_train = y_train.values.ravel()
y_test = y_test.values.ravel()


# In[62]:


print('Shape of X_train = ' + str(X_train.shape))
print('Shape of X_test = ' + str(X_test.shape))
print('Shape of y_train = ' + str(y_train.shape))
print('Shape of y_test = ' + str(y_test.shape))


# # Applying Different ML Models

# # 1.knn

# In[69]:



from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

Scores = []

for i in range (2,11):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    score = knn.score(X_test,y_test)
    Scores.append(score)

print(knn.score(X_train,y_train))
print(Scores)


# # 2.Logistic Regression

# In[70]:


from sklearn.linear_model import LogisticRegression

Scores = []

for i in range(1):
    logistic = LogisticRegression(random_state=0, solver='lbfgs',multi_class='multinomial',max_iter=100)
    logistic.fit(X_train, y_train)
    score = logistic.score(X_test,y_test)
    Scores.append(score)
    
print(logistic.score(X_train,y_train))
print(Scores)


# 3.SVC Classifier (non linear)

# In[71]:


from sklearn.svm import SVC

Scores = []

for i in range(1):
    svc = SVC(gamma='auto')
    svc.fit(X_train, y_train)
    score = svc.score(X_test,y_test)
    Scores.append(score)

print(svc.score(X_train,y_train))
print(Scores)


# # Summary
# 
# But since it is overfitting we will choose next best model that is:
# SVM (Non Linear Kernal)
# 
# training accuracy: 0.7586206896551724
# testing accuracy: 0.7551020408163265
# 

# In[ ]:




