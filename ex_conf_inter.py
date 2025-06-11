import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

M = 20

n = 64
x = 18.5
std = 4
sem = std / np.sqrt(n)
Z = (x-M)/sem
p = (stats.norm(x, sem).sf(M) * 2)
if p < 0.05:
    print(f'среднее ГС не входит в 95% доверительный интервал, ее p = {p:.4f}\np в процентах = {p * 100:.2f}%')
else: print(f'нулевая гипотеза не может быть отброшена, ее p = {p:.4f}\np в процентах = {p * 100:.2f}%')