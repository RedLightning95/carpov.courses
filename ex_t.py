import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

print('первый вариант решения, с использованием всех измерений')
first = '84,7   105,0   98,9   97,9   108,7   81,3   99,4   89,4   93,0   119,3   99,2   99,4   97,1   112,4   99,8   94,7   114,0   95,1   115,5   111,5'
second =  '57,2   68,6   104,4   95,1   89,9   70,8   83,5   60,1   75,7   102,0   69,0   79,6   68,9   98,6   76,0   74,8   56,0   55,6   69,4   59,5'

fir = first.replace(',', '.')
sec = second.replace(',', '.')

data1 = list(map(float, fir.split()))
data2 = list(map(float, sec.split()))

arr1 = pd.Series(data1)
arr2 = pd.Series(data2)

t_statistic, p_value = stats.ttest_ind(arr1, arr2, equal_var=True)
print(f't = {t_statistic:.4f}\np = {p_value:.4f}')

print('второй вариант решения, с использованием приведенных данных (mean, std, len)')
x1 = 89.9
x2 = 80.7
std1 = 11.3
std2 = 11.7
n1 = 20
n2 = 20

t = (x1 - x2) / np.sqrt(((std1 ** 2)/n1) + ((std2 ** 2)/n2))
df = n1+n2-2
print(f'p-value = {2 * (stats.t.sf(abs(t), df)):.4f}')


data = {'type 1': arr1,
        'type 2': arr2}
data = pd.DataFrame(data)
plt.title('Распределение средних разных выборок')
plt.ylabel('Температура плавления')
plt.boxplot(data, tick_labels=data.columns)
plt.grid()
plt.show()