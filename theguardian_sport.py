import pprint

import database
import requests
from bs4 import BeautifulSoup


def scraping_hackernews_pages():
    res = requests.get("https://www.theguardian.com/international")
    soup = BeautifulSoup(res.text, "html.parser")

    title = soup.find_all(class_="fc-item__container")
    vote = soup.select(".subtext")

    pprint.pprint(title)
    # newslist = (filtering_hacker_news(title, vote))
    #
    # title =[]
    # titlelink =[]
    # comment =[]
    # commentlink =[]
    # detail = []
    # for news in newslist:
    #     title.append(news["Title"].replace("'", '"'))
    #     titlelink.append(news['title_link'].replace("'", '"'))
    #     comment.append(news['comment'].replace("'", '"'))
    #     commentlink.append(news['comments_link'].replace("'", '"'))
    #     detail.append(news['detail'].replace("'", '"'))
    # database.insert_into_database("hackernews",title,titlelink,comment,commentlink,detail)
    return "insert to hacker news"


def filtering_hacker_news(title, vote):
    news_list = []
    for index, item in enumerate(title):
        url = title[index].get("href")
        point = vote[index].find(class_="score")
        comment = vote[index].find(class_="age")
        comment_link = "https://news.ycombinator.com/" + comment.find('a', href=True).get("href")
        comment = vote[index].getText().split("ago", 1)[1].replace("\xa0", " ").replace("  | hide |", "")
        detail = vote[index].getText().replace("| hide |", "").replace("\n", "").split("ago", 1)[0] + "ago"
        if point:
            current_vote = int(point.getText().replace(" points", ""))
            if current_vote > 99:
                current_news = {'Title': item.getText(), 'title_link': url,'Vote':point.getText(),
                                'comments_link': comment_link, 'detail': detail, 'comment': comment}
                news_list.append(current_news)
        if(len(news_list) > 5):
            return sorted(news_list[:5], key=lambda k: k['Vote'])
    return sorted(news_list[:5], key=lambda k: k['Vote'])

scraping_hackernews_pages()