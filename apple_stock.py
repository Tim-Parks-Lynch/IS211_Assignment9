import requests
from bs4 import BeautifulSoup

URL = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9"
}


def main():
    r = requests.get(url=URL, headers=HEADERS)
    soup = BeautifulSoup(r.content, "lxml")
    table_text = soup.find_all(
        class_="BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)"
    )

    for item in table_text:
        try:
            if len(item.contents) < 5:
                continue
            else:
                print(
                    f"Date: {item.contents[0].string} Close: {item.contents[4].string}"
                )
        except IndexError:
            print("Index Error")


if __name__ == "__main__":
    main()
