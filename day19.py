
# num=input("Enter the number: ")
# if(num!=""):
#     print(num)

# if(value:=input("Enter your name: "))!="":
#     print(value)

# line = input("Enter text (blank to stop): ")

# while line != "":
#     print("Line:", line)
#     line = input("Enter text (blank to stop): ")

# while (line := input("Enter text (blank to stop): ")) != "":
#     print("Line:", line)

import shutil
import os

# shutil.copytree("copyFolder", "newFolder")

# shutil.move("data.txt", "new_folder/backup.txt")

# shutil.rmtree("new_folder")

# shutil.make_archive("my_backup", "zip", "copyFolder")

# shutil.unpack_archive("my_backup.zip", "restored_folder")

# usage = shutil.disk_usage("/")
# print(f"Total: {usage.total}, Used: {usage.used}, Free: {usage.free}")

# l1=[i for i in range(11)]

# print(l1)

# def count_up_to(n):
#     i = 1
#     while i <= n:
#         yield i
#         i += 1

# gen = count_up_to(5)
# fisrt=next(gen)
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))

# # for number in gen:
# #     print(number)

# second=next(gen)

# import requests
# response = requests.get("https://jsonplaceholder.typicode.com/users")
# data = response.json()
# print(data)

# import requests
# payload = {'username': 'neeraj', 'password': '1234'}
# response = requests.post('https://httpbin.org/post', data=payload)
# print(response.status_code)
# print(response.json())

# import requests
# response = requests.get("https://httpbin.org/users")
# data = response.json()
# print(data)