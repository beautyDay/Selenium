
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
  

