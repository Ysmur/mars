from datetime import datetime

from requests import get, post

#print(get('http://localhost:5000/api/jobs').json())

#print(get('http://localhost:5000/api/jobs/2').json())

#print(get('http://localhost:5000/api/jobs/999').json())
# новости с id = 999 нет в базе

#print(get('http://localhost:5000/api/jobs/q').json())

# task 6

# print(post('http://localhost:5000/api/jobs',
#            json={'id': 10, 'job': 'installation of radiation protection'}).json())  # not full list of characters
# print(post('http://localhost:5000/api/jobs').json())  # empty request
# print(post('http://localhost:5000/api/jobs',
#            json={'id': 10, 'job': 'installing a long-distance communication antenna', 'team_leader': 4, 'work_size': 23,
#                  'collaborators': '6, 3, 8', 'category': 3, 'is_finished': True}).json())  # cool request
# print(get('http://localhost:5000/api/jobs').json())

print(get('http://localhost:5000/api/v2/users').json())
# print(post('http://localhost:5000/api/users',
#            json={'id': 10, 'job': 'installation of radiation protection'}).json())  # not full list of characters
# print(post('http://localhost:5000/api/jobs').json())  # empty request
print(post('http://localhost:5000/api/v2/users',
            json={'surname': 'Urna2',
                  'name': 'Ame',
                  'age': 25,
                  'position': 'marsolet',
                  'speciality': 'engineer',
                  'address': 'module_1',
                  'email': 'e2@mail.ru',
                  'hashed_password': '1234'
                  }).json())  # cool request
print(get('http://localhost:5000/api/v2/users').json())