from bs4 import BeautifulSoup
import requests
import panda as pd

url = "http://www.gestpymeweb.cl/gestdocu/PAGE_Login/SBAAAFXlRatkZFZFUkp4bW1kAwA"
page = requests.get(url)
soup = BeatifulSoup(page.content, 'html.parser')

#usuarios
user = soup.find_all('td', class_='l-6  wbcolA5 communbc-A5 padding webdevclass-riche')

print (user)
