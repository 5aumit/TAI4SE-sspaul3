# -*- coding:UTF-8 -*-
import numpy as np
import collections

X1D = {
    0: '1',
    1: '2',
    2: '3'
}
X2D = {
    0: 'S',
    1: 'M',
    2: 'L'
}
YD = {
    0: '-1',
    1: '1'
}

X1E = {
    '1': 0,
    '2': 1,
    '3': 2
}
X2E = {
    'S': 0,
    'M': 1,
    'L': 2
}
YE = {
    '-1': 0,
    '1': 1,
}


def decode(vec):
    return [X1D[vec[0]], X2D[vec[1]], YD[vec[2]]]


def encode(vec):
    return [X1E[vec[0]], X2E[vec[1]], YE[vec[2]]]


def load_data(path="./dataset"):
    data_set = []
    with open(path, 'r') as f:
        for i in f.readlines():
            line = i.replace('\n', '').split(sep=',')
            data_set.append(line[:])
    return np.array(data_set)


def naive_bayes_MLE(data_set, x):
    # Maximum likelihood estimation
    fearure = fearure_count(data_set)
    N = np.sum(fearure)
    res = []
    for y in np.unique(data_set[:, 2]):
        P1 = np.sum(fearure[:, :, YE[y]]) / N
        # P(Y=1)
        P2 = np.sum(fearure[X1E[x[0]], :, YE[y]]) / \
            np.sum(fearure[:, :, YE[y]])
        # P(X1=x1|Y=y)
        P3 = np.sum(fearure[:, X2E[x[1]], YE[y]]) / \
            np.sum(fearure[:, :, YE[y]])
        # P(X2=x2|Y=y)
        res.append([y, P1*P2*P3])
    res.sort(key=lambda x: x[1], reverse=True)
    print('> Maximum likelihood estimation <')
    print(res)
    return res[0][0]


def naive_bayes_BE(data_set, x, λ=1):
    # Bayesian estimation
    fearure = fearure_count(data_set)
    N = np.sum(fearure)
    K = np.unique(data_set[:, 2]).shape[0]
    res = []
    # Laplace smoothing
    for y in np.unique(data_set[:, 2]):
        P1 = (np.sum(fearure[:, :, YE[y]]) + λ) / (N + K*λ)
        # P(Y=1)
        P2 = (np.sum(fearure[X1E[x[0]], :, YE[y]]) + λ) / \
            (np.sum(fearure[:, :, YE[y]]) +
             np.unique(data_set[:, 0]).shape[0] * λ)
        # P(X1=x1|Y=y)
        P3 = (np.sum(fearure[:, X2E[x[1]], YE[y]]) + λ) / \
            (np.sum(fearure[:, :, YE[y]]) +
             np.unique(data_set[:, 1]).shape[0] * λ)
        # P(X2=x2|Y=y)
        res.append([y, P1*P2*P3])
    res.sort(key=lambda x: x[1], reverse=True)
    print('> Bayesian estimation <')
    print(res)
    return res[0][0]


def fearure_count(data_set):
    count = np.zeros((3, 3, 2)).astype(np.int)
    for vec in data_set:
        vec = encode(vec)
        count[vec[0], vec[1], vec[2]] += 1
    return count


if __name__ == "__main__":
    data_set = load_data()
    x = np.array(['2', 'S'])

    y = naive_bayes_MLE(data_set, x)
    print('Maximum likelihood estimation:', x, 'is', y)
    print('-'*30)
    y = naive_bayes_BE(data_set, x, λ=1)
    print('Bayesian estimation:', x, 'is', y)
