import requests
from bs4 import BeautifulSoup
import pprint
import database

def scraping_cnn_page():
    res = requests.get("https://edition.cnn.com/world")
    soup = BeautifulSoup(res.text, "html.parser")

    titles = soup.find_all(class_="cd__wrapper")
    pprint.pprint(titles[2].find("h3").get_text())
    pprint.pprint(titles[2].find("h3").find("a").get("href"))

    newslist = (filtering_cnn_news(titles))

    title = []
    titlelink = []
    comment = []
    commentlink = []
    detail = []
    for news in newslist:
        title.append(news["title"].replace("'", '"'))
        titlelink.append(news['title_link'].replace("'", '"'))
        comment.append(news['comment'].replace("'", '"'))
        commentlink.append(news['comment_link'].replace("'", '"'))
        detail.append(news['detail'].replace("'", '"'))
    pprint.pprint(newslist)
    database.insert_into_database("cnn", title, titlelink, comment, commentlink, detail)
    return "insert to cnn news"


def filtering_cnn_news(titles):
    news_list = []
    for index, item in enumerate(titles):
        if (item.find("h3").get_text()):
            title = item.find("h3").get_text().replace("\n", "").strip()
        if (item.find("h3").find("a").get("href")):
            title_link = "https://edition.cnn.com" + item.find("h3").find("a").get("href").replace("\n", "").strip()

        match_found = 0
        for tit in news_list:
            header = tit["title"]
            if header == title:
                match_found = 1
                continue
        if match_found == 0:
            current_news = {'title': title, 'title_link': title_link, 'comment': "", 'comment_link': "",
                            'detail': ""}
            news_list.append(current_news)
        if (len(news_list) > 5):
            return news_list[:5]

scraping_cnn_page()