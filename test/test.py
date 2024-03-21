import requests


requests.post('http://localhost:3000/', json={
    'title': 'Hello World!'
})

print(requests.get('http://localhost:3000/').json())