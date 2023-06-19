import requests

response = requests.get('https://randomuser.me/api/?results=100')
status_code = response.status_code
assert status_code == 200, 'Status code does not match'

json_response = response.json()
results = json_response['results']

action_type = 'CountByCountry'

users = []
for user in results:
    country = user['location']['country']
    users.append({'country': country})

request_body = {
    'actionType': action_type,
    'users': users
}

# Step 3: Send the request to the Toy Census API
toy_census_url = 'https://census-toy.nceng.net/prod/toy-census'
response = requests.post(toy_census_url, json=request_body)
status_code = response.status_code
assert status_code == 200, 'Status code does not match'

# Step 4: Process the response from the Toy Census API
json_response = response.json()

# Step 5: Extract and print the count of each country in descending order
country_counts = sorted(json_response, key=lambda x: x['value'], reverse=True)
for country_count in country_counts:
    print(f"Country: {country_count['name']}, Count: {country_count['value']}")
