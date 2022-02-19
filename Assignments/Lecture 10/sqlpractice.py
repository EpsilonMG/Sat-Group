import sqlite3
import pandas as pd

# Question 1 #
from Tools.scripts.dutree import display

connection = sqlite3.connect('Books.db')
rows = connection.execute("select * from BookPriceRate where rate >=3 and booktitle like '%Mr%'").fetchall()
connection.close()
if not rows:
    print('Data Doesnt exist')
else:
    for id1, book, price, rate in rows:
        print(f'book id: {id1} book name: {book} its price: {price} and rate:{rate} ')

# Question 2 #
connection = sqlite3.connect('Books.db')
rows = connection.execute("select * from BookPriceRate where rate >=3 and price>20").fetchall()
connection.close()
if rows:
    for id1, book, price, rate in rows:
        print(f'book id: {id1} book name: {book} its price: {price} and rate:{rate} ')
else:
    print('Data does not exist')

# Question 3 #
connection = sqlite3.connect('Books.db')
rows = connection.execute("select * from booktitle_price_rate where rate !=3 ").fetchall()
connection.close()
if not rows:
    print('Data Doesnt exist')
else:
    for book, price, rate in rows:
        print(f'book name: {book} its price: {price} and rate:{rate} ')

# Question 4 #
connection = sqlite3.connect('Books.db')
rows = connection.execute("select * from BookPriceRate where rate in (1,3,4) and price between 10 and 20").fetchall()
connection.close()
if not rows != []:
    print('Data does not exist')
else:
    for id1, book, price, rate in rows:
        print(f'book id: {id1} book name: {book} its price: {price} and rate:{rate} ')

# Question 5 #
connection = sqlite3.connect('Books.db')
rows = connection.execute("select * from BookPriceRate order by price desc limit 5").fetchall()
connection.close()
if not rows:
    print('Data Doesnt exist')
else:
    for id1, book, price, rate in rows:
        print(f'book id: {id1} book name: {book} its price: {price} and rate:{rate} ')

# Question 6 #
connection = sqlite3.connect('Books.db')
rows = connection.execute("SELECT * FROM BookPriceRate ORDER BY rate desc , price asc limit 10 offset 2").fetchall()
connection.close()
if not rows:
    print('Data does not exist')
else:
    for id1, book, price, rate in rows:
        print(f'book id: {id1} book name: {book} its price: {price} and rate:{rate} ')

# Question 7 #
connection = sqlite3.connect('Books.db')
cur = connection.cursor()

cur.execute("INSERT INTO BookPriceRate VALUES (517,'book1',1,1)")
cur.execute("INSERT INTO BookPriceRate VALUES (518,'book2',2,2)")
cur.execute("INSERT INTO BookPriceRate VALUES (519,'book3',3,3)")
cur.execute("INSERT INTO BookPriceRate VALUES (520,'book4',4,4)")
cur.execute("INSERT INTO BookPriceRate VALUES (521,'book5',5,5)")

connection.commit()
connection.close()

connection = sqlite3.connect('Books.db')
rows = connection.execute("select * from BookPriceRate").fetchall()
connection.close()
if not rows:
    print('Data does not exist')
else:
    for id1, book, price, rate in rows:
        print(f'book id: {id1} book name: {book} its price: {price} and rate:{rate} ')

# Question 8 #
connection = sqlite3.connect('Books.db')
cur = connection.cursor()

cur.execute("update BookPriceRate set rate=3 where price<20")

connection.commit()
connection.close()

connection = sqlite3.connect('Books.db')
rows = connection.execute("select * from BookPriceRate where price<20").fetchall()
connection.close()

if not rows:
    print('Data does not exist')
else:
    for id1, book, price, rate in rows:
        print(f'book id: {id1} book name: {book} its price: {price} and rate:{rate} ')

# Question 9 #
connection = sqlite3.connect('Books.db')
cur = connection.cursor()

cur.execute("delete from BookPriceRate where price>50 and rate <=2 ")

connection.commit()
connection.close()

connection = sqlite3.connect('Books.db')
rows = connection.execute("select * from BookPriceRate where price>50 and rate<=2").fetchall()
connection.close()
if not rows:
    print('Data Doesnt exist')
else:
    for id1, book, price, rate in rows:
        print(f'book id: {id1} book name: {book} its price: {price} and rate:{rate} ')

# Question 10 #
connection = sqlite3.connect('books.db')
rows = connection.execute(
    "select count(BookTitle) from BookPriceRate where BookTitle like '%Secret%' and price between 10 and 25").fetchall()
connection.close()
if not rows:
    print('Data Doesnt exist')
else:
    print("the number of books that have 'Secret' in their names and price between 10£ and 25£ is: ", rows[0][0])

# Question 11 #
connection = sqlite3.connect('books.db')
rows = connection.execute("select min(price) from BookPriceRate where rate=5 ").fetchall()
connection.close()
if not rows:
    print('Data Doesnt exist')
else:
    print("the minimum price of rate=5 : ", rows[0][0])
connection = sqlite3.connect('books.db')
rows = connection.execute("select max(price) from BookPriceRate where rate=5 ").fetchall()
connection.close()
if not rows:
    print('Data Doesnt exist')
else:
    print("the maximum price of rate=5 : ", rows[0][0])

# Question 12 #
connection = sqlite3.connect('books.db')
rows = connection.execute("select avg(price) from BookPriceRate where rate=5 ").fetchall()
connection.close()

if not rows:
    print('Data Doesnt exist')
else:
    print("the avg price for all the books that have rate 5 : ", rows[0][0])

# Question 13 #
connection = sqlite3.connect('books.db')
rows = connection.execute("select sum(price) from BookPriceRate where rate=2 and price between 10 and 40 ").fetchall()
connection.close()

if not rows:
    print('Data Doesnt exist')
else:
    print("the sum of all book's price that have rate 2 and price between 10 and 40: ", rows[0][0])

# Question 14 #
connection = sqlite3.connect('books.db')
rows = connection.execute(
    "SELECT BookPriceRate.BookTitle, BookPriceRate.price, BookPriceRate.rate, BookCategories.BookTitle, "
    "BookCategories.Category FROM BookPriceRate FULL OUTER JOIN BookCategories ON "
    "BookPriceRate.BookTitle=BookCategories.BookTitle ").fetchall()

connection.close()

if not rows:
    print('Data Doesnt exist')
else:
    print("the sum of all book's price that have rate 2 and price between 10 and 40: ", rows[0][0])

# Question 15 #
connection = sqlite3.connect('books.db')
rows = connection.execute(
    "select rate, count(BookTitle) from BookPriceRate where price between 20 and 30 group by rate").fetchall()
connection.close()

if not rows:
    print('Data Doesnt exist')
else:
    for rate, count in rows:
        print(f'rate: {rate} its count: {count} ')

# Question 16 #
connection = sqlite3.connect('books.db')
rows = connection.execute("select category, count(BookTitle) from BookCategories").fetchall()
connection.close()

if not rows:
    print('Data Doesnt exist')
else:
    for category, count in rows:
        print(f' category: {category} its count: {count} ')

# Question 17 #
connection = sqlite3.connect('books.db')
rows = connection.execute(
    "select *from BookCategories where Category=(select category from BookCategories where category='Music')").fetchall()
connection.close()

if not rows:
    print('Data Doesnt exist')
else:
    for id2, book, categ in rows:
        print(f'book id: {id2} book name: {book} its category: {categ} ')

# Reading the database using panda #

connection = sqlite3.connect('books.db')

df1 = pd.read_sql_query("SELECT * FROM BookPriceRate", connection)

df2 = pd.read_sql_query("SELECT * FROM BookCategories", connection)

connection.close()

display(df1)
display(df2)
