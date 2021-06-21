import database
import requests
from bs4 import BeautifulSoup
import re


def scraping_bbc_pages():
    res = requests.get("https://www.bbc.com/news")
    soup = BeautifulSoup(res.text, "html.parser")
    grn = soup.find_all("a")
    stitle = soup.find_all(class_="gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold "
                                  "nw-o-link-split__anchor")
    ftitle = soup.find_all(class_="gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-paragon-bold "
                                  "nw-o-link-split__anchor")
    title = ftitle + stitle
    summary = soup.find_all(class_="gs-c-promo-summary gel-long-primer gs-u-mt nw-c-promo-summary")
    date = soup.find_all(class_="gs-o-bullet__text date qa-status-date gs-u-align-middle gs-u-display-inline")
    area = soup.find_all(class_="gs-c-section-link gs-c-section-link--truncate nw-c-section-link nw-o-link "
                                "nw-o-link--no-visited-state")
    news_list = (filtering_bbc_news(title, summary, date, area))

    title = []
    titlelink = []
    time = []
    location = []
    detail = []
    for news in news_list:
        title.append(news["title"].replace("'", '"'))
        titlelink.append(news['title_link'].replace("'", '"'))
        time.append(news['time'].replace("'", '"'))
        location.append(news['location'].replace("'", '"'))
        detail.append(news['detail'].replace("'", '"'))
    database.insert_into_database("bbc",title, titlelink, time, location, detail)

    return "bbc database updated"


def filtering_bbc_news(title, summary, date, area):
    news_list = []
    for index, item in enumerate(title[:8]):
        title = item.getText()
        url = "https://www.bbc.com" + item.get("href")
        time = re.split("h|m|day",date[index].getText(),1)[1]
        detail = summary[index].getText()
        location = area[index].getText()

        match_found = 0
        for tit in news_list:
            header = tit["title"]
            if header == title:
                match_found = 1
                continue
        if match_found == 0:
            current_news = {'title': title, 'title_link': url, 'time': time,
                            'location': location, 'detail': detail}
            news_list.append(current_news)

    return news_list[:5]


