import json

cName = input("Company Name: ")

with open('fb.json') as json_file:  
	data = json.load(json_file)
	for p in data['data']:
		if p['name'] == cName:
			print('Page Name: ' + p['name'])
			print('ID: ' + p['id'])
			print('Token: ' + p['access_token'])