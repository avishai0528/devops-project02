from selenium import webdriver
from selenium.webdriver.common.by import By

gchrome = webdriver.Chrome(executable_path="C:\\Users\\aalgr\\ownCloud\\DevOps\\Python\\chromedriver_win32\\chromedriver.exe")

gchrome.get('http://127.0.0.1:5001/users/get_user_data/1')
user_name = gchrome.find_element(By.ID, 'user')
# Checking web element existence
print(user_name)
# Printing user name using locator
print(user_name.text)