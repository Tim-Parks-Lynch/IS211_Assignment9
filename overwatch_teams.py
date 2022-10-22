# This is a video game that I play, and these are
# international teams that are sponsored by real companies who pay
# the players.

# URL being scrapped: https://en.wikipedia.org/wiki/Overwatch_League

import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Overwatch_League"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9"
}


def main():
    r = requests.get(url=URL, headers=HEADERS)
    soup = BeautifulSoup(r.content, "lxml")
    tbody = soup.select("td")

    new_table = []
    for i in range(16, 115):

        if i % 5 == 2:
            new_table.append(tbody[i].contents[2].string.strip())
        else:
            new_table.append(tbody[i].contents[0].string.strip())

    del new_table[4::5]

    print(
        f"Team Name: {new_table[0]}, Location: {new_table[1]}, Joined: {new_table[2]}, Owned: {new_table[3]}"
    )
    print(
        f"Team Name: {new_table[4]}, Location: {new_table[5]}, Joined: {new_table[6]}, Owned: {new_table[7]}"
    )
    print(
        f"Team Name: {new_table[8]}, Location: {new_table[9]}, Joined: {new_table[10]}, Owned: {new_table[11]}"
    )
    print(
        f"Team Name: {new_table[12]}, Location: {new_table[13]}, Joined: {new_table[14]}, Owned: {new_table[15]}"
    )
    print(
        f"Team Name: {new_table[16]}, Location: {new_table[17]}, Joined: {new_table[18]}, Owned: {new_table[19]}"
    )
    print(
        f"Team Name: {new_table[20]}, Location: {new_table[21]}, Joined: {new_table[22]}, Owned: {new_table[23]}"
    )


if __name__ == "__main__":
    main()
