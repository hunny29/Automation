from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1')
import json
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver


# this is just to ensure that the page is loaded
time.sleep(5)
close = driver.find_elements_by_id('close-button')
for x in range(0,len(close)):
    if close[x].is_displayed():
        close[x].click()
time.sleep(5)
html = driver.page_source

# this renders the JS code and stores all
# of the information in static HTML code.

# Now, we could simply apply bs4 to html variable
soup = BeautifulSoup(html, "html.parser")
# all_divs = soup.find('div', {'class': 'products'})
# print(all_divs.text)

# product_price = driver.find_elements_by_class_name("catalog-item-price")
product_price = driver.find_elements_by_class_name("price")
product_name = driver.find_elements_by_class_name("catalog-item-name")
product_stock_status = driver.find_elements_by_class_name("status")
product_manufacturer = driver.find_elements_by_class_name("catalog-item-brand")

data=[]
for title,price,status,manufacturer in zip(product_name,product_price,product_stock_status,product_manufacturer):
    # print(title.text,price.text,status.text,manufacturer.text,sep="\n",end="\n\n\n")
    if status.text=='Out of Stock':
        status=False
    else:
        status=True

    data.append({
        'price': price.text,
        'title': title.text,
        'stock': status,
        'maftr': manufacturer.text
    })
print(data)
jsonString = json.dumps(data)
jsonFile = open("data.json", "w")
jsonFile.write(jsonString)
jsonFile.close()

driver.close()