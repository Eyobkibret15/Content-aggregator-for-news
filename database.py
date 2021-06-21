import psycopg2
import hackernews

connection = psycopg2.connect(dbname="postgres", user="postgres", password="dbmikemoh")
cursor = connection.cursor()

def insert_into_hackernews():
    connection = psycopg2.connect(dbname="postgres", user="postgres", password="dbmikemoh")
    cursor = connection.cursor()
    title, titlelink, comment, commentlink, detail =hackernews.scraping_all_pages()
    print(len(title))
    cursor.execute("DELETE FROM hackernews;")
    insert = f"INSERT INTO hackernews (TITLE, TITLELINK, COMMENT,COMMENTLINK,DETAIL) VALUES ('{title}' , '{titlelink}','{comment}','{commentlink}','{detail}');"
    cursor.execute(insert)
    connection.commit()

def select_from_database(name):
    connection = psycopg2.connect(dbname="postgres", user="postgres", password="dbmikemoh")
    cursor = connection.cursor()
    select = f"SELECT * FROM {name};"
    cursor.execute(select)
    data = cursor.fetchall()
    return data
def sending_artibuite_to_the_server():
    title = []
    titlelink = []
    comment = []
    commentlink = []
    detail = []
    # hackernews.scraping_all_pages()
    insert_into_hackernews()
    data = select_from_database("hackernews")
    for value in data:
        title.append(value[1])
        titlelink.append(value[2])
        comment.append(value[3])
        commentlink.append(value[4])
        detail.append(value[5])
    # print(len(title))
    
    return title,titlelink,comment,commentlink,detail
def close_database():
    cursor.close()

select_from_database("hackernews")
sending_artibuite_to_the_server()