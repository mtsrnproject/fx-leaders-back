from coinmarketcapapi import CoinMarketCapAPI
import pandas as pa
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import time



class getData():

    def __init__(self , type):
        self.type = type

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'e0f2c46f-e46c-4f73-ab5d-a8fd983704ca',
    }


    def analyze(self , data):
        cleanData = data

        
        # print(cleanData)
        price = []
        name = []
        percent_24 = []
        percent_1=[]
        for i in data:
            name.append(i['symbol'])
            price.append(i['quote']['USD']['price'])
            percent_24.append(i['quote']['USD']['percent_change_24h'])
            percent_1.append(i['quote']['USD']['percent_change_1h'])
            # time.sleep(1)
            # print(name , price)
        
        new=pa.DataFrame({ 'name' : name , 
                          'price' : price,
                           'prcent_change_1H' : percent_1,
                            'percent_change_24H' : percent_24 })
        new.to_csv('data.csv' , index=True)


    def geter(self):
        session = Session()
        session.headers.update(self.headers)

        try:
            response = session.get(self.url)
            data = json.loads(response.text)
            print(data['data'])
            self.analyze(data['data'])
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

