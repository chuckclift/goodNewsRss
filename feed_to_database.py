#!/usr/bin/python3

import sqlite3
import feedparser
from itertools import chain
import datetime

def gen_article(source_number, url):
    document = feedparser.parse(url)
    for a in document['entries']:
        yield (source_number, a['link'], a['title'], a['published_parsed'])

def insert_article(article, database_connection):
    (source, url, title, date) = article
    date_string = datetime.datetime(*date[:6]).strftime("%Y-%m-%d %H:%M:%S") 

    with database_connection:
        cursor = database_connection.cursor()
        cursor.execute('''INSERT INTO frontpage_article
                            (title, pub_date, source_id, url) VALUES(?,?,?,?)''',
                            (title, date_string, source, url))

def get_article_titles(database_connection):
    with database_connection:
        cursor = database_connection.cursor()
        cursor.execute('''SELECT title FROM frontpage_article;''')
        return {a[0] for a in cursor.fetchall()}

def get_source_id_url(database_connection):
    with database_connection:
        cursor = database_connection.cursor()
        cursor.execute('''SELECT id, url FROM frontpage_source;''')
        return [a for a in cursor.fetchall()]

if __name__ == '__main__':
    article_titles = get_article_titles(sqlite3.connect('db.sqlite3'))
    all_sources = get_source_id_url(sqlite3.connect('db.sqlite3'))

    all_articles = (a for i, url in all_sources for a in gen_article(i, url))
    new_articles = (a for a in all_articles if a[2] not in article_titles)
    
    # is_new_article = lambda x: x in article_titles
    # new_articles = filter(is_new_article, article)
    
    [insert_article(a, sqlite3.connect('db.sqlite3')) for a in new_articles]
