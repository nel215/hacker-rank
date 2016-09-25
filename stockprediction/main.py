# coding:utf-8
import numpy as np
from scipy import stats


def interval(prices):
    m = np.mean(prices)
    s = stats.sem(prices)
    return stats.t.interval(0.9, len(prices) - 1, loc=m, scale=s)


def low(prices):
    ci = interval(prices)
    return prices[-1] < ci[0]


def high(prices):
    ci = interval(prices)
    return prices[-1] > ci[1]

res = []
m, k, d = input().split()
m = float(m)
for i in range(int(k)):
    stock = input().split()
    name, owned, prices = stock[0], int(stock[1]), stock[2:]
    prices = list(map(float, prices))
    if owned > 0 and high(prices):
        res.append('{} SELL 1'.format(name))
    elif m >= prices[-1] and low(prices):
        m -= prices[-1]
        res.append('{} BUY 1'.format(name))

print(len(res))
print('\n'.join(res))
