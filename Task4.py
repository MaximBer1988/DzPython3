# 4.	Напишите программу, которая будет преобразовывать десятичное число в двоичное.
number = int(input("Введите число для преобразование в двоичное: "))
 
binary = ''
 
while number > 0:
    binary = str(number % 2) + binary
    number = number // 2
 
print(binary)
