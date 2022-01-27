from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = 'https://www.newegg.com/p/pl?N=100007709%204131&Order=3&PageSize=96'

#opening up a connection, grabbing the page
uClient = uReq(my_url)

#store everything read into a variable
page_html = uClient.read()

#close connection
uClient.close()

#does html parsing of the raw html, can be printed with print(page_soup.x)
page_soup = soup(page_html, "html.parser")

#grabs every product
containers = page_soup.findAll("div", {"class":"item-container"})

container = containers[0]


for container in containers:
  
  #Getting the Brand name
  brand_container = container.findAll("a", {"class":"item-brand"})
  brand = brand_container[0].img["title"]
  
  #Gettting the Product name
  product_name = container.a.img["title"]

  #Getting the shipping price
  shipping_container = container.findAll("li", {"price-ship"})
  shipping = shipping_container[0].text.strip()

  #prints the brand, product name, and shipping price
  print("Brand: " + brand)
  print("Product Name: " + product_name)
  print("Shipping Cost: " + shipping)
  print(" ")

