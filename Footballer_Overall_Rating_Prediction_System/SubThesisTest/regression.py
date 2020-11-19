import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score
from math import sqrt

df = pd.read_excel('SubThesisTest/Player_Attributes.xlsx')
df1 = pd.read_excel('SubThesisTest/Player.xlsx')

features = ['potential', 'crossing', 'finishing', 'heading_accuracy',
            'short_passing', 'volleys', 'dribbling', 'curve', 'free_kick_accuracy',
            'long_passing', 'ball_control', 'acceleration', 'sprint_speed',
            'agility', 'reactions', 'balance', 'shot_power', 'jumping', 'stamina',
            'strength', 'long_shots', 'aggression', 'interceptions', 'positioning',
            'vision', 'penalties', 'marking', 'standing_tackle', 'sliding_tackle',
            'gk_diving', 'gk_handling', 'gk_kicking', 'gk_positioning',
            'gk_reflexes']

target = ['overall_rating']
df = df.dropna()
X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=324)

# Linear_Regression
lregressor = LinearRegression()
lregressor.fit(X_train, y_train)


def idSearch(i):
    match = (df1['player_name'] == i)
    mats = df1.loc[match]
    mat = mats.copy()
    if mat.empty:
        player = 0
        return player
    player = mat.iloc[0]['player_api_id']
    return player


def acutual(i):
    grimm = (df['player_api_id'] == i)
    mats = df.loc[grimm]
    jack = mats.copy()
    actual_rate = jack.iloc[0]['overall_rating']
    return actual_rate


def linear_regressor(i):
    grimm = (df['player_api_id'] == i)
    mats = df.loc[grimm]
    input_data = mats.copy()
    real_input = input_data.head(1)
    finale = real_input[features]
    return lregressor.predict([finale.iloc[0]])


# KNN
kregressor = KNeighborsRegressor()
kregressor.fit(X_train, y_train)


def knn_regressor(i):
    grimm = (df['player_api_id'] == i)
    mats = df.loc[grimm]
    input_data = mats.copy()
    real_input = input_data.head(1)
    finale = real_input[features]
    return kregressor.predict([finale.iloc[0]])


# Decision_tree
dregressor = DecisionTreeRegressor()
dregressor.fit(X_train, y_train)


def decision_tree_regressor(i):
    grimm = (df['player_api_id'] == i)
    mats = df.loc[grimm]
    input_data = mats.copy()
    real_input = input_data.head(1)
    finale = real_input[features]
    return dregressor.predict([finale.iloc[0]])


def player_name():
    rukia = df1['player_name'].values
    return rukia