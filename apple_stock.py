import requests
import csv
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9"
}

URL = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"


r = requests.get(url=URL, headers=headers)
soup = BeautifulSoup(r.content, "lxml")
table_text = soup.find_all(
    class_="BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)"
)

date = []
open_amt = []
high_amt = []
low_amt = []
close_amt = []
adj_close_amt = []
volume = []
text = []

for items in table_text:
    try:
        if len(items.contents) < 5:
            continue
        else:
            date.append(items.contents[0].string)
            open_amt.append(items.contents[1].string)
            high_amt.append(items.contents[2].string)
            low_amt.append(items.contents[3].string)
            close_amt.append(items.contents[4].string)
            adj_close_amt.append(items.contents[5].string)
            volume.append(items.contents[6].string)
    except IndexError:
        print("Index Error")


for i in range(len(date) - 1):

    text.append(
        [
            date[i],
            open_amt[i],
            high_amt[i],
            low_amt[i],
            close_amt[i],
            adj_close_amt[i],
            volume[i],
        ]
    )

filename = "test-apple-stock.csv"
fieldnames = ["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]
with open(filename, "w", newline="") as csvfile:
    csvwritter = csv.writer(csvfile)
    csvwritter.writerow(fieldnames)
    csvwritter.writerows(text)

if __name__ == "__main__":
    pass
