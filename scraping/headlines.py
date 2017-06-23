from bs4 import BeautifulSoup
import urllib2


response = urllib2.urlopen("http://www.kxan.com")
html = response.read()
soup = BeautifulSoup(html, "html.parser")
headlines = soup.find_all("h1", class_="entry-title")

for headline in headlines:
    print headline.string

    
