import requests

# Functions for each User action
def test_post():
    requests.post('http://localhost:3000/post', json={
        'title': 'Sample Title',
        'topic': ['health', 'sport'],
        'message': 'Sample Message'
    })

def test_get():
    return requests.get('http://localhost:3000/post').json()

def test_get_id(id):
    return requests.get(f'http://localhost:3000/post/{id}').json()

def test_delete():
    requests.delete('http://localhost:3000/post/')

def test_delete_id(id):
    requests.delete(f'http://localhost:3000/post/{id}')

def test_patch(id, new_title, new_topic, new_message):
    requests.patch(f'http://localhost:3000/post/{id}', params={'postID': id}, json={'title':new_title, 'topic':new_topic, 'message':new_message})

def test_register():
    return requests.post('http://localhost:3000/user/register', json={
        'username': "AndrewM",
        'email': "amitch27@nd.edu",
        'password': "supersecret"
    })

def test_login():
    return requests.post('http://localhost:3000/user/login', json={
        'email': "amitch27@nd.edu",
        'password': "supersecret"
    })
    
# Test driver
if __name__ == '__main__':
    print(test_login().json())
    print(test_get())