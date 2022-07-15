import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

gchrome = webdriver.Chrome(executable_path="C:\\Users\\aalgr\\ownCloud\\DevOps\\Python\\chromedriver_win32\\chromedriver.exe")

try:
    # Post JSON payload 'john' to id '1'
    res = requests.post('http://127.0.0.1:5000/users/1', json={"user_name":"john"})
    print(res.json())

    # step2 and step3 - checking that id 1 returns john and making sure john is under id 1
    res = requests.get('http://127.0.0.1:5000/users/1')
    print(res.json())
    compare_dict = dict(res.json())
    user_name1 = (compare_dict['user_name'])
    user_name_fixed = user_name1[0]
    if user_name_fixed == 'john':
        print('it is john')
    else:
        print('it is not john')

    gchrome.get('http://127.0.0.1:5001/users/get_user_data/1')
    user_name = gchrome.find_element(By.ID, 'user')
    # Checking web element existence
    print(user_name)
    # Printing user name using locator
    print(user_name.text)
    gchrome.quit()
except:
    print ('test failed')
