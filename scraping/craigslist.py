from bs4 import BeautifulSoup as parser
from urllib.request import urlopen

response = urlopen("https://austin.craigslist.org/search/ata")
html = response.read()
soup = parser(html, "html.parser")
ads_data = soup.find_all("a", class_="result-title")

ads = set(ads_data)

def contains_chair(s):
  return "chair" in s.string

def contains_Chair(s):
  return "Chair" in s.string


filtered_ads_chair = list(filter(contains_chair, ads))
filtered_ads_Chair = list(filter(contains_Chair, ads))

total_chairs = filtered_ads_chair + filtered_ads_Chair

for ad in total_chairs:
    print(ad.string)
