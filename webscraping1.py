import requests
from bs4 import BeautifulSoup

url =  'https://realpython.github.io/fake-jobs/'
html = requests.get(url)

s = BeautifulSoup(html.content, 'html.parser')

results = s.find(id = 'ResultsContainer')
jobtitle = results.find_all('h2', class_='title is-5')

for job in jobtitle:
    print(job.text) 