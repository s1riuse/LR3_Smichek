from sympy import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

k, T, C, L = symbols("k T C L")


# Линейный способ
# Линейный способ
C_ost = 1000000  # изменено на 40000
Am_lst = []
C_ost_lst = []
for i in range(15):
    Am = (C - L) / T
    C_ost -= Am.subs({C: 1000000, T: 15, L: 0})  # изменено 40000 и 10 лет
    Am_lst.append(round(Am.subs({C: 100000, T: 15, L: 0}), 2))  # изменено 40000 и 10 лет
    C_ost_lst.append(round(C_ost, 2))
print("Am_lst = ", Am_lst)
print("C_ost_lst = ", C_ost_lst)

# Способ уменьшающего остатка
Aj = 0
C_ost = 1000000  # изменено 1000000 и 15 лет
Am_lst_2 = []
C_ost_lst_2 = []
for i in range(15):
    Am = k * 1 / T * (C - Aj)
    C_ost -= Am.subs({C: 1000000, T: 15, L: 0})  # изменено 40000 и 10 лет
    Am_lst_2.append(
        round(Am.subs({C: 1000000, T: 15, L: 0}), 2)
    )  # изменено 1000000 и 15 лет
    Aj += Am
    C_ost_lst_2.append(round(C_ost, 2))
print("Am_lst_2:", Am_lst_2)
print("C_ost_lst_2:", C_ost_lst_2)


# Табличный вывод
Y = range(1, 16)  # цикл от 1 до 10 включительно
table1 = list(zip(Y, C_ost_lst, Am_lst))
table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
tframe1 = pd.DataFrame(table1, columns=["Y", "C_ost_lst", "Am_lst"])
tframe2 = pd.DataFrame(table2, columns=["Y", "C_ost_lst_2", "Am_lst_2"])
print(tframe1)
print(tframe2)

# Визуализация
plt.plot(tframe1["Y"], tframe1["C_ost_lst"], label="Am")
plt.savefig("chart7.png")
plt.figure()

plt.plot(tframe2["Y"], tframe2["C_ost_lst_2"], label="Am2")
plt.savefig("chart8.png")
plt.figure()


vals = Am_lst
labels = [str(x) for x in range(1, 16)]  # цикл от 1 до 10 включительно
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)   # стало 10 элементов
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
plt.savefig("chart9.png")
plt.figure()

vals = Am_lst_2
labels = [str(x) for x in range(1, 16)]  # цикл от 1 до 10 включительно
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)  # стало 16 элементов
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
plt.savefig("chart10.png")
plt.figure()

table1 = list(zip(Y, Am_lst))
table2 = list(zip(Y, Am_lst_2))
tframe_am = pd.DataFrame(table1, columns=["Y", "Am_lst"])
plt.bar(tframe1["Y"], tframe1["Am_lst"])
plt.savefig("chart11.png")
plt.figure()

table1 = list(zip(Y, Am_lst))
table2 = list(zip(Y, Am_lst_2))
tframe2_am = pd.DataFrame(table2, columns=["Y", "Am_lst_2"])
plt.bar(tframe2["Y"], tframe2["Am_lst_2"])
plt.savefig("chart12.png")
plt.figure()  # Что происходит вообще здесь?????
# в строке кода 105 в переменную plt передается значение функции plt.figure(), которая создает новую фигуру для построения графиков.


# s1_Tarasenko = os.environ.get('s1_Tarasenko')
# print(s1_Tarasenko)
# s2_Pinchuk = os.environ.get('s2_Pinchuk')
# print(s2_Pinchuk)
# s3_Markin = os.environ.get('s3_Markin')
# print(s3_Markin)


# Задание 1: работал с Тарасенко Кириллом Юрьевичем
# Задание 2: работал c Маркиным Тимофеем Вадимовичем
# Задание 3: Маркин Тимофей Вадимович проверил, всё корректно
# Задание 4: работал с Маркин Тимофеем Вадимовичем


