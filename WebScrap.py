

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url='https://www.flipkart.com/search?q=hp%20laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
uclient = uReq(my_url)
page_html = uclient.read()
uclient.close()
page_soup = soup(page_html,"html.parser")

containers = page_soup.findAll("div", {"class":"_3O0U0u"})
#print(len(containers))
#print(soup.prettify(containers[0]))
container = containers[0]
#print(container.div.img["alt"])

F_name="Product Details.csv"
f = open(F_name, "w")
headers="Product,Price,Disc,Selling Price\n"
f.write(headers)

for container in containers:
    Prdct = container.div.img["alt"]
    
    price = container.findAll("div", {"class": "_3auQ3N _2GcJzG"})
    price = price[0].text.strip()
    
    discount = container.findAll("div", {"class":"VGWI6T"})
    discount = discount[0].text
    #strip() removes unnecessary commas and spaces
    sp = container.findAll("div", {"class":"_1vC4OE _2rQ-NK"})
    sp = sp[0].text.strip()
    
    print("PRODUCT:"+Prdct)
    print("PRICE:"+price)
    print("DISC:"+discount)
    print("SELLING PRICE:"+sp+"\n") 
    f.write(Prdct+","+price+","+discount+","+","+sp)
    f.close()
    

    
    
    
    
    
