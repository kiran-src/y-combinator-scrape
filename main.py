import requests
from bs4 import BeautifulSoup

website = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(website.text, "html.parser")

print(soup.find(name="a", class_="titlelink"))
website_info = []
for i in soup.find_all(name="a", class_="titlelink"):
    entry = {
        "Title": i.get_text(),
        "URL": i.get("href")
    }
    website_info.append(entry)
#for i in soup.find_all(class_="score"):
#    print(i.get_text())
#    print("A")
a = []
count = 1
for i in soup.find_all(class_="score"):
    print(f"{count}. {i}")
    count+=1
    a.append(i)
print(len(a))
b = []
count = 1
for i in soup.select(selector="tr.athing"):
    print(f"{count}. {i.select('td')[1].select('a[id]')}")
    count+=1
    b.append(i)
print(len(b))