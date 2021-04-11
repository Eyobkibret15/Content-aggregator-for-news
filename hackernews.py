import database
import requests
from bs4 import BeautifulSoup


def scraping_all_pages():
    res = requests.get("https://news.ycombinator.com/news")
    soup = BeautifulSoup(res.text, "html.parser")

    title = soup.select(".storylink")
    vote = soup.select(".subtext")
    news_list = (filtering_hacker_news(title, vote))

    database.initialize_database()
    for news in news_list:
        title = news["Title"].replace("'" ,'"')
        titlelink = news['title_link'].replace("'" ,'"')
        comment = news['comment'].replace("'" ,'"')
        commentlink = news['comments_link'].replace("'" ,'"')
        detail = news['detail'].replace("'" ,'"')
        database.insert_into_hackernews(title,titlelink,comment,commentlink,detail)

    return "hackernews database updated"


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
                current_news = {'Title': item.getText(), 'title_link': url,'Vote':vote,
                                'comments_link': comment_link, 'detail': detail, 'comment': comment}
                news_list.append(current_news)

    return sorted(news_list[:5], key=lambda k: k['Vote'])

