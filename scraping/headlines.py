from bs4 import BeautifulSoup
from urllib.request import urlopen


response = urlopen("http://www.kxan.com")
html = response.read()
soup = BeautifulSoup(html, "html.parser")
headlines = soup.find_all("h1", class_="entry-title")

headlines_set = set(headlines)

for headline in headlines_set:
    print(headline.string)
