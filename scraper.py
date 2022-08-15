import json
from numpy import product
import requests

products = []
sayac = 0
for page in range(1,99):
    response = requests.get("https://searchpublic.trendyol.com/discovery-sellerstore-websfxsearch-santral/v1/search/products?q=/sr?mid=181490&storefrontId=1&sellerId=181490&pageIndex={}&gender=1".format(page))
    if len(response.text) < 5:
        break
    jsondata = json.loads(response.text)

    for product in jsondata:
        if product == "":           
            break
        products.append(product)
    if sayac != 0:
        break

dosya = open("bas.txt","r",encoding="utf-8")
bas = dosya.read()



dosya2 = open("son.txt","r",encoding="utf-8")
son = dosya2.read()
site = ""
site += bas
for product in products:
    dosya3 = open("urun.txt","r",encoding="utf-8")
    urun = dosya3.read()
    site += urun.format("https://www.trendyol.com/"+product["link"],"https://cdn.dsmcdn.com/mnresize/-/-"+product["image"],product["title"],str(product["price"]["current"])+" TL")
site += son

dosya = open("index.html","a",encoding="utf-8")
dosya.write(site)
