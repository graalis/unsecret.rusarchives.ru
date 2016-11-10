from selenium import webdriver
import re
import time

chrome_path=r"D:\ALEX\Downloads\chromedriver_win32\chromedriver.exe"

browser = webdriver.Chrome(chrome_path)
browser.get("http://unsecret.rusarchives.ru/search")
search_opt = browser.find_elements_by_xpath(".//select[@id='Search_table']/option")

# find "Documents", not "Cases"
search_opt[1].click()
search_form = browser.find_element_by_id("search-form")
search_form.submit()

# how many entries there are
entries_info = browser.find_elements_by_xpath(".//h4/span")[0].text
print entries_info
entries_amount = re.findall("(\d+)", entries_info)[0]
entries_amount = int(entries_amount)

# find last page
last = browser.find_element_by_xpath(".//li[@class='last']/a")
last_url = last.get_attribute("href")
last_page = re.findall("(\d+)", last_url)[0]
print "Last page is %s" % (str(last_page))

# iterate through pages
page = 2
while page < last_page:
    # parse
    time.sleep(2)
    sources = browser.find_elements_by_xpath(".//*[@id='search-results-data']/div[1]/div/div/p")
    for smth in sources:
        new_smth = smth.get_attribute("innerHTML").split("<br>")
        header = new_smth[0].split("</b>:")[1]
        print "Header: " + header
        date = new_smth[1].split("</b>:")[1]
        print "Date: " + date
        address = re.sub("\n", "", new_smth[2])
        address = address.replace("  ", "")
        print "Address: " + address
        fond = new_smth[3].split("</b>:")[1]
        print "Fond: " + fond
        unsecret_year = re.findall("(\d+)", new_smth[4])[0]
        print "Unsecreted in: " + unsecret_year
        
        print "=="
    """
    time.sleep(2) # todo: https://davidwalsh.name/document-readystate
    divs = browser.find_elements_by_xpath(".//div[@id='search-results-data']/div[@class='container-fluid well']")
    for div in divs:
        # print div.text
        items = div.find_element_by_xpath(".//p[@class='mb0']")
        print items.find_element_by_xpath(".//*[@id='search-results-data']/div[1]/div/div/p/text()[2]")
        # print items.get_attribute("innerHTML")
    """
    """for item in items:
            print item.text"""
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
