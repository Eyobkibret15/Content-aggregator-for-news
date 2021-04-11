from flask import Flask, render_template, request, redirect
import database
import hackernews

app = Flask(__name__)


@app.route('/')
def home():
    title = []
    titlelink = []
    comment = []
    commentlink = []
    detail = []
    hackernews.scraping_all_pages()
    database.initialize_database()
    data = database.select_from_database("hackernews")
    for value in data:
        title.append(value[1])
        titlelink.append(value[2])
        comment.append(value[3])
        commentlink.append(value[4])
        detail.append(value[5])
    return render_template("index.html",
                           title0=title[0],titlelink0 = titlelink[0], comment0 = comment[0],commentlink0=commentlink[0],detail0 = detail[0],
                           title1=title[1],titlelink1 = titlelink[1], comment1 = comment[1],commentlink1=commentlink[1],detail1 = detail[1],
                           title2=title[2],titlelink2 = titlelink[2], comment2 = comment[2],commentlink2=commentlink[2],detail2 = detail[2],
                           title3=title[3],titlelink3 = titlelink[3], comment3 = comment[3],commentlink3=commentlink[3],detail3 = detail[3],
                           title4=title[4],titlelink4 = titlelink[4], comment4 = comment[4],commentlink4=commentlink[4],detail4 = detail[4])

def upload_hackernews():

    title = []
    titlelink = []
    comment = []
    commentlink = []
    detail = []
    database.initialize_database()
    data = database.select_from_database("hackernews")
    for value in data:
        print(value[1])
        title.append(value[1])
        titlelink += value[2]
        comment += value[3]
        commentlink += value[4]
        detail += value[5]
    database.close_database()
    print(title[0])
    return title,titlelink,comment,commentlink,detail

