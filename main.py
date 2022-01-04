from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

my_url = 'https://www.reddit.com/r/IdiotsInCars/top/'

#opening up and grabbing page
uClient = urlopen(my_url)

page_html = uClient.read()

#close client
uClient.close()

#does html parsing
page_soup = soup(page_html, "html.parser")

#grabs every post
containers = page_soup.findAll("div", {"class":"_1oQyIsiPHYt6nx7VOmd1sz _1RYN-7H8gYctjOQeL8p2Q7 scrollerItem _3Qkp11fjcAw9I9wtLo8frE _1qftyZQ2bhqP62lbPjoGAh"})

print("I couldn't figure out how to get my code to work, but at least I tried. Look through my version history for my attempts")
