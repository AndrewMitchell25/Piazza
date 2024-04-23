import requests

# Functions for each User action
def test_post(token):
    return requests.post('http://localhost:3000/post', json={
        'title': 'Sample Title',
        'topic': ['health', 'sport'],
        'message': 'Sample Message'
    }, headers={'auth-token': token}).json()

def test_get(token):
    return requests.get('http://localhost:3000/post', headers={'auth-token': token}).json()

def test_get_id(id, token):
    return requests.get(f'http://localhost:3000/post/{id}', headers={'auth-token': token}).json()

def test_delete(token):
    return requests.delete('http://localhost:3000/post/', headers={'auth-token': token}).json()

def test_delete_id(id, token):
    return requests.delete(f'http://localhost:3000/post/{id}', headers={'auth-token': token}).json()

def test_patch(id, new_title, new_topic, new_message, token):
    return requests.patch(f'http://localhost:3000/post/{id}', params={'postID': id}, json={'title':new_title, 'topic':new_topic, 'message':new_message}, headers={'auth-token': token}).json()

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
    
    print('- Register first user:', test_register("amitch27@nd.edu"))
    token = test_login("amitch27@nd.edu")['auth-token']
    print('- First user login token:', token)
    print('- Register second user:', test_register("kphan2@nd.edu"))
    token = test_login("kphan2@nd.edu")['auth-token']
    print('- Second user login token:', token)
    test_delete(token)
    print('- Database starts empty:', test_get(token))
    print('- POST without token:', test_post(""))
    print('- POST with invalid token:', test_post("123"))
    print('- POST with token:', test_post(token))
    print('- POST again with token:', test_post(token))
    print('- GET all without token:', test_get(""))
    print('- GET all with invalid token:', test_get("123"))
    print('- GET all with token:', test_get(token))
    first_ID = test_get(token)[0]['_id']
    print("- ID of first post: ", first_ID)
    print("- GET first post by ID: ", test_get_id(first_ID, token))
    print("- PATCH first post by ID without token: ", test_patch(first_ID, "New Title", "tech", "New Message", ""))
    print("- PATCH first post by ID with invalid token: ", test_patch(first_ID, "New Title", "tech", "New Message", "123"))
    print("- PATCH first post by ID with token: ", test_patch(first_ID, "New Title", "tech", "New Message", token))
    print("- GET all with token: ", test_get(token))
    print("- DELETE first post by ID without token: ", test_delete_id(first_ID, ""))
    print("- DELETE first post by ID with invalid token: ", test_delete_id(first_ID, "123"))
    print("- DELETE first post by ID with token: ", test_delete_id(first_ID, token))
    print("- GET all with token: ", test_get(token))
    test_delete(token)
    print("- DELETE all: ", test_get(token))
    