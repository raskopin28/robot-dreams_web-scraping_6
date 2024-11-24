import re
import json

import requests
from bs4 import BeautifulSoup

def parse_html():
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
    url = 'https://www.bbc.com/sport'
    data = []

#     response = requests.get(url, headers={'user-agent': user_agent})
#     with open('bbc_sport.html', 'w') as f:
#         f.write(response.text)

    with open('bbc_sport.html', 'r') as f:
        text = f.read()

    soup = BeautifulSoup(text, 'lxml')
    articles = soup.find_all('div', type='article')
    for article in articles[:5]:
        try:
            divs = article.find('div').find('div').find_all('div')
            path = divs[0].find('a').get('href')

            divs_2 = divs[1].find('div').find('ul', role='list').find('li', role='listitem').find_all('div')
            title = divs[1].find('span').find('a').find('span').text
        except:
            title = ''

        data.append({
            'Link': url + path,
            'Topics': [title]
        })

    with open('result.json', 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == '__main__':
    parse_html()