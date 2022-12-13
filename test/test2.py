from math import log, sqrt, pi, exp
from scipy.stats import norm
from datetime import datetime, date
import numpy as np
import pandas as pd
from pandas import DataFrame
from datetime import datetime, date
import numpy as np
import pandas as pd
import pandas_datareader.data as web
import requests


url = "https://eodhistoricaldata.com/api/options/TSLA.US?api_token=demo&from=2022-10-18&to=2023-09-15"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

df = response.json()
print("------------------",df)
date_price = {}
l = []
for i in range(len(df["data"])):
    call = df["data"][i]["options"]["CALL"]
    for j in call:
        if j["strike"] == 225:
            date_price[j["expirationDate"]] = round(j["lastPrice"])
            l.append(j["lastPrice"])

new_df = pd.DataFrame(date_price, index = [df["lastTradePrice"][0]])

df2 = pd.DataFrame(date_price, index = [0])
df2["lastTradePrice"] =  df["lastTradePrice"][0]
df2
df = df2.copy()

# a = float(input())  // for taking charge range data
a = 120
b = 0-a
x,y = 0,0
p_l =[]
n_l =[]
while round(x,1) != a:
    p_l.append(round(x+(a/10),1))
    x = round(x+(a/10),1)
while round(y,1) != b:  
    if round(y+(b/10),1) <= -100.0:
        n_l.append(-100.0)
        break
    n_l.append(round(y+(b/10),1))
    y = round(y+(b/10),1)


p = []
n = []
for i in p_l:
    a = (df2 * (100+i))/100
    p.append(a)
for a in p:
    df2 = df2.append(a,ignore_index = True)
    df3 = df2.iloc[::-1]
for i in n_l:
    b = (df * (100+i))/100
    n.append(b)
for c in n:
    df3 = df3.append(c, ignore_index=True)
df3.style.hide_index()
df3.insert(0, ' ', df3.pop('lastTradePrice'))

context={
    "columns": df3.to_html()
}