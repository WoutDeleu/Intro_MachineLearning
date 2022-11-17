# %% [markdown]
# # Machine learning - Predict MatchDay

# %% [markdown]
# ## 0. Imports

# %%
import pandas as pd
import math
from pandas.plotting import scatter_matrix
from sklearn.model_selection import train_test_split
from matplotlib import pyplot
import os

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# %% [markdown]
# ## 1. Filter & Format Barcelona Dataset

# %% [markdown]
# ### 1.1 Read in csv-files

# %%
# Read in CSV's in folder
totalFileList = os.listdir(
    "/home/woutd/Documents/School/Industriele Ingenieurswetenschappen/Ma1/Sem1/Machine Learning/Opdracht/Workspace/2-Twitter/")
listFileNames = []
for fileName in totalFileList:
    if ('Barcelona' in fileName):
        listFileNames.append(fileName)
datasets = []
for fileName in listFileNames:
    datasets.append(pd.read_csv(
        "/home/woutd/Documents/School/Industriele Ingenieurswetenschappen/Ma1/Sem1/Machine Learning/Opdracht/Workspace/2-Twitter/" + str(fileName)))


# %% [markdown]
# ### 1.2 Merge datasets into 1

# %%
merged_dataset = pd.DataFrame()
for dataset in datasets:
    merged_dataset = pd.concat([merged_dataset, dataset])
merged_dataset.drop_duplicates()

print(list(merged_dataset.columns))

# %% [markdown]
# ### 1.3 Format dataset [date, count]

# %%


def extractDate(value):
    date = pd.to_datetime(value)
    return date.date()


def incr(value):
    return value + 1


# %%
merged_dataset['dates'] = merged_dataset['timestamp'].apply(extractDate)

dataset = pd.DataFrame(columns=['Date', 'Count'])
for date in merged_dataset['dates']:
    if (date in dataset['Date'].unique()):
        dataset.loc[dataset['Date'] == date, 'Count'] += 1
    else:
        # print('Fail')
        dataset = pd.concat([dataset, pd.DataFrame(
            [[date, 0]], columns=['Date', 'Count'])])
dataset.drop_duplicates()
print(list(dataset.columns))
print(dataset)
