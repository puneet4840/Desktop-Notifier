# Scraping Hindi News.
print()

from bs4 import BeautifulSoup
import requests
from newspaper import article


url="https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=52afef4f44314099adb8a2b5841009df"
html=requests.get(url)
bbc=requests.get(url).json()
article=bbc["articles"]
results=[]

for ar in article:
    results.append(ar["title"])

for i in range(len(results)):
    print(i+1,':',results[i])