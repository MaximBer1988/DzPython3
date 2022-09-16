# 3.	Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
list = [1.1, 1.2, 3.1, 5, 10.01]
list2=[]
i=0
while i < len(list):
  list[i]=round(list[i]%1,15)
  if list[i]>0:
    list2.append(list[i])
  i=i+1  
  
print(list2)
min_element=min(list2)
max_element=max(list2)
print(min_element)
print(max_element)
result=max_element-min_element
print(result)
