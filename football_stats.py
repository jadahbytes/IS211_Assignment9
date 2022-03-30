from bs4 import BeautifulSoup
import requests



url = 'https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/?sortcol=td&sortdir=descending'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html5lib')
#print(soup.prettify())
#stats = soup.find_all('tr', attrs={'class': 'TableBase-bodyTr'})
#print(stats)


def main(url):
    for tr in soup.find_all('tr', class_='TableBase-bodyTr', limit=20):
        #print(tr)
        name = tr.find('span', class_='CellPlayerName--long').a.text.strip()
        #print("Name: ", name)
        position = tr.find('span', class_='CellPlayerName-position').text.strip()
        #print("Postion: ", position)
        team = tr.find('span', class_='CellPlayerName-team').text.strip()
        #print("Team: ", team)
        find_tds = tr.find_all('td')
        touchdowns = find_tds[8].get_text().strip()
        #print("Touchdowns", touchdowns)

        print(f'''
        +-------------------+
        |Name: {name}
        |Position: {position}
        |Team: {team}
        |Touchdowns: {touchdowns}
        +-------------------+
        ''')

if __name__ == "__main__":
    main(url)
