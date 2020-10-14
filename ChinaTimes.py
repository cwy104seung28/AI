import requests
from bs4 import BeautifulSoup

url='https://www.chinatimes.com/?chdtv'
r=requests.get(url)

if r.status_code==requests.codes.ok:
    soup=BeautifulSoup(r.text,'html.parser')
    
    titles=soup.find_all("h4",class_ = "title")
    for title in titles:
        print(title.select_one("a").getText())
        print(title.select_one("a").get("href"))
