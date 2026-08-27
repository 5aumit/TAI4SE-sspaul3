from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('https://www.convertworld.com/hu/homerseklet/celsius.html')


deg = input("Hőmérséklet=")
print(deg)
xpath = "//input[@name='amount']"
print(xpath)
driver.find_element(By.XPATH, xpath).send_keys(deg)
driver.find_element(By.XPATH, "//img[@alt='Átalakít']").click()

result = driver.find_element_by_id("value_3").text
print(result)

driver.quit()

