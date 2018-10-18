from bs4 import BeautifulSoup
import requests
r = requests.get("https://www.google.com/")

pre = BeautifulSoup(r.text, 'html.parser')

file = open("data.html","w+")
file.write(pre.html.encode('utf-8').strip())
file.close()
