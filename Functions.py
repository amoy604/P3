#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd 
import pickle

from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_selection import SelectKBest
from sklearn.preprocessing import KBinsDiscretizer, OneHotEncoder, StandardScaler
from sklearn.metrics import confusion_matrix, plot_confusion_matrix
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.naive_bayes import BernoulliNB, BaseEstimator, BaseNB
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline

import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px
import plotly
import plotly.graph_objects as go


# In[2]:


class Cleaner(BaseEstimator):
    
    def __init__( self, columns=None, cat_features=None):
        self.columns = columns
        self.cat_features = cat_features
    
    def fit( self, X, y = None ):
        return self 
    
    def transform( self, X, y = None):
        # fill blanks
        try:
            X['public_meeting'] = X['public_meeting'].fillna(value='unknown', axis=0)
        except:
            X=X

        # consolidate rare groups into bigger groups
        try:
            X['waterpoint_type_group'] = X['waterpoint_type_group'].map(lambda x: 'dam, trough, or spring' if x.lower() == 'dam' 
                                                                                else 'dam, trough, or spring' if x.lower() == 'cattle trough' 
                                                                                else 'dam, trough, or spring' if x.lower() == 'improved spring'
                                                                                else x.lower())
        except:
            X=X
        try:
            X['extraction_type_class'] = X['extraction_type_class'].map(lambda x: 'other' if x.lower() == 'wind-powered' 
                                                                                else 'other' if x.lower() == 'rope pump' 
                                                                                else x)
        except:
            X=X

        try:                                                                                
        # take the top members of a category and group the rest together                                                            
            X['management'] = X['management'].map(lambda x: x if x.lower() == 'vwc' 
                                                            else x if x.lower() == 'wug' 
                                                            else x if x.lower() == 'water board' 
                                                            else x if x.lower() == 'wua' 
                                                            else x if x.lower() == 'private operator' 
                                                            else x if x.lower() == 'parastatal' 
                                                            else 'misc.')
        except:
            X=X
        try:
            X['funder'] = X['funder'].map(lambda x: x if x == 'Government Of Tanzania' 
                                                        else x if x == 'Danida' 
                                                        else x if x == 'Hesawa' 
                                                        else x if x == 'Rwssp' 
                                                        else x if x== 'World Bank' 
                                                        else x if x == 'World Vision' 
                                                    else 'misc.')
        except:
            X=X
        try:                                                    
            X['installer'] = X['installer'].map(lambda x: x if x == 'DWE' 
                                                        else x if x == 'Government' 
                                                        else x if x == 'RWE' 
                                                        else 'misc.')
        except:
            X=X            

        try:
            X['district_code'] = X['district_code'].map(lambda x: str(x) if 0 < x < 6 else 'other')
        except:
            X=X
        
        # dummify categorical columns
        X = pd.get_dummies(X, columns=self.cat_features)
        return X


# In[5]:


train_values = pd.read_csv("./Data/training_set_values.csv")
train_labels = pd.read_csv("./Data/training_set_labels.csv")
test_set = pd.read_csv("./Data/water_test.csv")


# In[4]:


train_set = pd.merge(train_values, train_labels, on="id")


# In[ ]:




