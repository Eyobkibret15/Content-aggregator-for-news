import database
import requests
from bs4 import BeautifulSoup



def scraping_aljazeera_page():
    res = requests.get("https://www.aljazeera.com/")
    soup = BeautifulSoup(res.text, "html.parser")

    htitle = soup.find_all(class_='fte-featured__title__link')
    stitle = soup.find_all(class_='fte-featured__excerpt__link fte-featured__title__link')
    title = htitle + stitle

    details = soup.find_all('p')
    newslist = filtering_aljazeera_news(title ,details)

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
    database.insert_into_database("aljazeera", title, titlelink, time, detaillink, detail)

    return "aljazeera database updated"


def filtering_aljazeera_news(title, summery):
    news_list = []
    for index, item in enumerate(title[:8]):
        title = item.get_text()
        title_link = "https://www.aljazeera.com" + item.get('href')

        detail = summery[index].get_text()

        match_found = 0
        for tit in news_list:
            header = tit["title"]
            if header == title:
                match_found = 1
                continue
        if match_found == 0:
            current_news = {'title': title, 'title_link': title_link , 'time':"",'detaillink':title_link ,'detail': detail }
            news_list.append(current_news)

    return news_list[:5]


scraping_aljazeera_page()
