#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#Без применения встроеных методов (арифметически)
#Пример:
#45 -> 101101
#3 -> 11
#2 -> 10
n = int(input("Введите десятичное число: "))
binary = ''
while n != 0:
    binary = str(n%2) + binary
    n //=2
print(f'Двоичное число: => {binary}')