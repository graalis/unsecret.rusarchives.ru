from selenium import webdriver
import re
import time

chrome_path=r"D:/ALEX/Desktop/Indiegogo/unit tests/kickstarter/chromedriver.exe"


browser = webdriver.Chrome(chrome_path)
browser.get("http://unsecret.rusarchives.ru/search")
search_opt = browser.find_elements_by_xpath(".//select[@id='Search_table']/option")
# find "Documents", not "Cases"
search_opt[1].click()
search_form = browser.find_element_by_id("search-form")
search_form.submit()

entries_info = browser.find_elements_by_xpath(".//h4/span")[0].text
print entries_info
entries_amount = re.findall("(\d+)", entries_info)[0]
print entries_amount

last = browser.find_element_by_xpath(".//li[@class='last']/a")
last_url = last.get_attribute("href")
last_page = re.findall("(\d+)", last_url)[0]
print "Last page is %s" % (str(last_page))

page = 2
while page < last_page:
    # parse
    time.sleep(2)
    divs = browser.find_elements_by_xpath(".//div[@id='search-results-data']/div[@class='container-fluid well']")
    for div in divs:
        print div.text
    # click next page
    browser.find_element_by_xpath(".//a[@href='/main/SearchPager/page/" + str(page) + "']").click()
    page = page + 1





"""
##########################
from ghost import Ghost

g = Ghost()
session = g.start()
session.open("http://unsecret.rusarchives.ru/search")

g.fill("#search_form", {"Search[table]" : "docs"})
g.call("#search_form", "submit")

from grab import Grab

g = Grab()
result = g.go("http://unsecret.rusarchives.ru/")
# '//input[@name="YII_CSRF_TOKEN"]'
config = g.dump_config()
result = g.go("http://unsecret.rusarchives.ru/search",
              post={"Search[table]" : "docs"},
              headers={"YII_CSRF_TOKEN" : "b328e5a6f2c47f0c550dc456c79e799f9c10b5c7" }
              )
print result.unicode_body()

"""
