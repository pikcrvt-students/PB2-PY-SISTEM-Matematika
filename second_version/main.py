
def create_user():
    usernames = []
    with open('users.txt', "r") as f:
        a = f.read().split()
        for i in range(len(a)):
            usernames.append(a[i].split(':')[0])
    username = input()
    while username in usernames:
        print('already registred')
        username = input()
    password = input()
    with open('users.txt', "a") as f:
        f.write(f"{username}:{password}\n")
    print('user is created')


def login():
    global username
    users = []
    passes = []
    with open('users.txt', "r") as f:
        a = f.read().split()
        for i in range(len(a)):
            users.append(a[i].split(':')[0])
            passes.append(a[i].split(':')[1])
    username = input()
    indexof = users.index(username)
    password = input()
    if password == passes[indexof]:
        print('logged')
    else:
        print('wrong password')
a = 0
while a != 3:
    a = int(input('do you want to login or register an user?'))
    while a == 1:
        create_user()
        a = int(input('do you want to login or register an user?'))
    while a == 2:
        login()
        a = 3
print(f"currently logged in as {username}")

