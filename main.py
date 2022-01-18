from pandas_datareader import data as web
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display
from collections import OrderedDict

companies = {
    'WEGE3': 200,
    'TAEE11': 200,
    'EGIE3': 100,
    'ITSA4': 300,   #200
    'MDIA3': 100,
    'GRND3': 400,
    'AERI3': 300,   #200
    'EQTL3': 100    #100
}    #pd.read_excel('file.xlsx')
# amount of shares
# initial price

portfolio = {}

for companie, amount in companies.items():
    shares_price = web.DataReader(f'{companie}.SA', data_source='yahoo', start='01/13/2022', end='01/13/2022')
#    display(shares_price)
    current_price = shares_price['Adj Close'][0] * amount
#    print(f"Companie: {companie} | Price: {current_price:.2f}")
    portfolio[companie] = current_price
#    shares_price['Adj Close'].plot(figsize=(12, 6), title=companie)
#    plt.show()

portfolio_out = OrderedDict(sorted(portfolio.items(), key=lambda t: t[1]))

for companie, price in portfolio_out.items():
    print("{}:  R$ {:.2f}".format(companie, price))

print(portfolio_out)
plt.title('Shares Portfolio')
plt.pie(portfolio_out.values(), labels=portfolio_out.keys(), startangle=90)
plt.show()