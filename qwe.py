
f = open('a.php','w')
from urllib.request import urlopen
import urllib3.request
from dataclasses import replace
import requests
from bs4 import BeautifulSoup
import sys
keyword =sys.argv[1]
urlA = 'https://www.amazon.in/s?k='+keyword+''
urlF = 'https://www.flipkart.com/search?q='+keyword+''
urlR = 'https://www.reliancedigital.in/search?q='+keyword+''
urlH = 'https://www.happimobiles.com/mobiles/all?serach=&q='+keyword+''
urlL = 'https://www.lotmobiles.com/catalogsearch/result/?q='+keyword+''
urlP = 'https://www.paiinternational.in/SearchResults.aspx?search='+keyword+''
urlB = 'https://www.bajajelectronics.com/product/search?q='+keyword+''

prices = {}
def scrape(url):
    if url == urlF:
        try:
            res = requests.get(url).content
            soup = BeautifulSoup(res, 'html.parser')
            itemF = soup.find_all('div', class_='_4rR01T')
            costF = soup.find_all('div', class_='_30jeq3 _1_WHN1')
            #print(itemF[0].text + " " + costF[0].text)
            costF = costF[0].text[1:]
            prices["Flipkart"] = costF
            fp = "\nData is Retrieved Successfully!!\n"
            fp1 = fp.replace('\n','<br /> ')
            print(fp1)
            fp2 = '<button><a href="' +urlF+'" class="hero-btn">link</a></button>'
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
            costA = soup.find_all('span', class_='a-offscreen')
            #print(itemA[0].text + " " + costA[0].text)
            costA = costA[0].text[1:]
            prices["Amazon"] = costA
            fp="\nData is Retrieved Successfully!!\n"
            fp4=fp.replace('\n','<br />')
            print(fp4)
            fp2 = '<button><a href="' +urlA+'" class="hero-btn">link</a></button>'
            print (fp2)

            
            fp="\n========================================================\n"
            fp4=fp.replace('\n','<br />')
            print(fp4)

        except Exception as e:
            fp="\ndata from amazon is not found\n"
            fp4=fp.replace('\n','<br />')
            print(fp4)
            fp="\n========================================================\n"
            fp1=fp.replace('\n','<br />')
            print(fp1)

    elif url == urlR:
        try:
            res = requests.get(url).content
            soup = BeautifulSoup(res, 'html.parser')
            itemR = soup.find_all('p', class_='sp__name')
            costR = soup.find_all('span', class_='sc-bxivhb cHwYJ')
            #print(itemR[0].text + " " + costR[0].text)
            costR = costR[0].text[1:]
            prices["Reliance"] = costR
            fp="\nData is Retrieved Successfully!!\n"
            fp4=fp.replace('\n','<br />')
            print(fp4)
            fp2 = '<button><a href="' +urlR+'" class="hero-btn">link</a></button>'
            print (fp2)
            fp="\n========================================================\n"
            fp4=fp.replace('\n','<br />')
            print(fp4)
        except Exception as e:
            fp="\ndata from reliance is not found\n"
            fp4=fp.replace('\n','<br />')
            print(fp4)
            fp="\n========================================================\n"
            fp1=fp.replace('\n','<br />')
            print(fp1)

    elif url == urlH:
        try:
            res = requests.get(url).content
            soup = BeautifulSoup(res, 'html.parser')
            itemH = soup.find_all('a', class_='name')
            costH = soup.find_all('div', class_='p-c')
            #print(itemH[0].text + " " + costH[0].text)
            costH = costH[0].text[1:]
            prices["Happi Mobiles"] = costH
            fp="\nData is Retrieved Successfully!!\n"
            fp4=fp.replace('\n','<br />')
            print(fp4)
            fp2 = '<button><a href="' +urlH+'" class="hero-btn">link</a></button>'
            print (fp2)
            
            fp="\n========================================================\n"
            fp4=fp.replace('\n','<br />')
            print(fp4)
        except Exception as e:
            fp="\ndata from Happi mobiles is not found\n"
            fp4=fp.replace('\n','<br />')
            print(fp4)
            fp="\n========================================================\n"
            fp1=fp.replace('\n','<br />')
            print(fp1)

    elif url == urlL:
        try:
            res = requests.get(url).content
            soup = BeautifulSoup(res, 'html.parser')
            itemL = soup.find_all('a', class_='product-item-link')
            costL = soup.find_all('span', class_='price')
            #print(itemL[0].text+ " " + costL[0].text)
            costL = costL[0].text[1:]
            prices["Lot Mobiles"] = costL
            fp="\nData is Retrieved Successfully!!\n"
            fp4=fp.replace('\n','<br />')
            print(fp4)
            fp2 = '<button><a href="' +urlL+'" class="hero-btn">link</a></button>'
            print (fp2)
            fp="\n========================================================\n"
            fp4=fp.replace('\n','<br />')
            print(fp4)
        except Exception as e:
            fp="\ndata from Lot mobiles is not found\n"
            fp4=fp.replace('\n','<br />')
            print(fp4)
            fp="\n========================================================\n"
            fp1=fp.replace('\n','<br />')
            print(fp1)


    elif url == urlB:
        try:
            res = requests.get(url).content
            soup = BeautifulSoup(res, 'html.parser')
            itemB = soup.find_all('h3',class_='prodHeaderDesc mb10')
            costB = soup.find_all('h3', class_='prodPrice d-inline')
            #print(itemB[0].text+ " " + costB[0].text)
            costB = costB[0].text[1:]
            prices["Bajaj"] = costB
            fp="\nData is Retrieved Successfully!!\n"
            fp4=fp.replace('\n','<br />')
            print(fp4)
            fp2 = '<button><a href="' +urlB+'" class="hero-btn">link</a></button>'
            print (fp2)
            fp="\n========================================================\n"
            fp4=fp.replace('\n','<br />')
            print(fp4)
        except Exception as e:
            fp="\ndata from Bajaj is not found\n"
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
    print('connecting to Flipkart.com\n')
    flip=scrape(urlF)
    print('connecting to Amazon.in\n')
    ama=scrape(urlA)
    print('connecting to Reliance\n')
    rel=scrape(urlR)
    print('connecting to happi mobiles\n')
    hap=scrape(urlH)
    print('connecting to Lot Mobiles\n')
    lot=scrape(urlL)
    print('connecting to Bajaj Electronics\n')
    baj=scrape(urlB)
    b=priceComparision()
message = f"""<html>
<head></head>
<body><p></br>Flipkart : {prices["Flipkart"]}</br></p><a href={ama}>Link</a></body>
</html>"""
f.write(message)
f.close()


