from coinmarketcapapi import CoinMarketCapAPI
import pandas as pa
# from requests import Request, Session
import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import time



class getFiatData():

    def __init__(self , type):
        self.type = type

    url = "https://api.fastforex.io/fetch-all?api_key=ad56a856a7-70cd72b506-sffdfc"
    headers = {
    "Accepts": "application/json",
    # 'X-CMC_PRO_API_KEY': 'e0f2c46f-e46c-4f73-ab5d-a8fd983704ca',
    }


    def analyze(self , data):
        cleanData = data

        
        # print(cleanData)
        # price = []
        name = []
        sign = []
        symbol=[]
        for i in data:
            name.append(i['name'])
            sign.append(i['sign'])
            symbol.append(i['symbol'])
            # percent_1.append(i['quote']['USD']['percent_change_1h'])
            # time.sleep(1)
            # print(name , price)
        
        new=pa.DataFrame({ 'name' : name , 
                          'sign' : sign,
                           'symbol' : symbol,
                             })
        new.to_csv('fiat.csv' , index=False)


    def geter(self):
        # session = Session()
        # session.headers.update(self.headers)

        try:
            # response = session.get(self.url )
            response = requests.get(self.url, headers=self.headers)
            # data = json.loads(response.text)
            print(response.text)
            # self.analyze(data['data'])
            # names2 = []
            # for i in data['data']:
                # print(i)
                # time.sleep(2)
                # data.append(i)        # append the every currency data in list for dataFrame 
            # print(data)
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)
        # cmc = CoinMarketCapAPI(api_key='e0f2c46f-e46c-4f73-ab5d-a8fd983704ca')

        # rep = cmc.cryptocurrency_quotes_historical() # See methods below
        # # rep2 = cmc.cryptocurrency_info(symbol = 'ETH') # See methods below

       
        # self.analyze(names2 , rep2.data)

