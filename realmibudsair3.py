f = open('a.php','w')
from urllib.request import urlopen
import urllib3.request
from dataclasses import replace
import requests
from bs4 import BeautifulSoup
import sys
keyword = 'realmi buds air 3'
urlF='https://www.flipkart.com/realme-buds-air-3-fast-charge-active-noise-cancellation-anc-bluetooth-headset/p/itm89d3851d0df2a?pid=ACCGCPJ6WBGDDGHT&lid=LSTACCGCPJ6WBGDDGHT7UFJIN&marketplace=FLIPKART&q=realme+buds+air+3&store=0pm%2Ffcn&spotlightTagId=BestsellerId_0pm%2Ffcn&srno=s_1_3&otracker=AS_QueryStore_OrganicAutoSuggest_2_10_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_10_na_na_na&fm=search-autosuggest&iid=d0e4f594-cb01-4be0-bc7e-5a6131ecbd28.ACCGCPJ6WBGDDGHT.SEARCH&ppt=sp&ppn=sp&ssid=32zqlu98b40000001653966186798&qH=2f03e3297acfee30'
urlA = 'https://www.91mobiles.com/realme-buds-air-3-in-ear-canalphone-headphones-price-in-india'
f12 = 'https://www.amazon.in/realme-Earphone-Waterproof-Transparency-Cancellation/dp/B09B9GPZVS/ref=sr_1_14?keywords=realme%2Bbuds%2Bair%2B3&qid=1653966317&sr=8-14&th=1'
urlR = 'https://www.reliancedigital.in/realme-buds-air-3-rma2105-wireless-earphone-starry-blue/p/492796886'
prices = {}
a=f'Showing results for : {keyword} in different sites\n'
b="\n"+a+"\n"
fp4=b.replace('\n','<br />')
print(fp4)
def scrape(url):
    if url == urlF:
        try:
            res = requests.get(url).content
            soup = BeautifulSoup(res, 'html.parser')
            itemF = soup.find_all('div', class_='_4rR01T')
            costF = soup.find_all('div', class_='_30jeq3 _16Jk6d')
            #print(itemF[0].text + " " + costF[0].text)
            costF = costF[0].text[1:]
            prices["Flipkart"] = costF
            fp = "\nData is Retrieved Successfully!!\n"
            fp1 = fp.replace('\n','<br /> ')
            print(fp1)
            print(costF)
            fn = "\n"
            fp2 = '<a href="' +urlF+'" class="hero-btn">link</a></button>'
            print (fp2)
            
            fp="\n========================================================\n"
            fp1=fp.replace('\n','<br />')
            print(fp1)

        except Exception as e:
            fp3="\ndata from Flipkart is not found\n"
            fp4=fp3.replace('\n','<br />')
            print(fp4)
            fp="\n========================================================\n"
            fp1=fp.replace('\n','<br />')
            print(fp1)

    elif url == urlA:
        try:
            res = requests.get(url).content
            soup = BeautifulSoup(res, 'html.parser')
            itemA = soup.find_all('span', class_='a-size-medium a-color-base a-text-normal')
            costA = soup.find_all('span', class_='store_prc')
            #print(itemA[0].text + " " + costA[0].text)
            costA = costA[0].text[1:]
            prices["Amazon"] = costA
            fp="\nData is Retrieved Successfully!!\n"
            fp4=fp.replace('\n','<br />')
            print(fp4)
            print(costA)
            fp2 = '<a href="' +f12+'" class="hero-btn">link</a></button>'
            print (fp2)

            
            fp="\n========================================================\n"
            fp4=fp.replace('\n','<br />')
            print(fp4)

        except Exception as e:
            fp="\ndata from Amazon is not found\n"
            fp4=fp.replace('\n','<br />')
            print(fp4)
            fp="\n========================================================\n"
            fp1=fp.replace('\n','<br />')
            print(fp1)

    elif url == urlR:
        try:
            res = requests.get(url).content
            soup = BeautifulSoup(res, 'html.parser')
            itemH = soup.find_all('a', class_='name')
            costR = soup.find_all('span', class_='pdp__offerPrice')
            #print(itemH[0].text + " " + costH[0].text)
            costR = costR[0].text[1:]
            prices["Reliance Digital"] = costR
            fp="\nData is Retrieved Successfully!!\n"
            fp4=fp.replace('\n','<br />')
            print(fp4)
            print(costR)
            fp2 = '<a href="' +urlR+'" class="hero-btn">link</a>'
            print (fp2)
            
            fp="\n========================================================\n"
            fp4=fp.replace('\n','<br />')
            print(fp4)
        except Exception as e:
            fp="\ndata from Reliance Digital is not found\n"
            fp4=fp.replace('\n','<br />')
            print(fp4)
            fp="\n========================================================\n"
            fp1=fp.replace('\n','<br />')
            print(fp1)
def priceComparision():
    a=f'Showing results for : {keyword} in different sites'
    b="\n"+a+"\n"
    fp4=b.replace('\n','<br />')
    print(fp4)
    
    for item in prices.items():
      a=item[0],":",item[1]
      fp="\n"+item[0]+":"+item[1]+"\n"
      fp4=fp.replace('\n','<br />')
      print(fp4)
        
if __name__ == '__main__':
    print('\nFlipkart.com\n')
    flip=scrape(urlF)
    print('Amazon.in\n')
    ama=scrape(urlA)
    print('Reliance Digital.in\n')
    hap=scrape(urlR)
    b=priceComparision()
message = f"""<html>
<head></head>
<body><p></br>Flipkart : {prices["Flipkart"]}</br></p><a href={ama}>Link</a></body>
</html>"""
f.write(message)
f.close()