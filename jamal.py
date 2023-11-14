import requests
import webbrowser
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_Internet_top-level_domains"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

table = soup.find_all("table", {"class": "wikitable"})

tlds = []

for i in range(0, len(table)):
    rows = table[i].find_all("tr")
    for row in rows:
        tld = row.find("td")
        if tld:
            tlds.append(tld.text.strip())


print(tlds)

nome = "jamal"

abrir = False

for tld in tlds:
    url = "https://" + nome + tld
    print(url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("O domínio existe")
            if abrir:
                webbrowser.open(url)
    except:
        print("O domínio não existe")

