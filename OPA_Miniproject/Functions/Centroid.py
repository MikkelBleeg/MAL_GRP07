# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 07:59:09 2020

@author: Morten Sahlertz
"""
import numpy as np
from sklearn.neighbors import NearestCentroid
import plotly
import plotly.graph_objects as go
import numpy as np
import plotly.offline as py
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

def run_NearestCentroid(X_train, X_test, y_train):
    centroid = NearestCentroid()

    centroid.fit(X_train, y_train)
    cents = centroid.centroids_
    y_pred = centroid.predict(X_test)
    return y_pred, cents

def run_NearestNeighbor(X_train, X_test, y_train, neighbors=1):
    neighbor = KNeighborsClassifier(n_neighbors=neighbors)
    neighbor.fit(X_train, y_train)
    y_pred = neighbor.predict(X_test)
    return y_pred

# def run_bayes(): #X_train, X_test, y_train
#     X_train = np.array([[0, 1, 3, 3, 4],
#                         [1, 1, 1, 2, 2]]).T
#     y_train = np.array([1, 1, 2, 2, 2])
#     X_test = np.array([[1, 3, 2],
#                        [2, 0, 1]]).T
#     X_test_df = pd.DataFrame(X_test).rename(columns={0: "x1", 1: "x2"}).T
#
#     df = pd.concat([pd.DataFrame(X_train).rename(columns={0: "x1", 1: "x2"}),
#                    pd.DataFrame(y_train).rename(columns={0: "label"})], axis=1)
#     classes = dict(list(df.groupby(["label"])))
#     #average vectors
#     avg = {}
#     for class_no in classes.keys():
#         avg[class_no] = {"x1": classes[class_no]["x1"].mean(), "x2": classes[class_no]["x2"].mean()}
#     average_vectors = pd.DataFrame(avg)
#     #################
#     v = pd.DataFrame()
#     for i in average_vectors:
#         current_vector = average_vectors.T.loc[i]
#
#         for test_sample in X_test_df:
#             current_sample = X_test_df[test_sample]
#             sample_minus_mean = current_vector - current_sample
#             v.loc[i, test_sample] = 1 / (sum(sample_minus_mean.multiply(sample_minus_mean)))
#
#     p = {}
#
#     for i in v:
#         vck = v[i]
#         q[i] ={1:vck1[0], 2: }
#
#
#
#     return v.T

def plot_test_and_train(X_train, X_test, y_test, enable_centroids=False):

    data=[
        go.Scatter(x=X_train.T[0],
                   y=X_train.T[1],
                   mode='markers',
                   marker=dict(
                       color='Green',
                       size=14,
                       line=dict(
                           color='LightSkyBlue',
                           width=2
                       )
                   ),
                   name='Traning data'
                   ),
        go.Scatter(x=X_test.T[0],
                   y=X_test.T[1],
                   mode='markers',
                   marker=dict(
                       color='blue',
                       size=14,
                       line=dict(
                           color='Purple',
                           width=2
                       )
                   ),
                   name='Test data'
        )
    ]
    if enable_centroids:
        pred, cents = run_NearestCentroid(X_train, X_test, y_train)
        cent_x = []
        cent_y = []
        for i in range(cents.shape[0]):
            cent_x.append(cents[i][0])
            cent_y.append(cents[i][1])
        data.append(
            go.Scatter(
                x=cent_x,
                y=cent_y,
                mode='markers',
                marker=dict(
                    color='red',
                    size=14,
                    line=dict(
                        color='black',
                        width=2
                    )
                ),
                name='Centroids'
                ),
            )
    fig = go.Figure(data)
    py.plot(fig, filename="plot.html")

if __name__ == '__main__':
    run_bayes()
    X_train = np.array([[0, 1, 1, 3, 3, 4, 4],
                        [1, 0, 1, 1, 2, 1, 2]]).T
    y_train = np.array([1, 1, 1, 2, 2, 2, 2])
    X_test = np.array([[1, 3, 2],
                       [2, 0, 1]]).T
    plot_test_and_train(X_train, X_test, y_train, True)
    prediction_NC, cents = run_NearestCentroid(X_train, X_test, y_train)
    prediction_KNN = run_NearestNeighbor(X_train, X_test, y_train)
    print(prediction_NC)
    print(prediction_KNN)

