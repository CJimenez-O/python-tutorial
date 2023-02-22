# Selenium Tutorial

import os
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
options_current = Options()
options_current.add_argument("log-level=3") 

driver = webdriver.Chrome(PATH, options=options_current)
driver.minimize_window()
driver.get("https://www.techwithtim.net/")


# print(driver.title)


# search = driver.find_element(by=By.NAME, value='s')
# search.send_keys('test')
# search.send_keys(Keys.RETURN)



# -------- CSS Selector --------
h1 = driver.find_element(By.CSS_SELECTOR,".siteorigin-widget-tinymce h1")
# print(h1.get_attribute('style')) #output: text-align: center
# print(h1.text)

# ------- xpath  ---------
el = driver.find_element(By.XPATH, value='//*[@id="panel-6-0-0-0"]/div/div/h1')
# print(el.text)

# ---------- All matching elements --------
elements = driver.find_elements(By.TAG_NAME, 'h1')

for item in elements:
    print(item.text)

# --------- Buttons ----------
# submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
# submit_button = driver.find_element(by=By.CLASS_NAME, value="ow-button-hover")
# submit_button.click()


# --------- get css value ----------
# cssValue = driver.find_element(By.LINK_TEXT, "More information...").value_of_css_property('color')



# --------- cookies ----------
#  Deletes all cookies
driver.delete_all_cookies()
# Adds the cookie into current browser context
driver.add_cookie({"name": "foo", "value": "bar"})

# Get cookie details with named cookie 'foo'
# print(driver.get_cookie("foo"))
# print(driver.get_cookies())


#  ---------- windows -------
   # Opens a new tab and switches to new tab
# driver.switch_to.new_window('tab')

    # Opens a new window and switches to new window
# driver.switch_to.new_window('window')


# -- add before driver.get()
# minimize
# driver.minimize_window()

# fullscreen
# driver.fullscreen_window()

# Returns and base64 encoded string into image
driver.save_screenshot('./image.png')
# h1.screenshot('./title.png')  # takes ss of only element




# get performance
driver.execute_cdp_cmd('Performance.enable', {})
t = driver.execute_cdp_cmd('Performance.getMetrics', {})
print(t)

# time.sleep(20) # wait 20 seconds


driver.quit()

