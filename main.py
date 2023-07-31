from bs4 import BeautifulSoup
import requests
from pprint import pprint
request = requests.get("https://kworb.net/spotify/artist/7hJcb9fa4alzcOq3EaNPoG_songs.html").text

soup = BeautifulSoup(request, "html.parser")

total = 0

for n in range(194):
    one = soup.select_one(f".addpos tbody tr:nth-child({n+1}) td:nth-child(3)").text.replace(",", "")
    try:
        one_int = int(one)
    except ValueError:
        pass
    finally:
        total += one_int
print(f"This artist gets {total} streams per day.")