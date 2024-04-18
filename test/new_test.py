import requests

# Functions for each User action
def test_post(token):
    requests.post('http://localhost:3000/post', json={
        'title': 'Sample Title',
        'topic': ['health', 'sport'],
        'message': 'Sample Message'
    }, headers={'auth-token': token})

def test_get(token):
    return requests.get('http://localhost:3000/post', headers={'auth-token': token}).json()

def test_get_id(id, token):
    return requests.get(f'http://localhost:3000/post/{id}').json()

def test_delete(token):
    requests.delete('http://localhost:3000/post/', headers={'auth-token': token})

def test_delete_id(id, token):
    requests.delete(f'http://localhost:3000/post/{id}')

def test_patch(id, new_title, new_topic, new_message, token):
    requests.patch(f'http://localhost:3000/post/{id}', params={'postID': id}, json={'title':new_title, 'topic':new_topic, 'message':new_message})

def test_register(email):
    return requests.post('http://localhost:3000/user/register', json={
        'username': "test",
        'email': email,
        'password': "supersecret"
    }).json()

def test_login(email):
    return requests.post('http://localhost:3000/user/login', json={
        'email': email,
        'password': "supersecret"
    }).json()
    
def test_delete_users(token):
    requests.delete('http://localhost:3000/user/', headers={'auth-token': token})    
    
# Test driver
if __name__ == '__main__':
    token = test_login("amitch27@nd.edu")['auth-token']
    test_delete_users(token)
    
    print(test_register("amitch27@nd.edu"))
    token = test_login("amitch27@nd.edu")['auth-token']
    print(token)
    print(test_register("kphan2@nd.edu"))
    token = test_login("kphan2@nd.edu")['auth-token']
    print(token)
    test_delete(token)
    print(test_get(token))
    test_post(token)
    