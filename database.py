import psycopg2

connection = psycopg2.connect(dbname="postgres", user="postgres", password="35583377")
cursor = connection.cursor()


def initialize_database():
    cursor.execute("DELETE FROM hackernews;")


def insert_into_hackernews(title, titlelink, comment, commentlink, detail):
    insert = f"INSERT INTO hackernews (TITLE, TITLELINK, COMMENT,COMMENTLINK,DETAIL) VALUES ('{title}' , '{titlelink}','{comment}','{commentlink}','{detail}');"
    cursor.execute(insert)
    connection.commit()

def select_from_database(name):
    connection = psycopg2.connect(dbname="postgres", user="postgres", password="35583377")
    cursor = connection.cursor()
    select = f"SELECT * FROM {name};"
    cursor.execute(select)
    data = cursor.fetchall()
    return data

def close_database():
    cursor.close()

select_from_database("hackernews")