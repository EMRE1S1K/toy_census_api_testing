import requests
genders = ['male', 'female', 'genderless']

users = []

for gender in genders:
    response = requests.get(f'https://randomuser.me/api/?gender=100&gender={gender}')
    status_code = response.status_code
    assert status_code == 200, f'Status code does not match for gender: {gender}'

    json_response = response.json()
    results = json_response['results']

    users.extend(results)

action_type = 'CountByGender'

request_body = {
    'actionType': action_type,
    'users': users
}

toy_census_url = 'https://census-toy.nceng.net/prod/toy-census'
response = requests.post(toy_census_url, json=request_body)
status_code = response.status_code
assert status_code == 200, 'Status code does not match'

json_response = response.json()

gender_counts = sorted(json_response, key=lambda x: x['value'], reverse=True)
for gender_count in gender_counts:
    print(f"Gender: {gender_count['name']}, Count: {gender_count['value']}")
