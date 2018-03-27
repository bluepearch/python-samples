# pip  install BeautifulSoup4
    
from bs4 import BeautifulSoup
from urllib.request import urlopen
import random
    
response = urlopen("https://www.meetup.com/Girl-Develop-It-Austin/events/248011477/attendees/")
html = response.read()
    
soup = BeautifulSoup(html, "html.parser")
    
attendees  = soup.find_all("li", class_="attendee-item")
    
attendee_list = []
for attendee in attendees:
  name = attendee.find("h4").get_text()
  attendee_list.append(name)
    
attend_no_dups = set(attendee_list)
    
# remove teachers    
attend_no_dups.remove("Nola S.")
attend_no_dups.remove("Cecy C.")
attend_no_dups.remove("Lenna S.")

# print to see what we have 
#for attendee in attend_no_dups:
#  print(attendee)
     
list1 = random.sample(attend_no_dups, 6)
for attendee in list1:
  print(attendee)
      
