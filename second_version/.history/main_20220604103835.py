# username = None

# def create_user():
#     usernames = []
#     with open('users.txt', "r") as f:
#         a = f.read().split()
#         for i in range(len(a)):
#             usernames.append(a[i].split(':')[0])
#     username = input()
#     while username in usernames:
#         print('already registred')
#         username = input()
#     password = input()
#     with open('users.txt', "a") as f:
#         f.write(f"{username}:{password}\n")
#     print('user is created')


# def login():
#     global username
#     users = []
#     passes = []
#     with open('users.txt', "r") as f:
#         a = f.read().split()
#         for i in range(len(a)):
#             users.append(a[i].split(':')[0])
#             passes.append(a[i].split(':')[1])
#     username = input()
#     while username not in users:
#         if username == 'exit':
#             return False
#         print('user is not registred, if you want to exit type "exit"')
#         username = input()
#     indexof = users.index(username)
#     password = input()
#     if password == passes[indexof]:
#         print('logged')
#         return True
#     else:
#         print('wrong password')    
# a = 0

# while username is None or a != 3:
#     a = int(input('do you want to login or register an user?'))
#     while a == 1:
#         create_user()
#         a = int(input('do you want to login or register an user?'))
#     while a == 2:
#         error = login()
#         if error:
#             a = 3
#         else:
#             a = int(input('do you want to login or register an user?'))
# print(f"currently logged in as {username}")


import os
from os.path import isfile, join
# All files and directories ending with .txt and that don't begin with a dot:

def create_theory():
    counter = 0
    filename = "theory"
    while os.path.isfile(f"theory/{filename}{counter}.txt"):
        counter += 1
    print(f"{filename}{counter}.txt")
    with open(f'theory/{filename}{counter}.txt', "w") as f:
        text = ""
        while text != "0":
            text = input("enter a line of text, if you want to stop writing, write 0")
            f.write(f"{text} \n")
    print('file created!')
        
def read_theory():
    mypath = "theory/"   
    onlyfiles = [f for f in os.listdir(mypath) if isfile(join(mypath, f))]


read_theory()