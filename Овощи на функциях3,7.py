Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:13:28) [MSC v.1928 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Блок 3. Задача 7. Овощи на функциях
def nameLower(name):
    print(name.lower())


def nameUpper(name):
    print(name.upper())


def nameTitle(name):
    print(name.title())


def outSum(name, count):
    print('{} - {} кг.'.format(name.title(), count))


vegetable1 = input("Введите название 1-го овоща: ")
vegetable2 = input("Введите название 2-го овоща: ")
vegetable3 = input("Введите название 3-го овоща: ")

nameLower(vegetable1)
nameUpper(vegetable1)
nameTitle(vegetable1)

nameLower(vegetable2)
nameUpper(vegetable2)
nameTitle(vegetable2)

nameLower(vegetable3)
nameUpper(vegetable3)
nameTitle(vegetable3)

countVegetable1 = input("Введите количество 1-го овоща: ")
countVegetable2 = input("Введите количество 2-го овоща: ")
countVegetable3 = input("Введите количество 3-го овоща: ")

outSum(vegetable1, countVegetable1)
outSum(vegetable2, countVegetable2)
outSum(vegetable3, countVegetable3)