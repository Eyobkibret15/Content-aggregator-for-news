import database
import requests
from bs4 import BeautifulSoup


def scraping_first_news_pages():
    res = requests.get("https://www.thefirstnews.com/")
    soup = BeautifulSoup(res.text, "html.parser")

    titles = soup.find_all(class_='news__item')
    newslist = filtering_first_news(titles)

    title = []
    titlelink = []
    type = []
    detaillink = []
    detail = []
    for news in newslist:
        title.append(news["title"].replace("'", '"'))
        titlelink.append(news['title_link'].replace("'", '"'))
        type.append(news['type'].replace("'", '"'))
        detaillink.append(news['detaillink'].replace("'", '"'))
        detail.append(news['detail'].replace("'", '"'))
    database.insert_into_database("first_news", title, titlelink, type, detaillink, detail)
    return"the first news database updated"


def filtering_first_news(titles):
    news_list = []
    for index, item in enumerate(titles):
        if (item.find('h3')):
            title = item.find('h3').get_text().replace("\n", "").strip()
        if (item.find('h3').find('a').get('href')):
            title_link = 'https://www.thefirstnews.com' + item.find('h3').find('a').get('href').replace("\n","").strip()
        if (item.find('p')):
            detail = item.find('p').get_text().replace("\n", "").strip()
        if (item.find('span')):
            type = item.find('span').get_text().replace("\n", "").strip()

        match_found = 0
        for tit in news_list:
            header = tit["title"]
            if header == title:
                match_found = 1
                continue
        if match_found == 0:
            current_news = {'title': title, 'title_link': title_link,'type':type,'detaillink' : title_link ,
                             'detail': detail}
            news_list.append(current_news)

    return news_list[:5]

