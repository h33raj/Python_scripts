#Spider for writeups
import webbrowser
import requests
from bs4 import  BeautifulSoup

def trade_spider():
        c=1
	count=0
        while c==1:
                url="https://ctftime.org/writeups"
                source_code=requests.get(url)
                plain_text=source_code.text
                soup=BeautifulSoup(plain_text)
                for link in soup.findAll('table',{'class':'table table-striped'}):
                        for l in link.findAll('a'):
				title=l.string
				href= l.get("href")
                        	if href=='/event/226' or count>0:
					count+=1
					f=l.string
					print f.find('Rev')
					if count==2 and (f.find('rev')>=0 or f.find('Rev')>=0):
						webbrowser.open(url)
						exit(0)
				if count>=2:	
					count=0
		
		exit(0)	
trade_spider()
