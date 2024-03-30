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


# Test driver
if __name__ == '__main__':
    test_delete()
    print("\tStart the test with no posts: ", test_get())
    test_post()
    test_post()
    print("\tAfter creating two posts: ", test_get())
    first_ID = test_get()[0]['_id']
    print("\tID of first post: ", first_ID)
    print("\tGet the first post by ID: ", test_get_id(first_ID))
    test_patch(first_ID, "New Title", "tech", "New Message")
    print("\tEdited the first post: ", test_get())
    test_delete_id(first_ID)
    print("\tDeleted the first post: ", test_get())
    test_delete()
    print("\tAll posts deleted: ", test_get())