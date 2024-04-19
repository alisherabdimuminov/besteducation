import requests

# login
# url = "http://127.0.0.1:8000/api/auth/login/"
# data = {
#     "phone": "+998889107905",
#     "password": "123"
# }

# res = requests.post(url, data)
# print(res.text)

# # signup
# url = "http://127.0.0.1:8000/api/auth/signup/"
# data = {
#     "phone": "+998889107905",
#     "first_name": "Test user",
#     "last_name": "Test user",
#     "password": "123"
# }
# res = requests.post(url, data)
# print(res.text)

# users
url = "http://127.0.0.1:8000/api/auth/students/"
data = {
}
res = requests.get(url, headers={
    "Authorization": "Token be479f446e74941cc9ded72893d5ca7f5f44d5e8"
})
# print(res.text)

url = "http://127.0.0.1:8000/api/courses/"
data = {
}
res = requests.get(url, headers={
    "Authorization": "Token be479f446e74941cc9ded72893d5ca7f5f44d5e8"
})
# print(res.text)

url = "http://127.0.0.1:8000/api/courses/course/1/"
data = {
}
res = requests.get(url, headers={
    "Authorization": "Token be479f446e74941cc9ded72893d5ca7f5f44d5e8"
})
# print(res.text)

url = "http://127.0.0.1:8000/api/courses/course/1/lesson/1"
data = {
}
res = requests.get(url, headers={
    "Authorization": "Token be479f446e74941cc9ded72893d5ca7f5f44d5e8"
})
print(res.text)