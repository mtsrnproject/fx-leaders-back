from coinmarketcapapi import CoinMarketCapAPI
import pandas as pa


class getData():

    def __init__(self , type):
        self.type = type

    
    def analyze(self , names , data):
        cleanData = {}

        for i in names:
           cleanData[i] = (data[i])

        print(cleanData)
        new=pa.DataFrame([{'logo' : cleanData }])
        new.to_csv('data.csv' , index=False)


    def geter(self):
        cmc = CoinMarketCapAPI(api_key='f55c4269-15fd-4839-892a-73e2e6ea64fc')

        rep = cmc.cryptocurrency_info(symbol = 'BTC') # See methods below
        # rep2 = cmc.cryptocurrency_info(symbol = 'ETH') # See methods below

        names = []
        names2 = []
        for i in rep.data:
            names.append(i)
        # for i in rep2.data:
        #     names.append(i)
        self.analyze(names , rep.data)
        # self.analyze(names2 , rep2.data)

