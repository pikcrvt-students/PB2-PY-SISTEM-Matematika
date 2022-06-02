def recursion(a):
    if a == 1:
        print(f"средний элемент матрёшки с индексом {a}")
    else:
        print(f"верхний элемент матрёшки с индексом {a}")
        recursion(a-1)
        print(f"нижний элемент матрёшки с индексом {a}")

recursion(int(input()))