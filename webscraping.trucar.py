import requests
from bs4 import BeautifulSoup
import mysql.connector

cnx = mysql.connector.connect(user='root', password='reza6678232',
                              host='127.0.0.1',
                              database='maktabkhoone')

cursor = cnx.cursor()


print ('which brnad do you want to search? ')
brand = input().strip().replace(' ', '-').lower()
#print (brand)

r = requests.get(f'https://www.truecar.com/used-cars-for-sale/listings/{brand}/')

soup = BeautifulSoup(r.text , 'html.parser')

prices = soup.find_all('div' ,attrs={'data-test': 'vehicleListingPriceAmount'})
worked = soup.find_all('div' ,attrs={'class': ['truncate', 'text-xs'], 'data-test': 'vehicleMileage'})

count = 0
for price, w in zip(prices, worked):
    if count == 20:
        break
            
    #print(price.text.strip(), w.text.strip())
        
    query = "INSERT INTO truecar (price, worked) VALUES (%s, %s)"
    values = (price.text.strip(), w.text.strip())
    cursor.execute(query, values)

    count += 1
cnx.commit()

cnx.close()