import requests
from bs4 import BeautifulSoup


url='https://www.youtube.com/results?search_query=Travis+scott+Happy+english+song'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html5lib')

a=soup.find('id',attrs={'class':' style-scope ytd-item-section-renderer style-scope ytd-item-section-renderer'})

print(a)