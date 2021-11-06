import requests
from urllib.parse import urlencode
import json
import time
import pandas as pd

## source "/Users/Anderson/Desktop/PhDwork/Py-Github/venv/bin/activate" 激活虚拟环境
## 自定义函数：
## 当输入股票的id 688396。
## 但是当改变疾病病种时候，需要替换 cookies 与 Data数据

def Get_piao(id=688396):
    import requests
    piao="1."+str(id)

    headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'Accept': '*/*',
        'Referer': 'http://quote.eastmoney.com/basic/h5chart-iframe.html?code=603799&market=1&type=r',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    }

    params = (
        ('fields1', 'f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13'),
        ('fields2', 'f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61'),
        ('beg', '0'),
        ('end', '20500101'),
        ('ut', 'fa5fd1943c7b386f172d6893dbfba10b'),
        ('rtntype', '6'),
        ('secid', piao),
        ('klt', '101'),
        ('fqt', '1'),
        #('cb', 'jsonp1629285089974'),
    )

    response = requests.get('http://push2his.eastmoney.com/api/qt/stock/kline/get', headers=headers, params=params, verify=False)

    # 存储数据
    content = response.text

    if len(content)> 100:
      piao="1."+str(id)
      params = (
        ('fields1', 'f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13'),
        ('fields2', 'f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61'),
        ('beg', '0'),
        ('end', '20500101'),
        ('ut', 'fa5fd1943c7b386f172d6893dbfba10b'),
        ('rtntype', '6'),
        ('secid', piao),
        ('klt', '101'),
        ('fqt', '1'),
        #('cb', 'jsonp1629285089974'),
    )
    else:
      piao="0."+str(id)
      params = (
        ('fields1', 'f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13'),
        ('fields2', 'f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61'),
        ('beg', '0'),
        ('end', '20500101'),
        ('ut', 'fa5fd1943c7b386f172d6893dbfba10b'),
        ('rtntype', '6'),
        ('secid', piao),
        ('klt', '101'),
        ('fqt', '1'),
        #('cb', 'jsonp1629285089974'),
    )

    response = requests.get('http://push2his.eastmoney.com/api/qt/stock/kline/get', headers=headers, params=params, verify=False)

    content = response.text


    Path="/Users/Anderson/Desktop/PhDwork/Py-Github/Piao/"+str(id)+".txt"

    f = open(Path, "w")
    s=content
    f.write(s)
    # 关闭打开的文件，必须关闭不然电脑能炸裂
    f.close()


## 循环

Get_piao(id="399300") 

