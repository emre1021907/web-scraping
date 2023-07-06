from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.doviz.com/")
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'lxml')
table = soup.find('div', attrs={'class': 'news'})
listem = []

for row in table.findAll('h2', attrs={'class': 'headline--default'}):
    element = row.text
    element2 = element.strip()
    element2.
    listem.append(element2)

print(listem)
