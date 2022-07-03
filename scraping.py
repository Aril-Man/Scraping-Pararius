from itertools import count
import requests
from bs4 import BeautifulSoup
import csv

keyword = input("Enter a keyword: ")

URL = 'https://www.pararius.com/apartments/{}/page'.format(keyword)

write = csv.writer(open('results/hasil_scraping_{}.csv'.format(keyword), 'w', newline=''))
head = ['No', 'Name', 'Price/Bulan', 'Location']
write.writerow(head)

count = 0

for page in range(1, 3):

    req = requests.get(URL + str(page))

    # print(req)

    soup = BeautifulSoup(req.text, 'html.parser')

    items = soup.find_all('section', 'listing-search-item listing-search-item--list listing-search-item--for-rent')

    # print(items)
    for item in items:
        name = item.find('a', 'listing-search-item__link listing-search-item__link--title').text.replace('\n', '').replace('\t', '')
        price = item.find('div', 'listing-search-item__price').text.replace('\n', '').replace('\t', '')
        location = item.find('div', 'listing-search-item__location').text.replace('\n', '').replace('\t', '')
        count += 1
        
        info = [count, name, price, location]
        print(info)
        
        write = csv.writer(open('results/hasil_scraping_{}.csv'.format(keyword), 'a', newline=''))
        header = [count ,name, price, location]
        write.writerow(header)
        



