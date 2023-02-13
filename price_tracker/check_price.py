import re
import os
import requests
from csv import writer
from datetime import datetime
from bs4 import BeautifulSoup

# Function to check price
# Test (default) url

def check_price(filename, url):
    url = url
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find(id='productTitle').get_text()
    price = soup.find(class_='a-offscreen').get_text()[1:]

    title = re.split("-|,|:", title)[0]

    # print(title.strip())
    # print(price)

    now = datetime.now()
    date = now.strftime("%Y:%m:%d") #small "m" and "d" work better
    time = now.strftime("%H:%M:%S")

    header = ['Title', 'Price($)', 'Date', 'Time']
    data = [title, price, date, time]
    
    os.chdir(".")
    dir = "output"
    if not os.path.exists(dir):
        os.mkdir(dir)
    os.chdir(dir)
    
    if not os.path.exists(filename):
        with open(filename, 'w', newline='', encoding='UTF8') as f:
            thewriter = writer(f)
            thewriter.writerow(header)
            thewriter.writerow(data)
    else:
        with open(filename, 'a+', newline='', encoding='UTF8') as f:
            thewriter = writer(f)
            thewriter.writerow(data)
 
    return float(price)



# print(os.getcwd())

# os.chdir(".")
# dir = "output"
# if not os.path.exists(dir):
#     os.mkdir(dir)
#     os.chdir(dir)

# print(os.getcwd())