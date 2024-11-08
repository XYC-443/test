'''3.刚过完双十一，想必大家或多或少的都满足了自己的物欲。小彭是一名人口普查员，由于我国现在人口出生率直线下降，小彭想从消费者身上下手，
看一看近几年母婴用品购买趋势是，他现在有2019和2020年两年的数据，由于小彭近日比较忙，由你来帮小彭按如下要求分析数据。'''
import pandas as pd

'''（1）将两份dataframe进行轴向合并'''

df_2019 = pd.read_csv(r"C:\Users\I\Desktop\Task：数据处理+图形可视化\数据集3\2019年下半年订单表.csv")
df_2020 = pd.read_csv(r"C:\Users\I\Desktop\Task：数据处理+图形可视化\数据集3\2020年上半年订单表.csv")
df_s = pd.concat([df_2019, df_2020], ignore_index=True)

'''（2）使用groupby()函数,将「订单数据表」按「商品ID」进行分组，「按月采样」计算出订单「数量」的和并赋值给dfSales。'''

dfSales = df_s.groupby(['商品ID', pd.to_datetime(df_s['下单时间']).dt.to_period('M')])['数量'].sum().reset_index()

'''（3）还原索引index赋值给dfnewSales并将"下单时间"这列设置成“年-月”的字符串类型并重新赋值给dfnewSales["下单时间"]，处理完数据后保存csv文件'''

dfnewSales = dfSales.copy()
dfnewSales['下单时间'] = dfSales['下单时间'].dt.strftime('%Y-%m')
dfnewSales.to_csv(r"E:\I\feishu\03.csv", index=False)
