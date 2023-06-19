import requests

response = requests.get('https://randomuser.me/api/?results=100')
status_code = response.status_code
assert status_code == 200, 'Status code does not match'

json_response = response.json()
results = json_response['results']
action_type = 'CountPasswordComplexity'

users = []
for user in results:
    password = user['login']['password']
    complexity = sum(not char.isalnum() for char in password)
    users.append({'password': password, 'complexity': complexity})

request_body = {
    'actionType': action_type,
    'users': users
}

toy_census_url = 'https://census-toy.nceng.net/prod/toy-census'
response = requests.post(toy_census_url, json=request_body)
status_code = response.status_code
assert status_code == 200, 'Status code does not match'

json_response = response.json()

passwords_sorted = sorted(json_response, key=lambda x: x['complexity'], reverse=True)
for password_count in passwords_sorted:
    password = password_count['password']
    complexity = password_count['complexity']
    print(f"Password: {password}, Complexity: {complexity}")

