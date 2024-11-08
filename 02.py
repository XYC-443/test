'''2.小瑶是一家酒店的董事长，由于她对计算机行业相当感兴趣，想借助计算机来解决财务上的问题，目前正在自学数据处理的相关知识，她现在有问题难住了，
所以想求助计算机专业毕业的你，现在你帮她解决一下吧。'''

'''（1）使用numpy中的随机函数创建一个csv图表，图表一共分为5列10000行，
各列名称依次为:index, count,  class,  normal_distribution, 0-1,
分别代表     :序号，  统计数据，类别，   正态分布数据，          0-1数据，
其中count的数据范围在0-10000，class的数据范围为[1,2,3,4,5],
normal_distribution的数据范围为0-10000，0-1的数据范围为[0,1]，将创建的csv保存'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = {'index': np.arange(1, 10001),
        'count': np.random.randint(0, 10001, size=10000),
        'class': np.random.choice([1, 2, 3, 4, 5], size=10000),
        'normal_distribution': np.random.normal(0, 10000, 10000),
        '0-1': np.random.rand(10000)}
df = pd.DataFrame(data)
df.to_csv(r"E:\I\feishu\02.csv")

'''（2）从创建的图表里读取数据，根据normal_distribution列画出画出正态分布的图像'''


plt.figure(figsize=(10, 5))
plt.hist(df['normal_distribution'], bins=100)
plt.xlabel('x')
plt.ylabel('y')
plt.title('normal_distribution')
plt.show()

'''（3）从创建的图表里读取数据，根据class列中各类的数量画饼图，并标注各类占比'''

class_counts = df['class'].value_counts()
plt.figure(figsize=(5, 5))
plt.pie(class_counts, labels='class', autopct='%1.1f%%', startangle=60)
plt.title('class_distribution')
plt.savefig(r"D:\python project\ATrain\机械学习\matplotlab图像")
plt.show()

'''（4）从创建的图表离读取数据，根据class和count列画出柱状图，其中y轴为各类的数值（对应count列）总和，x轴为类名称，并在各柱上方标注值'''

class_count_sum = df.groupby('class')['count'].sum()
plt.figure(figsize=(10, 5))
plt.bar(class_count_sum.index, class_count_sum, color='orange')
plt.xlabel('Class')
plt.ylabel('Count sum')
plt.title('count sum of the class')
for i, v in enumerate(class_count_sum):
        plt.text(i+1, v+50, str(v), ha='center', va='bottom')
plt.show()

'''（5）从创建的图表离读取数据，根据count列画出各阶段分布直方图，均分为十段'''

plt.figure(figsize=(10, 5))
plt.hist(df['count'], bins=10)
plt.xlabel('count')
plt.ylabel('y')
plt.show()

'''（6）从创建的图表离读取数据，根据0-1列和class列模拟出各场红蓝对决比赛中人们的支持'''

support_rates = df.groupby('class')['0-1'].mean()
plt.figure(figsize=(10, 5))
plt.bar(support_rates.index, support_rates, color=('red', 'blue', 'red', 'blue', 'red'))
plt.xlabel('Class')
plt.ylabel('Support rate')
plt.title('Support rates')
for i, v in enumerate(support_rates):
        plt.text(i+1, v+0.01, f'{v:.2f}', ha='center', va='bottom')
plt.show()