import pprint

import database
import requests
from bs4 import BeautifulSoup


def scraping_cnet_pages():
    res = requests.get("https://gizmodo.com/latest")
    soup = BeautifulSoup(res.text, "html.parser")

    news = soup.find(class_='cw4lnv-4 eRRMSy').find(class_="cw4lnv-5 aoiLP")
    pprint.pprint(news)
    # newslist = filtering_techcrunch(news)
    # title = []
    # titlelink = []
    # time = []
    # author = []
    # detail = []
    # for news in newslist:
    #     title.append(news["title"].replace("'", '"'))
    #     titlelink.append(news['title_link'].replace("'", '"'))
    #     time.append(news['time'].replace("'", '"'))
    #     author.append(news['author'].replace("'", '"'))
    #     detail.append(news['detail'].replace("'", '"'))
    # database.insert_into_database("techcrunch", title, titlelink, time, author, detail)
    return"the techcrunch database updated"


def filtering_techcrunch(news):
    news_list = []
    for index, item in enumerate(news):
        if (item.find(class_="post-block__header").find("h2").find("a")):
            titles = item.find(class_="post-block__header").find("h2").find("a")
            title = titles.get_text().replace("\n", "").strip()
            title_link=titles.get("href").replace("\n", "").strip()
        if (item.find(class_="post-block__meta").find("a")):
            author = item.find(class_="post-block__meta").find("a").get_text().replace("\n", "").strip()
        if (item.find(class_="post-block__meta").find(class_="river-byline__time")):
            time =item.find(class_="post-block__meta").find(class_="river-byline__time").get_text().replace("\n", "").strip()
        if (item.find(class_="post-block__content")):
            detail = item.find(class_="post-block__content").get_text().replace("\n", "").strip()

        match_found = 0
        for tit in news_list:
            header = tit["title"]
            if header == title:
                match_found = 1
                continue
        if match_found == 0:
            current_news = {'title': title, 'title_link': title_link,'time':time,'author' : author ,
                             'detail': detail}
            news_list.append(current_news)

    return news_list[:5]
scraping_cnet_pages()
