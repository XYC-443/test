'''4.小李是一名大厂的码农，今天领导给了他一个数据集，让他分析他们所在公司的视频会员订单情况。
你是他带的实习生，所以这个活不小心落到了你头上，希望你能帮他做好这份工作。该数据集中有一些脏数据需要处理，要求如下：'''

'''（1）首先，我们需要读取文件,并对数据集进行格式转换，把其中单位、数据类型不正确的地方，进行简单处理。'''

import pandas as pd
df = pd.read_csv(r"C:\Users\I\Desktop\培训材料\Task：数据处理+图形可视化\数据集4.csv")

'''（2）快速浏览数据集（df.info()),查看数据的一些基本信息'''

df.info()

'''（3）使用恰当的函数判断缺失值'''

missing_values = df.isnull().sum()

'''（4）对缺失值进行恰当的处理，要求：
方法一使用`drop`函数，将payment_provider这一列缺失值的行删除。再用info()函数进行浏览。
方法二payment_provider这一列缺失值用“wxpay”进行填充，再用drop函数进行浏览'''

df_1 = df.dropna(subset=['payment_provider'])
df_1.info()

'''（5）使用isin()函数判断payment_provider这一列的异常值，若有便将其删除。**注：这一列的值仅限于“wxpay""alipay""applepay",若有其他值，则为异常值'''

allowed_values = ["wxpay", "alipay", "applepay"]
df = df[df['payment_provider'].isin(allowed_values)]

'''（6）将处理后的payment_provider中的种类变为One-hot编码，处理完数据后保存csv文件'''

df_one_hot = pd.get_dummies(df['payment_provider'], prefix='payment')
df = pd.concat([df, df_one_hot], axis=1)
df.drop(['payment_provider'], axis=1, inplace=True)
df.to_csv(r"E:\I\feishu\04.csv", index=False)
