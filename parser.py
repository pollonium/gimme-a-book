import urllib.request  # todo: обработать исключения типа 5xx, 4xx (см. https://khashtamov.com/ru/python-requests/)
from bs4 import BeautifulSoup  # https://www.crummy.com/software/BeautifulSoup/bs4/doc/

username = 'vankarish'
page = 1
base_url = 'https://www.livelib.ru/reader/' + username + '/wish/~' + str(page)
response = urllib.request.urlopen(base_url)
page = response.read().decode('utf-8')
soup = BeautifulSoup(page, "html.parser")
books_raw = soup.findAll("a", {"class": "brow-book-name"})
books_per_page = []
for book in books_raw:
    books_per_page.append(book.get('title'))

# todo: условием выхода будет пустой список
# while list on page isn't empty:
#   for book in books_per_page:
#       books.append(book)
# todo: выкидывать ли читаемое?
# todo: выдавать ли случайную, или предлагать другие опции?
