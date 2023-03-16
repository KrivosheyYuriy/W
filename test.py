from requests import get, post, delete

# print(get('http://localhost:8080/api/jobs').json())
# print(get('http://localhost:8080/api/jobs/1').json())
# print(get('http://localhost:8080/api/jobs/1454').json())
# print(get('http://localhost:8080/api/jobs/dsfdsfas').json())
# print(post('http://localhost:8080/api/jobs', json={'job': '123', 'work_size': 45}).json())
print(delete('http://localhost:8080/api/jobs/1').json())