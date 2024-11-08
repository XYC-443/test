import matplotlib.pyplot as plt;   '''引用matplotlib.pyplot库(画图)，之后简称为plt'''
import pandas as pd
import datetime

df = pd.read_csv(r"C:\Users\I\Desktop\培训材料\Task：数据处理+图形可视化\数据集1.csv")
plt.figure(figsize=(10000, 50), dpi=50)
plt.rcParams['font.sans-serif'] = ['SimHei']
c = df['Date']

x = []
for i in range(0, 188):
    x.append(datetime.datetime.strptime(c[i], '%Y/%m/%d'))
a = df['Deaths']
b = df['Confirmed']
result = a/b

y = []
for i in range(0, 188):
    y.append(result[i])

plt.xlabel('日期', fontsize=30)
plt.ylabel('死亡率', fontsize=30)
plt.title('2020年1月22日至2020年7月27日病毒死亡率走势', fontsize=50)
plt.plot(x, y, color='orange', marker='o', label='每日死亡率')
plt.show()