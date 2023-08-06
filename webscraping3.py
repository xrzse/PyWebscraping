from bs4 import BeautifulSoup
import requests

url = 'http://books.toscrape.com/catalogue/category/books_1/index.html'
html = requests.get(url)

soup = BeautifulSoup(html.text, 'lxml')
#Gets all the prices from a single page from a website
prices = soup.find_all('p', attrs={"class":"price_color"}) 
#Loops through the 'li' container and the class and gathers book names by searching for 'h3','a','title'
book_containers = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
book_names = []
for container in book_containers:
    book_name = container.find("h3").find("a")["title"]
    book_names.append(book_name)

for book in book_names:
    print(book)

for t in prices:
    print(t.text)
    
for book, t in zip(book_names, prices):
    print(book +" | Costs: "+ t.text)

