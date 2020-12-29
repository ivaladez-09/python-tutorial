"""
1. Download HTML/CSS/JS
2. Parse it
3. Use it

robots.txt - file with the content allowed to scrapped
A searcher like chrome use "Googlebot" as a scrapper tool
"""
import requests
from bs4 import BeautifulSoup
import pprint


def sort_stories_by_votes(hn_list):
    return sorted(hn_list, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []

    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})

    return sort_stories_by_votes(hn)


if __name__ == '__main__':
    res = requests.get('https://news.ycombinator.com/news')
    soup = BeautifulSoup(res.text, 'html.parser')  # Parsing HTML from web page
    # print(soup.find_all('div'))
    # print(soup.body.contents)
    # print(soup.find(id='score_20514755'))
    links = soup.select('.storylink')  # CSS Selectors
    subtext = soup.select('.subtext')
    pprint.pprint(create_custom_hn(links, subtext))

    # Getting data from page 2
    res = requests.get('https://news.ycombinator.com/news?p=2')
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select('.storylink')
    subtext = soup.select('.subtext')
    pprint.pprint(create_custom_hn(links, subtext))
