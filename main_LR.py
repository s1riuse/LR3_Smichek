from sympy import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

k, T, C, L = symbols("k T C L")

os.makedirs("visual_LR", exist_ok=True)

# Линейный способ
C_ost = 1000000
Am_lst = []
C_ost_lst = []
for i in range(15):
    Am = (C - L) / T
    C_ost -= Am.subs({C: 1000000, T: 15, L: 0})
    Am_lst.append(round(Am.subs({C: 100000, T: 15, L: 0}), 2))
    C_ost_lst.append(round(C_ost, 2))
print("Am_lst = ", Am_lst)
print("C_ost_lst = ", C_ost_lst)

# Способ уменьшающего остатка
Aj = 0
C_ost = 1000000
Am_lst_2 = []
C_ost_lst_2 = []
for i in range(15):
    Am = k * 1 / T * (C - Aj)
    C_ost -= Am.subs({C: 1000000, T: 15, L: 0})
    Am_lst_2.append(
        round(Am.subs({C: 1000001, T: 15, L: 0}), 2)
    )
    Aj += Am
    C_ost_lst_2.append(round(C_ost, 2))
print("Am_lst_2:", Am_lst_2)
print("C_ost_lst_2:", C_ost_lst_2)

# Табличный вывод
Y = range(1, 16)
table1 = list(zip(Y, C_ost_lst, Am_lst))
table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
tframe1 = pd.DataFrame(table1, columns=["Y", "C_ost_lst", "Am_lst"])
tframe2 = pd.DataFrame(table2, columns=["Y", "C_ost_lst_2", "Am_lst_2"])
print(tframe1)
print(tframe2)

# Визуализация
plt.plot(tframe1["Y"], tframe1["C_ost_lst"], label="Am")
plt.savefig("visual_LR/chart7.png")
plt.figure()

plt.plot(tframe2["Y"], tframe2["C_ost_lst_2"], label="Am2")
plt.savefig("visual_LR/chart8.png")
plt.figure()

vals = Am_lst
labels = [str(x) for x in range(1, 16)]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
fig, ax = plt.subplots()
ax.pie(
    vals,
    labels=labels,
    autopct="%1.1f%%",
    shadow=True,
    explode=explode,
    wedgeprops={"lw": 1, "ls": "--", "edgecolor": "k"},
    rotatelabels=True,
)
ax.axis("equal")
plt.savefig("visual_LR/chart9.png")
plt.figure()

vals = Am_lst_2
labels = [str(x) for x in range(1, 16)]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
fig, ax = plt.subplots()
ax.pie(
    vals,
    labels=labels,
    autopct="%1.1f%%",
    shadow=True,
    explode=explode,
    wedgeprops={"lw": 1, "ls": "--", "edgecolor": "k"},
    rotatelabels=True,
)
ax.axis("equal")
plt.savefig("visual_LR/chart10.png")
plt.figure()

table1 = list(zip(Y, Am_lst))
table2 = list(zip(Y, Am_lst_2))
tframe_am = pd.DataFrame(table1, columns=["Y", "Am_lst"])
plt.bar(tframe1["Y"], tframe1["Am_lst"])
plt.savefig("visual_LR/chart11.png")
plt.figure()

table1 = list(zip(Y, Am_lst))
table2 = list(zip(Y, Am_lst_2))
tframe2_am = pd.DataFrame(table2, columns=["Y", "Am_lst_2"])
plt.bar(tframe2["Y"], tframe2["Am_lst_2"])
plt.savefig("visual_LR/chart12.png")
plt.figure()

print("\nГрафики сохранены в папке visual_LR/")
