import dryscrape
from bs4 import BeautifulSoup

session = dryscrape.Session()
session.visit("https://www.google.ee/search?q=orange+apple&biw=1347&bih=677&source=lnms&tbm=isch&sa=X")
response = session.body()
soup = BeautifulSoup(response, "lxml")
print(soup.find(id="rg_meta"))


