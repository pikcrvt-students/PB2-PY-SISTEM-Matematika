import os
from os.path import isfile, join
from time import sleep

username = None

def register():
    usernames = []
    with open('users/users.txt', "r") as f:
        a = f.read().split()
        for i in range(len(a)):
            usernames.append(a[i].split(':')[0])
    username = input("enter an username: ")
    while username in usernames:
        print('already registred')
        username = input("enter an username: ")
    password = input("enter a password: ")
    with open('users/users.txt', "a") as f:
        f.write(f"{username}:{password}\n")
    print('user is created')
    with open(f'users/{username}.txt', "a") as f:
        f.write(f"{username}_file\n")


def login():
    global username
    users = []
    passes = []
    with open('users/users.txt', "r") as f:
        a = f.read().split()
        for i in range(len(a)):
            users.append(a[i].split(':')[0])
            passes.append(a[i].split(':')[1])
    username = input("enter an username: ")
    while username not in users:
        if username == 'exit':
            return False
        print('user is not registred, if you want to exit type "exit"')
        username = input("enter an username: ")
    indexof = users.index(username)
    password = input("enter a password: ")
    if password == passes[indexof]:
        print('logged')
        return True
    else:
        print('wrong password')    


def create_theory():
    counter = 0
    filename = "theory"
    while os.path.isfile(f"theory/{filename}{counter}.txt"):
        counter += 1
    print(f"{filename}{counter}.txt")
    with open(f'theory/{filename}{counter}.txt', "w") as f:
        text = ""
        while text != "stop":
            text = input("enter a line of text, if you want to stop writing, write stop")
            f.write(f"{text} \n")
    print('file created!')
        
def read_theory():
    mypath = "theory/"   
    onlyfiles = [f for f in os.listdir(mypath) if isfile(join(mypath, f))]
    for i in onlyfiles:
        print(i)
    counter = int(input("select theory "))
    while not os.path.isfile(f"theory/theory{counter}.txt"):
        print('theory not found')
        counter = int(input("select theory "))
    with open(f"theory/theory{counter}.txt", "r") as f:
        for i in f.read().split("\n"):
            print(i)
            sleep(1)

def create_exercises():
    counter = 0
    filename = "exercise"
    while os.path.isfile(f"exercises/{filename}{counter}.txt"):
        counter += 1
    print(f"{filename}{counter}.txt")
    with open(f'exercises/{filename}{counter}.txt', "w") as f:
        text = ""
        while text != "stop":
            text = input("enter an exercise, if you want to stop writing, write stop ")
            if text != "stop":
                answer = input("enter an answer ")
                f.write(f"{text}:{answer}\n")
            else:
                f.write(f"{text}\n")
            
    print('file created!')

def read_exercises():
    mypath = "exercises/"   
    onlyfiles = [f for f in os.listdir(mypath) if isfile(join(mypath, f))]
    for i in onlyfiles:
        print(i)
    counter = int(input("select exercise "))
    while not os.path.isfile(f"exercises/exercise{counter}.txt"):
        print('exercise not found')
        counter = int(input("select exercise "))
    questions = []
    answers = []
    with open(f"exercises/exercise{counter}.txt", "r") as f:
        a = f.read().split()
        print(a)
        for i in range(len(a)-1):
            questions.append(a[i].split(':')[0])
            answers.append(a[i].split(':')[1])
    max_answers = len(answers)
    count = 0
    for i in range(max_answers):
        print(questions[i])
        answer = input('enter answer ')
        if answers[i] == answer:
            print('correct!')
            count +=1
        else:
            print(f'incorrect!, answer is {answers[i]}')
            count = count
    print()    
        

def create_test():
    counter = 0
    filename = "test"
    while os.path.isfile(f"test/{filename}{counter}.txt"):
        counter += 1
    print(f"{filename}{counter}.txt")
    with open(f'test/{filename}{counter}.txt', "w") as f:
        text = ""
        while text != "stop":
            text = input("enter an exercise, if you want to stop writing, write stop ")
            if text != "stop":
                answer = input("enter an answer ")
                f.write(f"{text}:{answer}\n")
            else:
                f.write(f"{text}\n")
            
    print('file created!')

def read_test():
    mypath = "test/"   
    onlyfiles = [f for f in os.listdir(mypath) if isfile(join(mypath, f))]
    for i in onlyfiles:
        print(i)
    counter = int(input("select test "))
    while not os.path.isfile(f"test/test{counter}.txt"):
        print('test not found')
        counter = int(input("select test "))
    questions = []
    answers = []
    with open(f"test/test{counter}.txt", "r") as f:
        a = f.read().split()
        for i in range(len(a)-1):
            questions.append(a[i].split(':')[0])
            answers.append(a[i].split(':')[1])
    max_answers = len(answers)
    count = 0
    for i in range(max_answers):
        print(questions[i])
        answer = input('enter answer ')
        if answers[i] == answer:
            count +=1
        else:
            count = count
    print(f"you scored {count} points out of {max_answers}, your grade is {round(count/max_answers*10)}")
    with open(f'users/{username}.txt', "r") as f:
        read = f.read()
        if f"test{counter}" in read:
            pass
        else:
            with open(f'users/{username}.txt', "a") as a:
                a.write(f"test{counter} completed: grade = {round(count/max_answers*10)}\n")




a = 0
while True:
    while username is None or a != 3:
        try:
            a = int(input('do you want to login or register an user? (ctrl + c to exit) '))
            while a == 2:
                register()
                a = int(input('do you want to login or register an user? (ctrl + c to exit) '))
            while a == 1:
                error = login()
                if error:
                    a = 3
                else:
                    a = 0
        except ValueError:
            print('Value Error')
    print(f"currently logged in as {username}")

    if username == "teacher":
        try:
            while a == 1 or a == 2 or a == 3:
                print("whether you want to create a theory, exercises, test or logout (1, 2, 3, 4) ")
                a = int(input())
                if a == 1:
                    create_theory()
                elif a == 2:
                    create_exercises()
                elif a == 3:
                    create_test()
                else:
                    username = None
        except ValueError:
            print('Value Error')
    else:
        try:
            while a == 1 or a == 2 or a == 3:
                print("whether you want to read a theory, exercises, test or logout (1, 2, 3, 4) ")
                a = int(input())
                if a == 1:
                    read_theory()
                elif a == 2:
                    read_exercises()
                elif a == 3:
                    read_test()
                else:
                    username = None
        except ValueError:
            print('Value Error')
