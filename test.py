from requests import get, post, delete

# print(get('http://localhost:5000/api/v2/users').json())
#
# print(get('http://localhost:5000/api/v2/users/2').json())
#
# print(get('http://localhost:5000/api/v2/users/999').json())
# # user с id = 999 нет в базе
#
# print(get('http://localhost:5000/api/v2/users/q').json())

# task 6
print(post('http://localhost:5000/api/jobs',
           json={'id': 17, 'job': 'inst an antenna', 'team_leader': 4, 'work_size': 23,
                 'collaborators': '6, 3, 8', 'category': 3, 'is_finished': True}).json())


# print(post('http://localhost:5000/api/v2/users',
#            json={'name': 'installation of radiation protection'}).json())  # not full list of characters
# print(post('http://localhost:5000/api/v2/users').json())  # empty request

# print(post('http://localhost:5000/api/v2/users',
#             json={'surname': 'Urna2',
#                   'name': 'Ame',
#                   'age': 25,
#                   'position': 'marsolet',
#                   'speciality': 'engineer',
#                   'address': 'module_1',
#                   'email': 'e2@mail.ru',
#                   'hashed_password': '1234'
#                   }).json())  # cool request

# print(delete('http://localhost:5000/api/v2/users/4').json())
# # print(get('http://localhost:5000/api/v2/users').json())