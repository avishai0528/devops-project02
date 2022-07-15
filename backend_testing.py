import requests

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