# Дана последовательность чисел. Получить список 
# уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
data = [1, 2, 3, 5, 1, 5, 3, 10]
unique=[]
a = [int(i) for i in data]
print(a)
for i in a:
   if a.count(i) == 1:
       unique.append(i)
print(unique)