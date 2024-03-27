import requests


def test_post():
    requests.post('http://localhost:3000/', json={
        'title': 'Give me another item!'
    })

    print(requests.get('http://localhost:3000/').json())

def test_delete():
    print(requests.get('http://localhost:3000/').json())
    x = requests.delete('http://localhost:3000/delete')
    print(requests.get('http://localhost:3000/').json())