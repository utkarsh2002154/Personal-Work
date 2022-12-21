import yfinance as yf
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import linear_model, metrics
import datetime as dt

tic = input("Enter the ticker of the stock: ")
msft = yf.Ticker(tic)
hist = msft.history(period="max")

df = pd.DataFrame(hist)
df.reset_index(level=0, inplace=True)
date1 = df['Date'][0]
df['Days'] = df['Date'].apply(lambda x: (x - date1).days)
df['Days2'] = df['Days'].apply(lambda x: x**2)
df['Days3'] = df['Days'].apply(lambda x: x**3)
train, test = train_test_split(df, test_size=0.2)

x = train[['Days3','Days2', 'Days']]
y = train['Close']

ml = linear_model.LinearRegression()
ml.fit(x, y)

pred = input("Enter the date(DD/MM/YYYY): ")
dt = dt.datetime.strptime(birthday,"%d/%m/%Y").date()
ndt = (dt - date1).days

a = ndt
b = a**2
c = a**3
print(ml.predict([[c,b,a]]))
