import requests
import json
api_response = requests.get('https://api.covid19india.org/state_district_wise.json')
print(type(api_response))

print(api_response.status_code)
data = api_response.json()
#print(data)

actives = data['Andaman and Nicobar Islands']['districtData']['South Andaman']['active']
print(actives)

deceased = data['Andaman and Nicobar Islands']['districtData']['South Andaman']['deceased']
print(deceased)