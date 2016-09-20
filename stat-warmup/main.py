import numpy as np
from scipy import stats

N = int(input())
data = input()
data = np.array(list(map(float, data.split())))
print(data.mean())
print(np.median(data))
print(int(stats.mode(data).mode[0]))
print('%.1f' % (np.std(data)))
t_min = data.mean() - 1.96 * np.std(data)/np.sqrt(N)
t_max = data.mean() + 1.96 * np.std(data)/np.sqrt(N)
print('%.1f %.1f' % (t_min, t_max))
