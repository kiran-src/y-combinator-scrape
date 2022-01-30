import requests
from bs4 import BeautifulSoup

website = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(website.text, "html.parser")

print(soup.find(name="a", class_="titlelink"))
website_info = []

for i in soup.find_all(name="a", class_="titlelink"):
    entry = {
        "Title": i.get_text(),
        "URL": i.get("href"),
        "Score": 0
    }
    website_info.append(entry)

score_entry = soup.find_all(class_="subtext")

for i in range(len(website_info)):
    if score_entry[i].find(class_='score') is None:
        website_info[i]["Score"] = 0
    else:
        website_info[i]["Score"] = int(score_entry[i].find(name='span', class_='score').get_text().split()[0])
print(website_info)

