from datetime import timezone
from datetime import datetime
import time
from kucoin.client import Client
import requests
import pandas as pa
# import talib.abstract as ta
from requests.exceptions import ConnectionError
from kucoin.exceptions import KucoinAPIException



client = Client('6158278d2f6d5200017ba661','04b4c178-f05a-4c4a-9461-b400fafa35b3','Mireh1230098')

def Time():
	t=time.localtime()
	if t[1] == 1:
		if t[2] == 2:
			dt = datetime(t[0]-1 , 12 , 30 , t[3])
			thattime = (dt - datetime(1970 , 1 , 1)).total_seconds()
			nowtime=time.time() 
			return([thattime , nowtime])
		elif t[2] == 1:
			dt = datetime(t[0]-1 , 12 , 29 , t[3])
			thattime = (dt - datetime(1970 , 1 , 1)).total_seconds()
			nowtime=time.time() 
			return([thattime , nowtime])

		else:
			dt = datetime(t[0]-1 , 12 , (t[2]-2) ,t[3])
			thattime = (dt - datetime(1970 , 1 , 1)).total_seconds()
			nowtime=time.time() 
			return([thattime , nowtime])


	else:
		if t[2] == 2:
			dt = datetime(t[0] , t[1]-1 , 30 , t[3])
			thattime = (dt - datetime(1970 , 1 , 1)).total_seconds()
			nowtime=time.time() 
			return([thattime , nowtime])
		elif t[2] == 1:
			dt = datetime(t[0] , t[1]-1 , 29 , t[3])
			thattime = (dt - datetime(1970 , 1 , 1)).total_seconds()
			nowtime=time.time() 
			return([thattime , nowtime])

		else:
			dt = datetime(t[0] , t[1] , (t[2]-2) ,t[3])
			thattime = (dt - datetime(1970 , 1 , 1)).total_seconds()
			nowtime=time.time() 
			return([thattime , nowtime])




def datamaker():
	Clist2 = []
	datadic = {}
	while True:
		try:
			
			print('part 1')
			clist =['BTC','ETH','LINK','UNI','YFI','EOS','DOT','FIL','ADA','LTC','GRT','SUSHI','1INCH',
			'DASH','AAVE','VET','BNB','SXP','SOL','CRV','ALGO','AVAX','FTM','MATIC','THETA','ATOM','KSM','LUNA','VET','BNB','SXP','SOL','CRV','ALGO','AVAX','FTM','MATIC','THETA','ATOM',
			'CHZ','ENJ','MANA','OCEAN','BAT','SNX','NEO','ONT','XMR','COMP','WAVES','BAND','MKR',
			'DGB','AXS','ALICE','NEAR','SAND','TLM']
			'''
                                 ,'KSM','LUNA','VET','BNB','SXP','SOL','CRV','ALGO','AVAX','FTM','MATIC','THETA','ATOM',
			'CHZ','ENJ','MANA','OCEAN','BAT','SNX','NEO','ONT','XMR','COMP','WAVES','BAND','MKR',
			'RVN','DGB','AXS','ALICE','NEAR','SAND','TLM']
                        '''
			for i in clist:
				if i not in Clist2:
					time.sleep(1)
					name = i					
					T=Time()
					price=client.get_kline_data(name+'-USDT', '1hour' , int(T[0]))

					

					

					close=[]

					for i in price:
						close.append(i[2])
						if len(close) == 44:
							break

					close.reverse()
					


					new=pa.DataFrame({'close':close })


					rsi = ta.RSI(new)

					rsi.to_csv('rsi.csv' , index = 'False')

					new.to_csv('price.csv')

					rsi2=pa.read_csv("rsi.csv")

					Price = pa.read_csv('price.csv')


					priceshape = Price.shape

					rsishape = rsi2.shape



					rsilist = []
					pricelist = []


					for i in range(14 , rsishape[0]):
						r = rsi2.loc[i]
						s = Price.loc[i]
						rsilist.append(r[1])
						pricelist.append(s[1])




					datadic[name] = [pricelist , rsilist] 
					Clist2.append(name)
					print(f'{name}s data made ')
			print(len(datadic))
			print(len(clist))
			return(datadic)
			break
			

		except KucoinAPIException as e:
					print(e.message)




def tahlil(data):
	while True:
		ttime = time.localtime()			
		if ttime[4] == 29 and ttime[5] >= 30:
			print('part 2')	
			clist2=[]
			while True:
				clist=['BTC','ETH','LINK','UNI','YFI','EOS','DOT','FIL','ADA','LTC','GRT','SUSHI','1INCH',
			'DASH','AAVE','VET','BNB','SXP','SOL','CRV','ALGO','AVAX','FTM','MATIC','THETA','ATOM','KSM','LUNA','VET','BNB','SXP','SOL','CRV','ALGO','AVAX','FTM','MATIC','THETA','ATOM',
			'CHZ','ENJ','MANA','OCEAN','BAT','SNX','NEO','ONT','XMR','COMP','WAVES','BAND','MKR','DGB','AXS','ALICE','NEAR','SAND','TLM']

			
				try:
					tt = time.localtime()
					for i in clist:
						if i not in clist2:
							name = i
							T=Time()

							price=client.get_kline_data(name+'-USDT', '1hour' , int(T[0]))


							price.reverse()

							close=[]

							for i in price:
								close.append(i[2])


							new=pa.DataFrame({'close':close })


							rsi = ta.RSI(new)

							rsi.to_csv('rsi.csv' , index = 'False')

							new.to_csv('price.csv')

							rsi2=pa.read_csv("rsi.csv")
							Price = pa.read_csv('price.csv')


							priceshape = Price.shape

							rsishape = rsi2.shape

							newprice = Price.loc[priceshape[0]-1][1]
							newrsi = rsi2.loc[rsishape[0]-1][1]

							PP=data[name][0]
							RR=data[name][1]

							minprice = min(PP)
							maxprice = max(PP)

							


							if newprice > maxprice and newrsi < RR[PP.index(maxprice)]:
								if (RR[PP.index(maxprice)] - newrsi ) > 2:
									print(f'its time to buy {name} , short')
									print(f'pos == candel {tt[3]}')
									print(f'newrsi = {newrsi}  ,  newprice = {newprice}')
									print(f'maxrsi = {RR[PP.index(maxprice)]} , minrsi = {RR[PP.index(minprice)]} , maxprice = {maxprice} , minprice = {minprice}')
									print('===========================')
								

							elif newprice < minprice and newrsi > RR[PP.index(minprice)]:
								if (newrsi -  RR[PP.index(minprice)]) > 2:
									print(f'its time to buy {name} , long')
									print(f'pos == candel {tt[3]}')
									print(f'newrsi = {newrsi}  ,  newprice = {newprice}')
									print(f'maxrsi = {RR[PP.index(maxprice)]} , minrsi = {RR[PP.index(minprice)]} , maxprice = {maxprice} , minprice = {minprice}')
									print('==========================')


							
								


							clist2.append(name)
							PP.remove(PP[0])
							RR.remove(RR[0])
							PP.append(newprice)
							RR.append(newrsi)


							data[name] = [PP , RR]

							time.sleep(2)
							
					break

					
					

				except KucoinAPIException as e:
					print(e.message)





a = datamaker()

tahlil(a)
