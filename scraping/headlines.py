from bs4 import BeautifulSoup
from urllib.request import urlopen


response = urlopen("http://www.kxan.com")
html = response.read()
#print(html)
soup = BeautifulSoup(html, "html.parser")
headlines = soup.find_all("h4", class_="headline")
#print(headlines)
headlines_set = set(headlines)

for headline in headlines_set:
    print(headline.get_text().strip())
