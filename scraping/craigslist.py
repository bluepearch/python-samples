from bs4 import BeautifulSoup as parser
from urllib.request import urlopen

response = urlopen("https://austin.craigslist.org/search/ata")
html = response.read()
soup = parser(html, "html.parser")
ads_data = soup.find_all("a", class_="result-title")

ads = set(ads_data)

def contains_chair(s):
  return ("chair" in s.string) or ("Chair" in s.string)

filtered_ads_chair = list(filter(contains_chair, ads))


for ad in filtered_ads_chair:
    print(ad.string)
