import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pprint
import re

def scraping_tvn24_page():
    res = requests.get("https://www.goal.com/en")
    soup = BeautifulSoup(res.text, "html.parser")

    detail = soup.find_all('h3')
    titles = soup.find_all(class_="widget-news-card__title")
    pprint.pprint(detail)
    # newslist = filtering_tvn24_news(titles)
    return "goal.com database updated"

def filtering_tvn24_news(titles):
    news_list = []
    for index, item in enumerate(titles):
            title = item.get_text().replace("\n", "").strip()
            pprint.pprint(title)
            title_link = 'https://www.thefirstnews.com' + item.find('h3').find('a').get('href').replace("\n","").strip(

            )
        # if (item.find('p')):
        #     detail = item.find('p').get_text().replace("\n", "").strip()
        # if (item.find('span')):
        #     type = item.find('span').get_text().replace("\n", "").strip()
        #
        # match_found = 0
        # for tit in news_list:
        #     header = tit["title"]
        #     if header == title:
        #         match_found = 1
        #         continue
        # if match_found == 0:
        #     current_news = {'title': title, 'title_link': title_link, 'detail': detail,'detail_link' : title_link ,
        #                      'type':type}
        #     news_list.append(current_news)

    return news_list[:5]


scraping_tvn24_page()