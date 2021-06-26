import pprint
import hackernews
import bbc
import database
import tvn24
import the_first_news
import aljazeera
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    the_first_news.scraping_first_news_pages()
    firstnews_data = database.get_first_news_data()
    bbc.scraping_bbc_pages()
    bbc_data = database.get_bbc_data()
    tvn24.scraping_tvn24_pages()
    tvn24_data = database.get_tvn24_data()
    aljazeera.scraping_aljazeera_page()
    aljazeera_data = database.get_aljazeera_data()
    hackernews.scraping_hackernews_pages()
    hackernews_data = database.get_hackernews_data()
    news = {'hackernews':hackernews_data,'bbc':bbc_data,'aljazeera':aljazeera_data,'tvn24':tvn24_data,'firstnews':firstnews_data}
    pprint.pprint(news)

    return news
    # return render_template("index.html",
    #                        title0=title[0],titlelink0 = titlelink[0], comment0 = comment[0],commentlink0=commentlink[0],detail0 = detail[0],
    #                        title1=title[1],titlelink1 = titlelink[1], comment1 = comment[1],commentlink1=commentlink[1],detail1 = detail[1],
    #                        title2=title[2],titlelink2 = titlelink[2], comment2 = comment[2],commentlink2=commentlink[2],detail2 = detail[2],
    #                        title3=title[3],titlelink3 = titlelink[3], comment3 = comment[3],commentlink3=commentlink[3],detail3 = detail[3],
    #                        title4=title[4],titlelink4 = titlelink[4], comment4 = comment[4],commentlink4=commentlink[4],detail4 = detail[4])


#this