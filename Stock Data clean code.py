import pandas as pd
import numpy as np
import json  

# load data
f =open('/Users/Anderson/Desktop/PhDwork/Github-New/Stock_github/603260.txt',encoding='utf-8') #打开‘product.json’的json文件
res=f.read()  #读文件
print(json.loads(res))#把json串变成python的数据类型：字典   


a=json.loads(res)
type(a)# a里面包含字典信息；字典信息里面的data存储了股票每天的股价信息

# extract data
y=a['data'] 
xx=y['klines']# 股票每天的股价信息
type(xx)


#现在将list信息转成 Pd dataframe
df=pd.DataFrame(y)
df

#现在将 pd dataframe 的字符串分列
df=pd.DataFrame(y)
df[['time','kaipan','shoupan','max','min','percentage','percentage_value','volume','money','amplitude','turnover']]=df['klines'].str.split(',', expand=True)
print(df.tail())

#save data

stockname=df['code']
x= stockname.drop_duplicates()
print(x)
#xx.to_csv()

df.to_csv(x[0]+'.csv')






