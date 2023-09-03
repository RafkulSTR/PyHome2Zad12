S = int(input("Введите сумму чисел: "))
P = int(input("Введите произведение чисел: "))
numbers = []
for x in range(1, S):
        y = S - x
        if x * y == P:
            numbers =  [x, y]
if numbers:
    print("Задуманные числа: ", numbers[0], ",", numbers[1])
else:
    print("Числа не найдены")            

    