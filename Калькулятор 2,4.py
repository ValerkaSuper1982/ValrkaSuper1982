Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:13:28) [MSC v.1928 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
# Блок 2. Задача 4. Калькулятор
import math
import random
# ^ - возведение в степень, m - модуль, r - рандом, ! - факториал, ac - арккосинус
print('Возможные операторы: +, -, *, /')
print('^ - возведение в степень, m - модуль, r - рандом, ! - факториал, ac - арккосинус')
operator1 = input("Введите оператор : ")
if operator1 == 'r':
    print("Случайное число = ", random.uniform(-1000,1000))
else:
    number1 = float(input("Введите первое число : "))
    if operator1 == 'm':
        print("Модуль числа = ", abs(number1))
    elif operator1 == '!':
        number3 = int(abs(number1))
        print("Факториал определен на множестве целых неотрицательных чисел.")
        print("Поэтому посчитаем факториал от ", number3)
        print(number3, "! = ", math.factorial(number3))
    elif operator1 == 'ac':
        if number1 < -1 or number1 > 1:
            print("Аргумент должен быть в диапазоне от -1 до 1")
        else: print("Арккосинус", number1, "=", math.acos(number1), "рад")
    else:
        number2 = float(input("Введите второе число : "))
        if operator1 == '+':
            print("Сумма = ", number1 + number2)
        elif operator1 == '-':
            print("Разность = ", number1 - number2)
        elif operator1 == '*':
            print("Произведение = ", number1 * number2)
        elif operator1 == '/':
            if number2 == 0:
                print("На 0 делить нельзя!")
            else: print("Частное = ", number1 / number2)
        elif operator1 == '^':
            print(number1, "в степени", number2, "=", number1 ** number2)