import requests
from bs4 import BeautifulSoup

data = {"Host": "www.google.com","User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0","Accept": "image/png,image/*;q=0.8,*/*;q=0.5",
"Accept-Language": "en-US,am;q=0.7,zh-HK;q=0.3","Accept-Encoding": "gzip, deflate","Referer": "https://www.google.com","Cookie": "PREF=ID=1111111111111111:FF=0:LD=en:CR=2:TM=1439993585:LM=1445565646:V=1:S=cGak3Dk6YKLPadm7; NID=72=Kd8i3KUAz64m6HZ9YDGnSAXDTGzj5YOqDuEIq52mLqcOwyyp4LXeUfoK_S76eoOys8GQu0k26e7DCMj2N48l75-mdQDKXzLghZPQMzPGiYH7wt4yVAVDjJ4WrGba5VhogYWnEoDVb3IJbcRJgAxkS29vEYFQGxOkZ_PGtvrFWg_5oR9rbc1XNysRIS0rZGTgBkI0L-FwD-tJSqvHS7R4zKMbxfCZv9u0pIeFbA; OGP=-5061451:","Connection": "keep-alive"}
def get_pic(search):
    img_urls = []
    try:
        res = requests.get("https://www.google.com/search?site=imghp&tbm=isch&source=hp&biw=1366&bih=648&q=" + search,params=data)
        soup = BeautifulSoup(res.content,'html.parser')
	print(soup)
        for link in soup.find_all("img"):
            img = link.get('src')
            print(img)

    except:
        print "error"

get_pic("Orange Apple")
