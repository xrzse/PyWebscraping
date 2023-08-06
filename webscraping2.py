import requests
from bs4 import BeautifulSoup

url =  'https://quotes.toscrape.com/'
html = requests.get(url)

soup = BeautifulSoup(html.text, 'html.parser')
##span is the tag that all quotes in the website have in html
quotes = soup.find_all("span", attrs={"class":"text"})
authors = soup.find_all("small", attrs={"class":"author"})

for quote, author in zip(quotes, authors):
    print(quote.text + "-" + author.text)
