import psycopg2


def create_table_for_hackernews():
    connection = psycopg2.connect(dbname="postgres", user="postgres", password="dbmikemoh")
    cursor = connection.cursor()
    createhackernews = f"CREATE TABLE IF NOT EXISTS hackernews(id SERIAL PRIMARY KEY ,TITLE text,TITLELINK text,COMMENT text,COMMENTLINK text,DETAIL text);"
    cursor.execute(createhackernews)
    connection.commit()


def create_table_for_bbc():
   connection = psycopg2.connect(dbname="postgres", user="postgres", password="dbmikemoh")
    cursor = connection.cursor()
    bbc = "CREATE TABLE IF NOT EXISTS bbc(id SERIAL PRIMARY KEY ,TITLE text,TITLELINK text,TIME text,LOCATION text,DETAIL text);"
    cursor.execute(bbc)
    connection.commit()

def create_table_for_tvn24():
    connection = psycopg2.connect(dbname="postgres", user="postgres", password="dbmikemoh")
    cursor = connection.cursor()
    tvn24 = "CREATE TABLE IF NOT EXISTS tvn24(id SERIAL PRIMARY KEY ,TITLE text,TITLELINK text,TIME text,DETAILLINK text,DETAIL text);"
    cursor.execute(tvn24)
    connection.commit()

def create_table_for_aljazeera():
    connection = psycopg2.connect(dbname="postgres", user="postgres", password="dbmikemoh")
    cursor = connection.cursor()
    aljazeera = "CREATE TABLE IF NOT EXISTS aljazeera(id SERIAL PRIMARY KEY ,TITLE text,TITLELINK text,TIME text,DETAILLINK text,DETAIL text);"
    cursor.execute(aljazeera)
    connection.commit()

def create_table_for_first_news():
    connection = psycopg2.connect(dbname="postgres", user="postgres", password="dbmikemoh")
    cursor = connection.cursor()
    firsr_news = "CREATE TABLE IF NOT EXISTS first_news (id SERIAL PRIMARY KEY ,TITLE text,TITLELINK text,TYPE text,DETAILLINK text,DETAIL text);"
    cursor.execute(firsr_news)
    connection.commit()

def insert_into_database(news,title,titlelink,comment,commentlink,detail):
    connection = psycopg2.connect(dbname="postgres", user="postgres", password="dbmikemoh")
    cursor = connection.cursor()
    if news == "hackernews":
        create_table_for_hackernews()
        cursor.execute("DELETE FROM hackernews;")
        for value in range(5):
            insert = f"INSERT INTO hackernews(TITLE, TITLELINK, COMMENT,COMMENTLINK,DETAIL) VALUES ('{title[value]}','{titlelink[value]}','{comment[value]}','{commentlink[value]}','{detail[value]}');"
            cursor.execute(insert)

    elif news == "bbc":
        create_table_for_bbc()
        cursor.execute("DELETE FROM bbc;")
        for value in range(5):
            insert = f"INSERT INTO bbc (TITLE, TITLELINK, time,location,DETAIL) VALUES ('{title[value]}','{titlelink[value]}','{comment[value]}','{commentlink[value]}','{detail[value]}');"
            cursor.execute(insert)

    elif news == "tvn24":
        create_table_for_tvn24()
        cursor.execute("DELETE FROM tvn24;")
        for value in range(5):
            insert = f"INSERT INTO tvn24 (TITLE, TITLELINK, TIME,DETAILLINK,DETAIL) VALUES ('{title[value]}','{titlelink[value]}','{comment[value]}','{commentlink[value]}','{detail[value]}');"
            cursor.execute(insert)

    elif news == "aljazeera":
        create_table_for_aljazeera()
        cursor.execute("DELETE FROM aljazeera;")
        for value in range(5):
            insert = f"INSERT INTO aljazeera (TITLE, TITLELINK, TIME,DETAILLINK,DETAIL) VALUES ('{title[value]}','{titlelink[value]}','{comment[value]}','{commentlink[value]}','{detail[value]}');"
            cursor.execute(insert)

    elif news == "first_news":
        create_table_for_first_news()
        cursor.execute("DELETE FROM first_news;")
        for value in range(5):
            insert = f"INSERT INTO first_news (TITLE, TITLELINK, TYPE ,DETAILLINK,DETAIL) VALUES ('{title[value]}','{titlelink[value]}','{comment[value]}','{commentlink[value]}','{detail[value]}');"
            cursor.execute(insert)


    connection.commit()
    cursor.close()


def select_from_database(name):
    connection = psycopg2.connect(dbname="postgres", user="postgres", password="dbmikemoh")
    cursor = connection.cursor()
    select = f"SELECT * FROM {name};"
    cursor.execute(select)
    data = cursor.fetchall()
    return data


def get_hackernews_data():
    title = []
    titlelink = []
    comment = []
    commentlink = []
    detail = []

    data = select_from_database("hackernews")
    for value in data:
        title.append(value[1])
        titlelink.append(value[2])
        comment.append(value[3])
        commentlink.append(value[4])
        detail.append(value[5])
    hackernews = {"title": title, 'titlelink': titlelink, 'comment': comment, 'commentlink': commentlink, 'detail': detail}
    return hackernews

def get_bbc_data():
    title = []
    titlelink = []
    time = []
    location = []
    detail = []
    data = select_from_database("bbc")
    for value in data:
        title.append(value[1])
        titlelink.append(value[2])
        time.append(value[3])
        location.append(value[4])
        detail.append(value[5])
    bbc = {"title": title, 'titlelink': titlelink, 'time': time, 'location': location, 'detail': detail}
    return bbc

def get_tvn24_data():
    title = []
    titlelink = []
    time = []
    detaillink = []
    detail = []
    data = select_from_database("tvn24")
    for value in data:
        title.append(value[1])
        titlelink.append(value[2])
        time.append(value[3])
        detaillink.append(value[4])
        detail.append(value[5])
    tvn24 = {"title": title, 'titlelink': titlelink, 'time': time, 'detaillink': detaillink, 'detail': detail}
    return tvn24

def get_first_news_data():
    title = []
    titlelink = []
    type = []
    detaillink = []
    detail = []
    data = select_from_database("first_news")
    for value in data:
        title.append(value[1])
        titlelink.append(value[2])
        type.append(value[3])
        detaillink.append(value[4])
        detail.append(value[5])
    first_news = {"title": title, 'titlelink': titlelink, 'type': type, 'detaillink': detaillink, 'detail': detail}
    return first_news


def get_aljazeera_data():
    title = []
    titlelink = []
    time = []
    detaillink = []
    detail = []
    data = select_from_database("aljazeera")
    for value in data:
        title.append(value[1])
        titlelink.append(value[2])
        time.append(value[3])
        detaillink.append(value[4])
        detail.append(value[5])
    aljazeera = {"title":title,'titlelink':titlelink,'time':time,'detaillink':detaillink,'detail':detail}
    return aljazeera