from bs4 import BeautifulSoup
import csv
import requests
import os

#os.chdir('D:\Github Epsilon\Sat-Group\Sat-Group\Mohamed Ashraf Shebl\Lecture 8 Assignment')

Scrapper = BeautifulSoup(requests.get("https://books.toscrape.com/index.html").text,'html.parser')
Domain = 'https://books.toscrape.com/'

Category_name_link = {} #Store each category's name and link in this dictionary
rating = {'One':1,'Two':2,'Three':3,'Four':4,'Five':5}

for il in Scrapper.find('ul' , attrs={'class':'nav nav-list'}).find('ul').findAll('li'):
    Category_name_link[il.get_text().strip()] = Domain+il.find('a').get('href')


def Scrap_dict(dictionary_url,dictionary_name):

    Scrapper = BeautifulSoup(requests.get(dictionary_url).text,'html.parser')
    Data = []
    with open('books.csv','a',newline='') as f:
        writer=csv.writer(f)
        writer.writerow(['Book Name','Rating','Price','Category'])
        if Scrapper.find('li',attrs={'class':'next'}) == None: #If no next pages found print the next
            for book in Scrapper.find('ol' , attrs={'class':'row'}).find_all('li'):
                Data.append((book.find('h3').find('a').get('title'), rating[book.find('p').get('class')[1]], float(book.find('p',attrs={'class':'price_color'}).get_text()[2:])))
                writer.writerow([book.find('h3').find('a').get('title').decode(encoding='UTF-8',errors='strict'),rating[book.find('p').get('class')[1]],float(book.find('p',attrs={'class':'price_color'}).get_text()[2:]),dictionary_name])
            print("Finished Category: no remanining pages left.")

        else:
            Scrapper = BeautifulSoup(requests.get(dictionary_url[:dictionary_url.rfind('/')] +'/'+ Scrapper.find('li',attrs={'class':'next'}).find('a').get('href')).text,'html.parser')
            for book in Scrapper.find('ol' , attrs={'class':'row'}).find_all('li'):
                Data.append((book.find('h3').find('a').get('title'), rating[book.find('p').get('class')[1]], float(book.find('p',attrs={'class':'price_color'}).get_text()[2:])))
                writer.writerow([book.find('h3').find('a').get('title').decode(encoding='UTF-8',errors='strict'),rating[book.find('p').get('class')[1]],float(book.find('p',attrs={'class':'price_color'}).get_text()[2:]),dictionary_name])   
        return Data #returns a List of items (Book Title , Book Rating , Book Price])

for name , link in Category_name_link.items():
    print(Scrap_dict(link,name))





