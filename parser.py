# todo: add requirements.txt
import urllib.request  # todo: обработать исключения типа 5xx, 4xx (см. https://khashtamov.com/ru/python-requests/)
from bs4 import BeautifulSoup  # https://www.crummy.com/software/BeautifulSoup/bs4/doc/

username = 'vankarish'
base_url = 'https://www.livelib.ru/reader/' + username + '/wish/~'
page_number = 1
books = []
while True:
    url = base_url + str(page_number)
    response = urllib.request.urlopen(url)
    page = response.read().decode('utf-8')
    soup = BeautifulSoup(page, "html.parser")
    books_raw = soup.findAll("a", {"class": "brow-book-name"})
    books_per_page = []
    for book in books_raw:
        books_per_page.append(book.get('title'))
    if not len(books_per_page):
        break
    books += books_per_page
    page_number += 1
