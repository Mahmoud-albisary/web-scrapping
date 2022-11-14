import requests
from bs4 import BeautifulSoup
import pandas

r = requests.get("https://www.century21.com/real-estate/rock-spring-ga/LCGAROCKSPRING/", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c = r.content
content = BeautifulSoup(c, "html.parser")
all = content.find_all("div", {"class":"property-card-primary-info"})
a = []
for items in all:
    d = {}
    x = items.find("div", {"class":"property-beds"})
    d["price"] = items.find("a", {"class":"listing-price"}).text.replace("\n","").replace(" ", "")
    d["city"] = items.find("div", {"class":"property-city"}).text.replace("\n","").replace(" ","")
    d["address"] = items.find("div", {"class":"property-address"}).text.replace("\n","").replace(" ", "")
    if x != None:
        for items in x.text.replace("\n","").replace(" ", ""):
            try :
                int(items)
                d["beds"] = items
            except:
                pass
    else:
        d["beds"] = "Unknown"
    print(" ")
    a.append(d)
a = pandas.DataFrame(a)
a.to_csv("final.csv", index=False)
print(a)
