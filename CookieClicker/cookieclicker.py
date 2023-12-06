#https://orteil.dashnet.org/cookieclicker/

# Code start's from here:
# importing modules which we needed in this projects
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time 

# opening chrome and searching for the website

driver = webdriver.Chrome()
driver.get("http://www.google.com/")
WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME,"gLFyf"))
)
driver.fullscreen_window()
input_Field = driver.find_element(By.CLASS_NAME,"gLFyf")
input_Field.send_keys("cookieclicker"+Keys.ENTER)
link = driver.find_element(By.PARTIAL_LINK_TEXT,'Cookie Clicker - Orteil')
link.click()
WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.XPATH,"//*[@id=\"langSelect-EN\"]"))
)
language = driver.find_element(By.XPATH,"//*[@id=\"langSelect-EN\"]")
language.click()
while True:
    WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.ID,"bigCookie"))
)
    cookies_click = driver.find_element(By.ID,"bigCookie")
    cookies_click.click()
    cookies_count = int(driver.find_element(By.ID,"cookies").text.split(" ")[0])
    cursor_clicker = int(driver.find_element(By.ID,"productPrice0").text)
    buy_cursor =  driver.find_element(By.ID,"product0")
    if cookies_count>=cursor_clicker:
        buy_cursor.click()

    gandma_clicker = int(driver.find_element(By.ID,"productPrice1").text)
    buy_grandma =  driver.find_element(By.ID,"product1")
    if cookies_count>= gandma_clicker:
        buy_grandma.click()

    try:
        farm_clicker = int(driver.find_element(By.ID,"productPrice2").text)
        buy_farm =  driver.find_element(By.ID,"product2")
        if cookies_count>= farm_clicker:
            buy_farm.click()
    except:
        continue

    try:    
        Mine_clicker = int(driver.find_element(By.ID,"productPrice1").text)
        buy_Mine =  driver.find_element(By.ID,"product1")
        if cookies_count>= Mine_clicker:
            buy_Mine.click()
    except:
        continue

    try:
        Factory_clicker = int(driver.find_element(By.ID,"productPrice1").text)
        buy_Factory =  driver.find_element(By.ID,"product1")
        if cookies_count>= Factory_clicker:
            buy_Factory.click()   
    except:
        continue
