from bs4 import BeautifulSoup
from urllib.request import urlopen
import random

response = urlopen("https://www.meetup.com/Girl-Develop-It-Austin/events/248011477/attendees/")
html = response.read()
#print(html)
soup = BeautifulSoup(html, "html.parser")
attendees = soup.find_all("li", class_="attendee-item")

attendees_list = []
for attendee in attendees:
    name = attendee.find("h4").get_text()
    print(name)
    attendees_list.append(name)

random_winners = random.sample(attendees_list, 4)
print("\n\n\n")
print("And the winners are ... ")

# winners
for winner in random_winners:
    print(winner)
