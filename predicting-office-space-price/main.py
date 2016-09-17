# coding:utf-8
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.grid_search import GridSearchCV
np.random.seed(215)

F, N = map(int, input().split())
train = np.array([list(map(float, input().split())) for _ in range(N)])
X, y = train[:, 0:-1], train[:, -1]

param_grid = {
    'poly__degree': [2, 3, 4],
    'poly__include_bias': [True, False],
    'linear__fit_intercept': [True, False],
}
model = GridSearchCV(
    estimator=Pipeline([
        ('poly', PolynomialFeatures()),
        ('linear', LinearRegression()),
    ]),
    param_grid=param_grid,
    scoring='mean_absolute_error',
)

model.fit(X, y)

T = int(input())
test = np.array([list(map(float, input().split())) for _ in range(T)])
pred = model.predict(test)
print('\n'.join(map(str, pred.tolist())))
