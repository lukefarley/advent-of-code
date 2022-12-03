import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPRegressor, MLPClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import (
    confusion_matrix,
    average_precision_score,
    precision_recall_curve,
)


def get_fuel_usage(positions, alignment_pos):
    return sum([abs(p - alignment_pos) for p in positions])


def get_optimal_pos(positions, f):
    results = [f(positions, i) for i in range(max(positions))]
    return results.index(min(results))


def get_fuel_usage2(positions, alignment_pos):
    return sum([sum(list(range(1, abs(p - alignment_pos) + 1))) for p in positions])


# y = X.apply(lambda x: get_fuel_usage(list(x)[:-1], list(x)[-1]), axis=1)

Xtrain = pd.DataFrame(np.random.uniform(1, 10, size=(100000, 10)).astype(int))
Xtrain.columns = [f"x{i}" for i in range(Xtrain.shape[1])]
ytrain = Xtrain.apply(lambda x: get_optimal_pos(list(x), get_fuel_usage), axis=1)

# Xtrain['pos'] = np.random.uniform(2, 9, size = Xtrain.shape[0]).astype(int)
# ytrain = Xtrain.apply(lambda x: get_fuel_usage(list(x)[:-1], list(x)[-1]), axis=1)

Xtest = pd.DataFrame(np.random.uniform(1, 10, size=(100, 10)).astype(int))
Xtest.columns = [f"x{i}" for i in range(Xtest.shape[1])]
ytest = Xtest.apply(lambda x: get_optimal_pos(list(x), get_fuel_usage), axis=1)

lm = LinearRegression().fit(Xtrain, ytrain)
lm_preds = np.round(lm.predict(Xtest)).astype(int)
lm_preds_prob = np.round(lm.predict_proba(Xtest)[:, 1])

confusion_matrix(ytest, lm_preds)
# average_precision_score(ytest, lm_preds)

rf = RandomForestClassifier().fit(Xtrain, ytrain)
rf_preds = np.round(rf.predict(Xtest)).astype(int)
confusion_matrix(ytest, rf_preds)

nn = MLPClassifier().fit(Xtrain, ytrain)
nn_preds = np.round(nn.predict(Xtest)).astype(int)
confusion_matrix(ytest, nn_preds)


if __name__ == "__main__":

    with open("data/day07.txt") as f:
        positions = [int(x) for x in f.read().split(",")]

    results = {}
    for i in range(1000):
        results[i] = get_fuel_usage(positions, i)

    vals = list(results.values())
    print("Part 1:", vals[vals.index(min(vals))])

    results = {}
    for i in range(1000):
        results[i] = get_fuel_usage2(positions, i)

    vals = list(results.values())
    print("Part 2:", vals[vals.index(min(vals))])
