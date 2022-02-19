import requests
from bs4 import BeautifulSoup
import csv
import time

start_time = time.time()

url = 'http://books.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

rating_dic = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}

listofcateg = soup.find('ul', attrs={'class': 'nav nav-list'})

id1 = 0
id2 = 0

with open('BookPriceRate.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'Book Title', 'Price', 'Rate'])

    for categ_ref_li in listofcateg.find('ul').find_all('li'):
        categ_name = (categ_ref_li.find('a').get_text().strip())

        categ_ref = ('https://books.toscrape.com/' + (categ_ref_li.find('a').get('href')))
        response_categ = requests.get(categ_ref)
        soup_categ = BeautifulSoup(response_categ.text, 'html.parser')

        for book in soup_categ.find_all('article', attrs={'class': 'product_pod'}):
            book_name = book.find('h3').find('a').get('title')
            rate = rating_dic[book.find('p').get('class')[1]]
            price = float(
                book.find('div', attrs={'class': 'product_price'}).find('p', attrs={'class': 'price_color'}).get_text()[2:])
            writer.writerow([id1, book_name, price, rate])
            id1 = id1 + 1

with open('BookCategories.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'BookTitle', 'Category'])

    for categ_ref_li in listofcateg.find('ul').find_all('li'):
        categ_name = (categ_ref_li.find('a').get_text().strip())

        categ_ref = ('https://books.toscrape.com/' + (categ_ref_li.find('a').get('href')))
        response_categ = requests.get(categ_ref)
        soup_categ = BeautifulSoup(response_categ.text, 'html.parser')

        for book_num in soup_categ.find_all('article', attrs={'class': 'product_pod'}):
            bookname = (book_num.find('h3').find('a').get('title'))
            writer.writerow([id2, bookname, categ_name])
            id2 = id2 + 1

print("--- %s seconds ---" % (time.time() - start_time))
