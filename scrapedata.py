import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(res.text,"html.parser")
scr = soup.select('.subtext')
story = soup.select('.storylink')

def sorted_stories(hnlist):
    return (sorted(hnlist,key= lambda k:k['votes'],reverse=True))
def f(scr,story):
    hn = []
    for idx, item in enumerate(story):
        links = story[idx].get('href')
        heading = story[idx].getText()
        # hn.append({'title': links, 'heading': votes})
        points = scr[idx].select('.score')
        if len(points):
            votes = int(points[0].getText().split( )[0])
            if votes>99:
                hn.append({'title': links, 'heading': heading, 'votes':votes})
    return sorted_stories(hn)

pprint.pprint(f(scr,story))