from bs4 import BeautifulSoup
import urllib2

response = urllib2.urlopen("https://austin.craigslist.org/search/ata")
html = response.read()
soup = BeautifulSoup(html, "html.parser")
ads_data = soup.find_all("a", class_="result-title")

ads = set(ads_data)

# elem for elem in li if len(elem) > 1 

def contains_chair(s):
  return "chair" in s.string

filtered_ads = filter(contains_chair, ads)

for ad in filtered_ads:
    print ad.string

#result-title hdrlnk