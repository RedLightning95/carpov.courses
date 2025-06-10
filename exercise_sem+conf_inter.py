import numpy as np
import pandas as pd
import random as r
y = '102 91 99 100 103 98 99 101 106 93 103 97 103 101 101 91 104 105 105 100 101 91 99 98 102 102 100 97 100 102 100 98 102 99 94 104 104 97 99 102 98 107 101 93 98 101 100 91 100 102 96 93 100 105 103 107 99 102 106 102 94 104 103 102'
data = list(map(int, y.split()))
arr = pd.Series(data) # приводим набор чисел к удобному для нас формату (series/серии)

sem = arr.sem() # по заданию необходимо найти стандартную ошибку 95%-го доверительного интервала
print(f'se: {arr.sem(): .2f}\n95% доверительный интервал = {arr.mean() - arr.sem() * 1.96: .2f} : {arr.mean() + arr.sem() * 1.96: .2f}')
min_of_conf_interval = arr.mean() - arr.sem() * 1.96 
max_of_conf_interval = arr.mean() + arr.sem() * 1.96 # находим min и max значения доверительного интервала

# далее идет необязательная, но интересная часть, где мы пытаемся 
# найти такую случайную выборку, при которой среднее значение ГС будет вне доверительного 95-ти % интервала выборки, а также кол-во попыток
count = 0
rand_from_data = r.sample(data, 31)
arr_rand = pd.Series(rand_from_data)
while min_of_conf_interval < arr_rand.mean() < max_of_conf_interval:
    rand_from_data = r.sample(data, 31)
    arr_rand = pd.Series(rand_from_data)
    count += 1
    if min_of_conf_interval > arr_rand.mean() or arr_rand.mean() > max_of_conf_interval:
        print('найдена выборка, доверительный интервал которой, не включает в себя среднее ГС')
        print(f'кол-во попыток найти ее = {count}')
        print(f'ее среднее - {arr_rand.mean(): .2f}')

