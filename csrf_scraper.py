import requests as rq
from pprint import pprint
from bs4 import BeautifulSoup
scn = rq.Session()
url = "https://www.scrapingcourse.com/login/csrf"
login_page = scn.get(url)
login_page_soup = BeautifulSoup(login_page.text, "html.parser")
token = login_page_soup.find("input", attrs={"name": "_token"})["value"]
payload = {'email': "admin@example.com",
           'password': "password",
           '_token': token}

home_page = scn.post(url, data=payload)
print(home_page.status_code)
soup = BeautifulSoup(home_page.text, "html.parser")
print(soup.title.string)
products = soup.find_all(class_="product-info")
data = []
for product in products:
    data.append({
        'name': product.find(class_="product-name").text,
        'price': product.find(class_="product-price").text 
        })
pprint(data)
