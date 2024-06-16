import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.codewithtomi.com/")

soup = BeautifulSoup(res.content, "html.parser")

s = soup.find_all("p", class_="post-snippet") 
for data in s:
    print(data.text)