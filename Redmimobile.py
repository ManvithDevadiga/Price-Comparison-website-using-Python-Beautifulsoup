
f = open('a.php','w')
from urllib.request import urlopen
import urllib3.request
from dataclasses import replace
import requests
from bs4 import BeautifulSoup
import sys
keyword = 'REDMI Note 10T 5G '
urlA='https://www.amazon.in/Redmi-Note-Metallic-Dimensity-Processor/dp/B09Q6DPWHH/ref=sr_1_2?crid=2KX5U7TLVE15Z&keywords=Xiaomi+Redmi+Note+10T&qid=1653919948&sprefix=xiaomi+redmi+note+10t%2Caps%2C315&sr=8-2'
urlF = 'https://www.flipkart.com/redmi-note-10t-5g-mint-green-64-gb/p/itm66267253b4a39?pid=MOBGC7QFNGX5K3RE&lid=LSTMOBGC7QFNGX5K3REIVGTIP&marketplace=FLIPKART&q=redmi&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=d521755e-575f-47d8-bb73-77e77e31a4c2.MOBGC7QFNGX5K3RE.SEARCH&ppt=pp&ppn=pp&ssid=2m894a70q80000001653916131374&qH=9b6bf0057c19bd94'
urlR = 'https://www.reliancedigital.in/xiaomi-redmi-note-10t-5g-128-gb-6-gb-ram-mint-green-mobile-phone/p/491997377'
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
            fn1 = fn.replace('\n','<br /> ')
            print(fn1)
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
            fp2 = '<a href="'+urlA+'" class="hero-btn">link</a></button>'
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
    print('\nAmazon.in\n')
    ama=scrape(urlA)
    print('\nReliancedigital.in\n')
    hap=scrape(urlR)
    b=priceComparision()
message = f"""<html>
<head></head>
<body><p></br>Flipkart : {prices["Flipkart"]}</br></p><a href={ama}>Link</a></body>
</html>"""
f.write(message)
f.close()


