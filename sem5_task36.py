# Дан список чисел. Создать список, в который попадают числа, 
# описываемые возрастающую последовательность. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. 
# Порядок элементов менять нельзя

data = [1, 5, 2, 3, 4, 6, 1, 7, 1, 9]
list=[]
list1=[]
for i in range(1, len(data)-1):
    if data[i] > data[i-1]:
        list.append(data[i-1])
for i in range(1, len(list)-1):
    if list[i] > list[i-1]:
        list1.append(list[i-1])
print(list1)