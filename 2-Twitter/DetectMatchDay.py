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
import datetime

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# %% [markdown]
# ## 1. Filter & Merge Badminton Dataset

# %%


def extractDate(value):
    date_time_obj = pd.to_datetime(value)
    print('Date:', date_time_obj.date())


# %%
dataset = pd.read_csv("./2-Twitter/Barcelona_1.csv")
print(list(dataset.columns))

dates = extractDate(dataset['timestamp'].values[0])
# dates = dataset['timestamp'].apply(extractDate)
