# Дана последовательность чисел. 
# Получить список уникальных элементов заданной последовательности.

# data = [1, 4, 7, 8, 10, 3, 4, 7, 1, 1]
# j=1
# n=0
# a = len(data)-1
# for i in data:
#     j=n
#     while j < a:
        
#         if i == data[j]:
#             data.remove(i)
            
#         j=j+1
#     n=n+1    
# print(data)
data = [1, 4, 7, 8, 10, 3, 4, 7, 1, 1, 45]
def unique_numbers(data):
    list = []
    numbers = set(data)
    for n in numbers:
        list.append(n)
    return list
print(unique_numbers(data))
        

