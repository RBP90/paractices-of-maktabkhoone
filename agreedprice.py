import requests
from bs4 import BeautifulSoup
import re

r = requests.get('https://divar.ir/s/tehran')

soup = BeautifulSoup(r.text , 'html.parser')

all_items = soup.find_all('div' , attrs={'class': 'kt-post-card__body'})


for item in all_items:
    if 'توافقی' in item.text:
        print(re.sub(r'\s+', '', item.text).strip())
