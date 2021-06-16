import database
import requests
from bs4 import BeautifulSoup
import pprint
import re


def scraping_cnn_page():
    res = requests.get("https://www.aljazeera.com/")
    soup = BeautifulSoup(res.text, "html.parser")
    title = soup.find_all(class_='fte-featured__title__link')[0].get_text()
    titlelink = "https://www.aljazeera.com" + soup.find_all(class_='fte-featured__title__link')[0].get('href')
    print(titlelink)
    stitle = soup.find_all(class_='fte-featured__excerpt__link fte-featured__title__link')

    for i in stitle:
         stitle = i.get_text()
         stitlelink = "https://www.aljazeera.com"+ i.get("href")
    detail = soup.find_all(class_='fte-featured__excerpt__link fte-featured__title__link')
      
    # grn = soup.find_all("a")
    # stitle = soup.find_all(class_="gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold "
    #                               "nw-o-link-split__anchor")
    # ftitle = soup.find_all(class_="gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-paragon-bold "
    #                               "nw-o-link-split__anchor")
    # title = ftitle + stitle
    # summary = soup.find_all(class_="gs-c-promo-summary gel-long-primer gs-u-mt nw-c-promo-summary")
    # date = soup.find_all(class_="gs-o-bullet__text date qa-status-date gs-u-align-middle gs-u-display-inline")
    # area = soup.find_all(class_="gs-c-section-link gs-c-section-link--truncate nw-c-section-link nw-o-link "
    #                             "nw-o-link--no-visited-state")
    # news_list = (filtering_hacker_news(title, summary, date, area))
    # pprint.pprint(news_list)
    # print(len(news_list))
    # database.initialize_database()
    # for news in news_list:
    # titlelink = "https://www.bbc.com"+news.get("href")
    # title =news.getText()
    # news_list.append(news.getText())
    # title = news["Title"].replace("'" ,'"')
    # titlelink = news['title_link'].replace("'" ,'"')
    # comment = news['comment'].replace("'" ,'"')
    # commentlink = news['comments_link'].replace("'" ,'"')
    # detail = news['detail'].replace("'" ,'"')
    # database.insert_into_hackernews(title,titlelink,comment,commentlink,detail)

    return "bbc database updated"


def filtering_hacker_news(title, summary, date, area):
    news_list = []
    for index, item in enumerate(title[:8]):
        title = item.getText()
        url = "https://www.bbc.com" + item.get("href")
        time = re.split("h|m|day",date[index].getText(),1)[1]
        detail = summary[index].getText()
        location = area[index].getText()
        # comment_link = "https://news.ycombinator.com/" + comment.find('a', href=True).get("href")
        # comment = vote[index].getText().split("ago", 1)[1].replace("\xa0", " ").replace("  | hide |", "")
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


scraping_cnn_page()
