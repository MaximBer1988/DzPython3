# 2.	Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
list = [2, 3, 4, 5, 6]
new_list=[]
i=0
length=len(list)/2

while i <= length:
  mult=list[i]*list[len(list)-1-i]
  print(mult)
  new_list.append(mult)
  i=i+1
print(new_list)  
