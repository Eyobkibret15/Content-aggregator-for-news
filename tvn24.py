import database
import requests
from bs4 import BeautifulSoup



def scraping_tvn24_pages():
    res = requests.get("https://tvn24.pl/tvn24-news-in-english")
    soup = BeautifulSoup(res.text, "html.parser")

    title = soup.find_all(class_='teaser-wrapper__content default-teaser default-teaser--standard')

    time = soup.find_all(class_='label-date')

    newslist = filtering_tvn24_news(title , time)
    title = []
    titlelink = []
    time = []
    detaillink = []
    detail = []
    for news in newslist:
        title.append(news["title"].replace("'", '"'))
        titlelink.append(news['title_link'].replace("'", '"'))
        time.append(news['time'].replace("'", '"'))
        detaillink.append(news['detaillink'].replace("'", '"'))
        detail.append(news['detail'].replace("'", '"'))
    database.insert_into_database("tvn24", title, titlelink, time, detaillink, detail)
    return "tvn24 database updated"


def filtering_tvn24_news(title, times):
    news_list = []
    for index, item in enumerate(title[:8]):
        title = item.find('h2').get_text()
        title_link = item.find('a').get('href')
        detail = item.find('p').get_text()
        time = times[index].get_text()

        match_found = 0
        for tit in news_list:
            header = tit["title"]
            if header == title:
                match_found = 1
                continue
        if match_found == 0:
            current_news = {'title': title, 'title_link': title_link, 'time' : time,'detaillink':title_link,'detail': detail}
            news_list.append(current_news)

    return news_list[:5]
