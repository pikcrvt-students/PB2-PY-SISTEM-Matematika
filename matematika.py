from time import sleep
while True:
    print('выберите режим (1 - теория, 2 - задания, 3 - контрольная, 4 - выйти')
    choice = int(input())
    while choice == 1:
        print("----Теория----")
        sleep(1)
        print("Факториал - n!")
        sleep(1)
        print("""
        Факториал числа n — это произведение натуральных чисел от 1 до n. Обозначается n, произносится
        """)
        sleep(1)
        print('Факториал определен для целых неотрицательных чисел.')
        sleep(1)
        a = input('Всё понятно?')
        print('Вычисляется факториал по формуле: путем умножения всех чисел от одного до значения самого числа под факториалом. ')
        sleep(1)
        print('3! = 1*2*3 = 6')
        sleep(1)
        print('4! = 1*2*3*4 = 24')
        a = input('Всё понятно?')
        print('какой будет ответ в выражении 5!:')
        a = int(input())
        print('неправильно, ответ 120') if a != 120 else print('правильно!')
        print('выберите режим (1 - теория, 2 - задания, 3 - контрольная, 4 - выйти')
        choice = int(input())
    while choice == 2:
        print("----Задания----")
        sleep(1)
        print("Факториал - n!")
        sleep(1)
        print('какой будет ответ в выражении 5!:')
        a = int(input())
        print('неправильно, ответ 120') if a != 120 else print('правильно!')     
        print('какой будет ответ в выражении 4!:')
        a = int(input())
        print('неправильно, ответ 24') if a != 24 else print('правильно!')
        print('какой будет ответ в выражении 3!:')
        a = int(input())
        print('неправильно, ответ 6') if a != 6 else print('правильно!')
        print('выберите режим (1 - теория, 2 - задания, 3 - контрольная, 4 - выйти')
        choice = int(input())
    while choice == 3:
        correct = 0
        print("----Контрольная----")
        sleep(1)
        print("Факториал - n!")
        sleep(1)
        print('какой будет ответ в выражении 6!:')
        a = int(input())
        if a != 720:
            print('неправильно, ответ 720')
        else:
            print('правильно!')
            correct+=1
        print('какой будет ответ в выражении 3!:')
        a = int(input())
        if a != 6:
            print('неправильно, ответ 6')
        else:
            print('правильно!')
            correct+=1
        print('какой будет ответ в выражении 4!:')
        a = int(input())
        if a != 24:
            print('неправильно, ответ 24')
        else:
            print('правильно!')
            correct+=1
        print('какой будет ответ в выражении 0!:')
        a = int(input())
        if a != 1:
            print('неправильно, ответ 1')
        else:
            print('правильно!')
            correct+=1
        print('какой будет ответ в выражении -1!:')
        a = int(input())
        if a != 0:
            print('неправильно, ответ 0')
        else:
            print('правильно!')
            correct+=1
        print('тест пройден')
        sleep(1)
        print(f"вы набрали {correct} баллов из {5} ваша оценка {correct*2}")
        sleep(1)
        print('выберите режим (1 - теория, 2 - задания, 3 - контрольная, 4 - выйти')
        choice = int(input())
    print('вы вышли')
    break