from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

option=webdriver.ChromeOptions()
option.add_argument("-incognito")

browser=webdriver.Chrome(executable_path="/Users/shristijalan/Desktop/chromedriver",chrome_options=option)
browser.get("url of github profile")

timeout=20

try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH,"//img[@class='avatar width-full rounded-2']")))
except  TimeoutException :
    print("quit")
    browser.quit()

titles = browser.find_elements_by_xpath("//a[@class='text-bold']")
#for x in titles:
    #print(x.text)

title=[x.text for x in titles]

languages=browser.find_elements_by_xpath("//p[@class='mb-0 f6 text-gray']")
#for y in languages:
    #print(y.text)

language=[x.text for x in languages]

for ftitle,flangauge in zip(title,language):

    print("Title:",ftitle)
    print("Language:",flangauge)
    print("\n")
