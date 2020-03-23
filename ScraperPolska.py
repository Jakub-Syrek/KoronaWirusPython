import os
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
URL = "https://www.gov.pl/web/koronawirus/wykaz-zarazen-koronawirusem-sars-cov-2"

driver = webdriver.Chrome()
driver.get(URL)
driver.maximize_window()
driver.implicitly_wait(3)

links = driver.find_elements_by_xpath("//*[@id='tab-tables']")
if len(links) > 0:
    driver.execute_script("arguments[0].click();", links[0])    

driver.implicitly_wait(3)

links2 = driver.find_elements_by_css_selector("#js-pagination-rows > a:nth-child(3)")
actions = ActionChains(driver)
driver.implicitly_wait(3)
if len(links2) > 0:
    driver.execute_script("arguments[0].click();", links2[0])    
driver.implicitly_wait(3)

table = driver.find_element_by_class_name("results-container")
driver.implicitly_wait(3)
rows = table.find_elements_by_xpath('//td')

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

if os.path.exists("ConfirmedCasesPolskaDetails.txt"):
        file = open("ConfirmedCasesPolskaDetails.txt","r+")
        file.truncate(0)
        file.close()
 
currentRow = -1
for row in rows:   
    currentRow += 1         
            
    f= open(r"ConfirmedCasesPolskaDetails.txt","a",encoding="utf-8")
    if "zobacz szczegóły" not in row.text:
        if "".__ne__(str(row.text)):
            print(str(row.text))
            if is_integer(str(row.text)) and is_integer(str(rows[currentRow+1].text)).__eq__(False) and is_integer(str(rows[currentRow-1].text)).__eq__(False):
                f.write(row.text)
                f.write("\n")
                print("0")
                f.write("0")
                f.write("\n")
            else:
                f.write(row.text)
                f.write("\n")
                f.close()               
            

driver.quit()
