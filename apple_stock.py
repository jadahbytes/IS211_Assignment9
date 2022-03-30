from bs4 import BeautifulSoup
import requests

url = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"

hdrs = {"authority": "finance.yahoo.com",
            "method": "GET",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64)"}


def main(url):
    response = requests.get(url, headers = hdrs)
    soup = BeautifulSoup(response.text, features="lxml")

    table = soup.find('table', attrs={'class': 'W(100%) M(0)'})
    rows = table.find_all('tr', attrs={'class': 'BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)'})
    for row in rows:
        data = row.find_all('td')
        try:
            date = data[0].get_text()
            close = data[4].get_text()
        except:
            continue
        print(f'''
        +-------------------+
        |Date: {date}
        |Closing Price: ${close}
        +-------------------+
        ''')

if __name__ == "__main__":
    main(url)
