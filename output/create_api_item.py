
import requests

response = requests.post('https://example-api.com/items', json={'name': 'new_item'})
print(response.status_code)
