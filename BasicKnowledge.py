
cheese = driver.find_element_by_id("cheese")
cheddar = cheese.find_elements_by_id("cheddar")

driver.find_element_by_css_selector("#cheese #cheddar")

mucho_cheese = driver.find_elements_by_css_selector("#cheese li")

driver.find_element_by_name("name").send_keys(name)

driver.find_element_by_css_selector("input[type='submit']").click()

driver.find_element_by_link_text("new window").click()

driver.switch_to.window(window_handle)

locator:
class name
css selector
id
name
link text
tag name
xpath
  
driver.current_url
driver.back()
driver.forward()
driver.refresh()
driver.close()
driver.quit()  # 关闭当前所有windows和tabs
driver.title
driver.current_window_handle
driver.window_handles


# unittest teardown
# https://docs.python.org/3/library/unittest.html?highlight=teardown#unittest.TestCase.tearDown
def tearDown(self):
    self.driver.quit()
-----------------------------------------------
# clean up the WebDriver session
try:
    #WebDriver code here...
finally:
    driver.quit()
    
 -----------------------------------------------  
#Python’s WebDriver now supports the python context manager, which when using the with keyword can automatically quit the driver at the end of execution
with webdriver.Firefox() as driver:
  # WebDriver code here...

# WebDriver will automatically quit after indentation
-----------------------------------------------------

<div id="modal">
  <iframe id="buttonframe" name="myframe"  src="https://seleniumhq.github.io">
   <button>Click here</button>
 </iframe>
</div>


# Store iframe web element
iframe = driver.find_element_by_css_selector("#modal > iframe")

# switch to selected iframe
driver.switch_to.frame(iframe)

# Now click on button
driver.find_element_by_tag_name('button').click()
  
---------------------------------------------------------
# switch back to default content
driver.switch_to.default_content()

----------------------------------------------------------
# Access each dimension individually
width = driver.get_window_size().get("width")
height = driver.get_window_size().get("height")

# Or store the dimensions and query them later
size = driver.get_window_size()
width1 = size.get("width")
height1 = size.get("height")

-----------------------------------------------------------
driver.set_window_size(1024, 768)

------------------------------------------------------------
driver.maximize_window()

------------------------------------------------------------
driver.minimize_window()

------------------------------------------------------------
driver.fullscreen_window()

------------------------------------------------------------
driver.implicitly_wait(10)

------------------------------------------------------------
JavaScript alerts, prompts and confirmations
# Click the link to activate the alert
driver.find_element_by_link_text("See an example alert").click()

# Wait for the alert to be displayed and store it in a variable
alert = wait.until(expected_conditions.alert_is_present())

# Store the alert text in a variable
text = alert.text

# Press the OK button
alert.accept()

***************************************************************
# Click the link to activate the alert
driver.find_element_by_link_text("See a sample confirm").click()

# Wait for the alert to be displayed
wait.until(expected_conditions.alert_is_present())

# Store the alert in a variable for reuse
alert = driver.switch_to.alert

# Store the alert text in a variable
text = alert.text

# Press the Cancel button
alert.dismiss()

*****************************************************************
# Click the link to activate the alert
driver.find_element_by_link_text("See a sample prompt").click()

# Wait for the alert to be displayed
wait.until(expected_conditions.alert_is_present())

# Store the alert in a variable for reuse
alert = Alert(driver)

# Type your message
alert.send_keys("Selenium")

# Press the OK button
alert.accept()

--------------------------------------------------------------------
from selenium import webdriver

PROXY = "<HOST:PORT>"
webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
    "httpProxy": PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,
    "proxyType": "MANUAL",

}

with webdriver.Firefox() as driver:
    # Open URL
    driver.get("https://selenium.dev")
    
---------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options)
# Navigate to url
driver.get("http://www.google.com")
driver.quit()

----------------------------------------------------------------------
Find Element From Element

driver = Firefox()
driver.get("http://www.google.com")
search_form = driver.find_element_by_tag_name("form")
search_box = search_form.find_element_by_name("q")
search_box.send_keys("webdriver")
 
-----------------------------------------------------------------------
The keyDown is used to simulate action of pressing a modifier key(CONTROL, SHIFT, ALT)


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()

# Navigate to url

driver.get("http://www.google.com")

# Enter "webdriver" text and perform "ENTER" keyboard action

driver.find_element_by_name("q").send_keys("webdriver"+Keys.ENTER)

# Perform action ctrl + A (modifier CONTROL + Alphabet A) to select the page

webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").perform()

*******************************************************************************

from selenium import webdriver
driver = webdriver.Chrome()

# Navigate to url

driver.get("http://www.google.com")
# Store 'SearchInput' element

SearchInput = driver.find_element_by_name("q")
SearchInput.send_keys("selenium")
# Clears the entered text

SearchInput.clear()
 
*********************************************************************************

from selenium import webdriver

driver = webdriver.Chrome()

# Navigate to url
driver.get("http://www.example.com")

driver.add_cookie({"name": "test1", "value": "cookie1"})
driver.add_cookie({"name": "test2", "value": "cookie2"})

# Get all available cookies
print driver.get_cookies()

---------------------------------------------------------------------------------


  

