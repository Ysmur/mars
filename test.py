from requests import get, post

print(get('http://localhost:5000/api/jobs').json())

print(get('http://localhost:5000/api/jobs/2').json())

print(get('http://localhost:5000/api/jobs/999').json())
# новости с id = 999 нет в базе

print(get('http://localhost:5000/api/jobs/q').json())