import time
#import pyttsx3
import requests
from binance.client import Client 
import pandas as pa
import talib.abstract as ta
from binance.exceptions import BinanceAPIException
from win32con import SW_HIDE 
import win32gui
from requests.exceptions import ConnectionError
from subprocess import check_output
import subprocess
import win32api



def vpn():
	
	a=check_output('rasdial' , shell=True)
	if 'No' in str(a):
		return(0)
	else:
		return(1)


def connect():
	try:
		a=check_output("netsh wlan show networks" , shell='True')
		
		return(1)
	except:
		return(0)



try:	
	api_key=open('api_key.txt')
	api_secret_key=open('api_secret_key.txt')
	api_key=api_key.readline()
	api_secret_key=api_secret_key.readline()
	print('spider 2  is Already start')
except:
	print('i dont have your a p i key , please tell me')
	while True:

		apikey=input('api key:')
		secretkey=input('secret key:')
		try:
			testclient=Client(apikey , secretkey, {"timeout": 20})
			with open ('api_key.txt' , 'w+') as api:
				api.write(apikey)
				api.close()
			with open ('api_secret_key.txt' , 'w+') as secret:
				secret.write(secretkey)
				secret.close()
			print('your api keys succesfully added ')
			break
		except BinanceAPIException as e:
			if e.status_code=='-2014' or e.message=='API-key format invalid.':
				print('your key is not correct')

			elif e.status_code=='401' or e.message=='Invalid API-key, IP, or permissions for action.':
				print('check your ip')
				print('check your ip')
				time.sleep(6)

			else:
				print("system Out of reach")
				print(e.status_code , ' , the error == ' , e.message)
				time.sleep(6)

		except ConnectionError as c:
			if connect()==0:
				print('your network connection is lost')
				print('your network connection is lost')
				time.sleep(6)
			else:

				print('your network connection is weak ')
				print('your network connection is weak ')
				time.sleep(6)

		except requests.exceptions.Timeout as r:
			if vpn() == 0:
				print('your vpn connection losst')
				print('your vpn connection losst')
				time.sleep(6)
			else:
				print('Binance does not answer')
				print('Binance does not answer')
				time.sleep(6)
		except SyntaxError as sy:
			print(sy.message)
		except NameError as n:
			print('name errore ocured')
			print(n.message)
		
		except:
			print('check the start part in saving the keys')
		


#client entry
while True:
	try:	
		client=Client(api_key , api_secret_key , {"timeout": 20})
		break
	except BinanceAPIException as e:
		if e.status_code=='401' or e.message=='Invalid API-key, IP, or permissions for action.':
			print('check your ip')
			print('check your ip')
			time.sleep(3)
		elif e.message=='Timestamp for this request is outside of the recvWindow.':
			print('Timestamp is wrong')
			
			time.sleep(2)
		else:
			print("system Out of reach")
			print(e.status_code , ' , the error == ' , e.message)
			time.sleep(6)
	except ConnectionError as c:
		if connect()==0:
			print('your network connection is lost')
			print('your network connection is lost')
			time.sleep(6)
		else:

			print('your network connection is weak ')
			print('your network connection is weak ')
			time.sleep(6)

	except requests.exceptions.Timeout as r:
		if vpn() == 0:
			print('your vpn connection losst')
			print('your vpn connection losst')
			time.sleep(6)
		else:
			print('Binance does not answer')
			print('Binance does not answer')
			time.sleep(6)
	except SyntaxError as sy:
		print(sy.message)

	except NameError as n:
		print('name errore ocured')
		print(n.message)

	except:
		print("your device have problem")
		print('error ocure in checking the keys ')
		time.sleep(6)





#crypto list

clist=["ETH",'BNB','ADA',"ENJ",'FET','VET','BCH','LINK','ANKR','DUSK','ALGO','FTM','BTT','UNI','DOT','AVA','WAVES','BEAM','STRAX',
		'LTC','AVAX','ALPHA','TWT','1INCH','KAVA','AKRO','AAVE','AXS','COTI','UNFI','STORJ','CRV','SOL','OCEAN','RSR','HOT','VTHO','XMR','XRP','EOS','IOTA','XLM','ONT','TRX','ICX','CVC',
		'MATIC','TFUEL','XVS','GTO','BLZ','DOGE','NEO','WIN','CAKE','COS','MTL','TOMO','PERL','DENT','NULS','PAX','ONG','ZIL','ZRX','BAT','ZEC','IOST','DASH','NANO','OMG','THETA',
		'MFT','KEY','WAN','MDT','STMX','KNC','REP','LRC','PNT','COMP','SC','ZEN','SNX','FUN','CHZ','BAND',
		'XTZ','REN','RVN','HBAR','NKN','STX','ARPA','IOTX','RLC','CTXC','TROY','VITE','FTT','OGN','DREP','TCT',
		'LSK','BNT','LTO','AION','MBL','STPT','WTC','DATA','CTSI','HIVE','CHR','GXS','ARDR','DGB','GBP','SXP',
		'MKR','DIA','DCR','YFI','YFII','IRIS','KMD','JST','SRM','ANT','SAND','NMR'
		,'WNXM','TRB','KSM','DIA','RUNE','FIO','UMA','BEL','WING','NBS','OXT','SUN','HNT','FLM','ORN',
		'UTK','INJ','HARD','DNT','ROSE','SKL','GRT',
		'REEF','ATM','FIRO','LIT','SFP','ACM','PERP',
		'RAMP']





def ashar(n):
	s=0
	while True:
		if n>1:
			break
		else:
			s+=1
			n=n*10
	return(s)




#counter nmber
def counter(n):
	n//=10
	s=1
	while True:
		if n==0:
			break
		else:
			n//=10
			s+=1
	return(s)




def amount(name):
	name=client.get_asset_balance(name[:-4])
	amount=float(name['free'])
	if amount>1:
		if counter(amount)>=3:

			return(int(amount))
		else:

			if round(amount,1)>amount:
				return(round(amount,1)-0.05)
			else:
				return(round(amount,1))
	else:
		if ashar(amount)>3:
			if round(amount,7)>amount:
				return(round(amount,7)-0.0000005)
			else:
				return(round(amount,7))
		else:
			if round(amount,3)>amount:
				return(round(amount,3)-0.005)
			else:
				return(round(amount,3))



#sellfuncion
def sell(name):
	am=amount(name)
	try:
		print("its time to sell the " + name)
		print("its time to sell the " + name)
		sell=client.order_market_sell(symbol=name , quantity=am)
		print("sell the " + name + str(am) + 'is successfull')
		print("sell the " , name , am , 'is successfull')
	except BinanceAPIException as e:
		if e.status_code=='401' or e.message=='Invalid API-key, IP, or permissions for action.':
			print('check your ip')
			print('check your ip')
			time.sleep(3)
		elif e.message=='Timestamp for this request is outside of the recvWindow.':
			print('Timestamp is wrong')
			
			time.sleep(2)
		else:
			print("system Out of reach")
			print(e.status_code , ' , the error == ' , e.message)
			time.sleep(6)
	except ConnectionError as c:
		if connect()==0:
			print('your network connection is lost')
			print('your network connection is lost')
			time.sleep(6)
		else:
			print('your network connection is weak ')
			print('your network connection is weak ')
			time.sleep(6)

	except requests.exceptions.Timeout as r:
		if vpn() == 0:
			print('your vpn connection losst')
			print('your vpn connection losst')
			time.sleep(6)
		else:
			print('Binance does not answer')
			print('Binance does not answer')
			time.sleep(6)
	except SyntaxError as sy:
		print(sy.message)

	except NameError as n:
		print('name errore ocured')
		print(n.message)
	






#buyfunction
def buy(name,am):
	print("its time to buy the " + name)
	print("its time to buy the " + name)
	try:
		price=client.get_all_tickers()
		for i in range(len(price)):
			if price[i]['symbol']==name:
				pric=float(price[i]['price'])
				if pric>=1:
					if counter(pric)>3:
						pric=pric+2
						pric=int(am/pric)
						buy=client.order_market_buy(symbol=name, quantity=pric)
						print('buying ',am ,'the', name , 'successfull')
						print('buying '+str(am) +'the'+ name + 'successfull')
					elif counter(pric)==3:
						pric=pric+0.1
						pric=round((am/pric),1)
						buy=client.order_market_buy(symbol=name, quantity=pric)
						print('buying ',am ,'the', name , 'successfull')
						print('buying '+str(am) +'the'+ name + 'successfull')
					else:
						pric+=0.01
						pric=round((am/pric),2)
						buy=client.order_market_buy(symbol=name, quantity=pric)
						print('buying ',am ,'the', name , 'successfull')
						print('buying'+str(am) +'the'+ name + 'successfull')
				else:
					if ashar(pric)>=3:
						pric+=0.000003
						pric=int((am/pric))
						buy=client.order_market_buy(symbol=name, quantity=pric)
						print('buying ',am ,'the', name , 'successfull')
						print('buying '+str(am) +'the'+ name + 'successfull')
					else:
						pric+=0.001
						pric=round((am/pric),1)
						buy=client.order_market_buy(symbol=name, quantity=pric)
						print('buying ',am ,'the', name , 'successfull')
						print('buying '+str(am) +'the'+ name + 'successfull')
	except BinanceAPIException as e:
		if e.status_code=='401' or e.message=='Invalid API-key, IP, or permissions for action.':
			print('check your ip')
			print('check your ip')
			time.sleep(3)
		elif e.message=='Account has insufficient balance for requested action.':
			print('cant buy this currency')
			print('cant buy this currency')
			time.sleep(3)
		elif e.message=='Timestamp for this request is outside of the recvWindow.':
			print('Timestamp is wrong')
			
			time.sleep(2)
		else:
			print("system Out of reach")
			print(e.status_code , ' , the error == ' , e.message)
			time.sleep(6)

	except ConnectionError as c:
		if connect()==0:
			print('your network connection is lost')
			print('your network connection is lost')
			time.sleep(6)
		else:

			print('your network connection is weak ')
			print('your network connection is weak ')
			time.sleep(6)

	except requests.exceptions.Timeout as r:
		if vpn() == 0:
			print('your vpn connection losst')
			print('your vpn connection losst')
			time.sleep(6)
		else:
			print('Binance does not answer')
			print('Binance does not answer')
			time.sleep(6)

	
	






















#how many cash i have
def dolors():
	cash=client.get_asset_balance("USDT")
	return(float(cash['free']))



#how much fund in cryptos
def fund():
	print('fund')
	while True:
		try:
			s=0
			crlist={}
			crname=[]
			for i in range(len(clist)):
				nam=clist[i]
				amount=client.get_asset_balance(nam)
				if round(float(amount["free"]),2) != 0:
					price=client.get_all_tickers()
					for i in range(len(price)):
						f=price[i] 
						name=f["symbol"]
						p=f["price"]
						if name == amount["asset"]+"USDT":
							amount2=float(amount["free"]) * float(p)
							amount2=round(amount2,2)
							if amount2 >= 10:
								s+=1
								crlist[name]=amount2
								crname.append(name)
				else:
					time.sleep(2)



			fund=[crlist,crname]
			return(fund)
			break
		except BinanceAPIException as e:
			if e.status_code=='401' or e.message=='Invalid API-key, IP, or permissions for action.':
				print('check your ip')
				print('check your ip')
				time.sleep(3)
			elif e.message=='Timestamp for this request is outside of the recvWindow.':
				print('Timestamp is wrong')
				
				time.sleep(2)
			else:
				print("system Out of reach")
				print(e.status_code , ' , the error == ' , e.message)
				time.sleep(6)
		except ConnectionError as c:
			if connect()==0:
				print('your network connection is lost')
				print('your network connection is lost')
				time.sleep(6)
			else:

				print('your network connection is weak ')
				print('your network connection is weak ')
				time.sleep(6)

		except requests.exceptions.Timeout as r:
			if vpn() == 0:
				print('your vpn connection losst')
				print('your vpn connection losst')
				time.sleep(6)
			else:
				print('Binance does not answer')
				print('Binance does not answer')
				time.sleep(6)
		
	


#bitcheck
def bitcheck():
	print('bitcheck')
	while True:
		try:
			price=client.get_historical_klines('BTCUSDT' , Client.KLINE_INTERVAL_15MINUTE , '10 day ago UTC')
			close=[]
			oPen=[]
			hi=[]
			lo=[]
			vol=[]
			for i in range(len(price)):
				pr=price[i]
				close.append(float(pr[4]))
				oPen.append(float(pr[1]))
				hi.append(float(pr[2]))
				lo.append(float(pr[3]))
				vol.append(float(pr[5]))

			new=pa.DataFrame({'open':oPen,
							'close':close })

			newmfi=pa.DataFrame({'open':oPen,
								'close':close,
								'high' :hi,
								'low' : lo,
								'volume' : vol})

			newmacd1=pa.DataFrame({
							'close':close })
			macd=ta.MACD(newmacd1 , 12 , 26 )
			rsi=ta.RSI(new)
			mfi=ta.MFI(newmfi)

			macd.to_csv("macd.csv",index='False')
			rsi.to_csv('rsi.csv' , index='False')
			mfi.to_csv('mfi.csv' , index='False')
			mfi2=pa.read_csv('mfi.csv')
			macd2=pa.read_csv("macd.csv")
			rsi2=pa.read_csv("rsi.csv")
			mshape=macd2.shape
			rshape=rsi2.shape
			fshape=mfi2.shape
			f=fshape[0]
			ff=mfi2.loc[f-1]
			s=mshape[0]
			m=macd2.loc[s-1]
			sr=rshape[0]
			r=rsi2.loc[sr-1]
			a=[m['macdhist'],r[1],ff[1]]

			if a[0]>0:
				return('+')
				break
			else:
				return('wait')
				break
		except BinanceAPIException as e:
			if e.status_code=='401' or e.message=='Invalid API-key, IP, or permissions for action.':
				print('check your ip')
				print('check your ip')
				time.sleep(3)
			elif e.message=='Timestamp for this request is outside of the recvWindow.':
				print('Timestamp is wrong')
				
				time.sleep(2)
			else:
				print("system Out of reach")
				print(e.status_code , ' , the error == ' , e.message)
				time.sleep(6)

		except ConnectionError as c:
			if connect()==0:
				print('your network connection is lost')
				print('your network connection is lost')
				time.sleep(6)
			else:

				print('your network connection is weak ')
				print('your network connection is weak ')
				time.sleep(6)

		except requests.exceptions.Timeout as r:
			if vpn() == 0:
				print('your vpn connection losst')
				print('your vpn connection losst')
				time.sleep(6)
			else:
				print('Binance does not answer')
				print('Binance does not answer')
				time.sleep(6)


		


def entry():
	clist=["ETH",'BNB','ADA',"ENJ",'FET','VET','BCH','LINK','ANKR','DUSK','ALGO','FTM','BTT','UNI','DOT','AVA','WAVES','BEAM','STRAX',
		'LTC','AVAX','ALPHA','TWT','1INCH','KAVA','AKRO','AAVE','AXS','COTI','UNFI','STORJ','CRV','SOL','OCEAN','RSR','HOT','VTHO','XMR','XRP','EOS','IOTA','XLM','ONT','TRX','ICX','CVC',
		'MATIC','TFUEL','XVS','GTO','BLZ','DOGE','NEO','WIN','CAKE','COS','MTL','TOMO','PERL','DENT','NULS','PAX','ONG','ZIL','ZRX','BAT','ZEC','IOST','DASH','NANO','OMG','THETA',
		'MFT','KEY','WAN','MDT','STMX','KNC','REP','LRC','PNT','COMP','SC','ZEN','SNX','FUN','CHZ','BAND',
		'XTZ','REN','RVN','HBAR','NKN','STX','ARPA','IOTX','RLC','CTXC','TROY','VITE','FTT','OGN','DREP','TCT',
		'LSK','BNT','LTO','AION','MBL','STPT','WTC','DATA','CTSI','HIVE','CHR','GXS','ARDR','DGB','GBP','SXP',
		'MKR','DIA','DCR','YFI','YFII','IRIS','KMD','JST','SRM','ANT','SAND','NMR'
		,'WNXM','TRB','KSM','DIA','RUNE','FIO','UMA','BEL','WING','NBS','OXT','SUN','HNT','FLM','ORN',
		'UTK','INJ','HARD','DNT','ROSE','SKL','GRT',
		'REEF','ATM','FIRO','LIT','SFP','ACM','PERP',
		'RAMP']
	while True:
		try:
			for i in range (len(clist)):
				name=clist[i]+'USDT'
				price=client.get_historical_klines(name , Client.KLINE_INTERVAL_15MINUTE , '1 day ago UTC')
				close=[]
				oPen=[]
				hi=[]
				lo=[]
				vol=[]
				for i in range(len(price)):
					pr=price[i]
					close.append(float(pr[4]))
					oPen.append(float(pr[1]))
					hi.append(float(pr[2]))
					lo.append(float(pr[3]))
					vol.append(float(pr[5]))

				new=pa.DataFrame({'open':oPen,
								'close':close })

				newmfi=pa.DataFrame({'open':oPen,
									'close':close,
									'high' :hi,
									'low' : lo,
									'volume' : vol})

				newmacd1=pa.DataFrame({
								'close':close })

				macd=ta.MACD(newmacd1 , 12 , 26)
				rsi=ta.RSI(new)
				mfi=ta.MFI(newmfi)

				macd.to_csv("macd.csv",index='False')
				rsi.to_csv('rsi.csv' , index='False')
				mfi.to_csv('mfi.csv' , index='False')
				macd2=pa.read_csv("macd.csv")
				rsi2=pa.read_csv("rsi.csv")
				mfi2=pa.read_csv('mfi.csv')
				mshape=macd2.shape
				rshape=rsi2.shape
				fshape=mfi2.shape
				f=fshape[0]
				ff=mfi2.loc[f-1]
				s=mshape[0]
				m=macd2.loc[s-1]
				sr=rshape[0]
				r=rsi2.loc[sr-1]

				a15=[m['macdhist'],r[1],ff[1]]

				if a15[0]>0 and a15[1]<50 and a15[2]<50:
					price=client.get_historical_klines(name , Client.KLINE_INTERVAL_5MINUTE , '1 day ago UTC')
					close=[]
					oPen=[]
					hi=[]
					lo=[]
					vol=[]
					for i in range(len(price)):
						pr=price[i]
						close.append(float(pr[4]))
						oPen.append(float(pr[1]))
						hi.append(float(pr[2]))
						lo.append(float(pr[3]))
						vol.append(float(pr[5]))

					new=pa.DataFrame({'open':oPen,
								'close':close })
			
					newmfi=pa.DataFrame({'open':oPen,
									'close':close,
									'high' :hi,
									'low' : lo,
									'volume' : vol})

					newmacd1=pa.DataFrame({
								'close':close })

					macd=ta.MACD(newmacd1 , 12 , 26)
					rsi=ta.RSI(new)
					mfi=ta.MFI(newmfi)

					macd.to_csv("macd.csv",index='False')
					rsi.to_csv('rsi.csv' , index='False')
					mfi.to_csv('mfi.csv' , index='False')
					macd2=pa.read_csv("macd.csv")
					rsi2=pa.read_csv("rsi.csv")
					mfi2=pa.read_csv('mfi.csv')
					mshape=macd2.shape
					rshape=rsi2.shape
					fshape=mfi2.shape
					f=fshape[0]
					ff=mfi2.loc[f-1]
					s=mshape[0]
					m=macd2.loc[s-1]
					sr=rshape[0]
					r=rsi2.loc[sr-1]

					a5=[m['macdhist'],r[1],ff[1], m['macd'] , m['macdsignal']]

					if a5[0]>0 and a5[1]<50 and a[2]<50:
						money=dolors()
						if money>10:
							macdd=(((a[3]-a[4])/abs(a[3]))*100)
							if macdd > 2 and macdd < 5:
								if ofund(name)<10:
									buy(name , (money-1))
									break
		except BinanceAPIException as e:
			if e.message=='Invalid API-key, IP, or permissions for action.':
				print('check your ip')
				print('check your ip')
				time.sleep(3)
			elif e.message=='Timestamp for this request is outside of the recvWindow.':
				print('Timestamp is wrong')
				
				time.sleep(2)
			else:
				print("system Out of reach")
				print(e.status_code , ' , the error == ' , e.message)
				time.sleep(6)

		except ConnectionError as c:
			if connect()==0:
				print('your network connection is lost')
				print('your network connection is lost')
				time.sleep(6)
			else:

				print('your network connection is weak ')
				print('your network connection is weak ')
				time.sleep(6)

		except requests.exceptions.Timeout as r:
			if vpn() == 0:
				print('your vpn connection losst')
				print('your vpn connection losst')
				time.sleep(6)
			else:
				print('Binance does not answer')
				print('Binance does not answer')
				time.sleep(6)

		
		


def exitpart():
	while True:
		try:
			howmany=fund()
			print(howmany[1][0])
			name=howmany[1][0]

			price=client.get_historical_klines(name , Client.KLINE_INTERVAL_5MINUTE , '1 day ago UTC')
			close=[]
			oPen=[]
			hi=[]
			lo=[]
			vol=[]
			for i in range(len(price)):
				pr=price[i]
				close.append(float(pr[4]))
				oPen.append(float(pr[1]))
				hi.append(float(pr[2]))
				lo.append(float(pr[3]))
				vol.append(float(pr[5]))

			new=pa.DataFrame({'open':oPen,
							'close':close })

			newmfi=pa.DataFrame({'open':oPen,
								'close':close,
								'high' :hi,
								'low' : lo,
								'volume' : vol})

			newmacd1=pa.DataFrame({
							'close':close })

			macd=ta.MACD(newmacd1 , 12 , 26)
			rsi=ta.RSI(new)
			mfi=ta.MFI(newmfi)

			macd.to_csv("macd.csv",index='False')
			rsi.to_csv('rsi.csv' , index='False')
			mfi.to_csv('mfi.csv' , index='False')
			macd2=pa.read_csv("macd.csv")
			rsi2=pa.read_csv("rsi.csv")
			mfi2=pa.read_csv('mfi.csv')
			mshape=macd2.shape
			rshape=rsi2.shape
			fshape=mfi2.shape
			f=fshape[0]
			ff=mfi2.loc[f-1]
			s=mshape[0]
			m=macd2.loc[s-1]
			sr=rshape[0]
			r=rsi2.loc[sr-1]

			a5=[m['macdhist'],r[1],ff[1]]
			

			if a5[0]<0:
				sell(name)
				break
				time.sleep(2)

			else:
				trades = client.get_my_trades(symbol=name)
				
				price=client.get_all_tickers()

				for i in range(len(price)):
					nam=price[i]['symbol']
					if name==nam:
						priCe=flaot(price[i]['price'])
						tp=float(trades[-1])
						darsad=((priCe-tp)/priCe)*100
						if darsad>=0.5:
							sell(name)
							break
				time.sleep(2)




		except BinanceAPIException as e:
			if e.message=='Invalid API-key, IP, or permissions for action.':
				print('check your ip')
				print('check your ip')
				time.sleep(3)
			elif e.message=='Timestamp for this request is outside of the recvWindow.':
				print('Timestamp is wrong')
				
				time.sleep(2)
			else:
				print("system Out of reach")
				print(e.status_code , ' , the error == ' , e.message)
				time.sleep(6)

		except ConnectionError as c:
			if connect()==0:
				print('your network connection is lost')
				print('your network connection is lost')
				time.sleep(6)
			else:

				print('your network connection is weak ')
				print('your network connection is weak ')
				time.sleep(6)

		except requests.exceptions.Timeout as r:
			if vpn() == 0:
				print('your vpn connection losst')
				print('your vpn connection losst')
				time.sleep(6)
			else:
				print('Binance does not answer')
				print('Binance does not answer')
				time.sleep(6)

		
		








while True:
	howmany=fund()
	if len(howmany[1])==0:
		bt=bitcheck()
		if bt=='+':
			entry()
	else:
		exitpart()