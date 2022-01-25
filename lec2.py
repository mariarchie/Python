# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'w')
# data.writelines(colors)
# data.write('\nline 2')
# data.write('\nline 3')
# data.close()

# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# import lec as h
# print(h.f(1))

# def new_string(symbol, count = 3):
#     return symbol * count
# print (new_string('!', 5)) #!!!!!
# print (new_string('!')) #!!!
# print (new_string(4)) #12

# def concat(*params):
#     res: int = 0  #тип переменной указывать не обязательно
#     for item in params:
#         res+= item
#     return res
# print(concat(1, 2, 3, 4))

# Рекурсия
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)

# Кортежи - состоят из большого кол-ва координат - неизменяемый список
# a = (3, 4)
# # print(a)
# # print(a[-1])
# # a = (3,) #кортеж из одного элемента

# for item in a:
#     print(item)

# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue))  #r:red g:green b:blue

# Словари - неупорядоченные коллекции произвольных обьектов с доступом по ключу
# dictionary = {}
# # \ чтобы не писать все в одну строчку 
# dictionary = \
#     {
#         'up': '↑',
#         'left': '←',
#         'down': '↓',
#         'right': '→'
#     }
# print(dictionary)
# print(dictionary['left'])

# for k in dictionary.keys():  #up lesf down right
#     print(k)

# for k in dictionary.values():  #↑←↓→
#     print(k)

# Множества 'set'
# colors = {'red', 'green', 'blue'}
# print(type(colors))
# print(colors) #{'red', 'blue', 'green'}
# colors.add('red')
# print(colors) #{'red', 'blue', 'green'}
# colors.add('gray')
# print(colors) #{'red', 'blue', 'green', 'gray'}
# colors.remove('red')
# print(colors) 
# colors.clear()
# print(colors) 

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() #c = {1, 2, 3, 5, 8}
# u = a.union(b) #u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b) #i = {8, 2, 5}
# dl = a.difference(b) #dl = {1, 3}
# dr = b.difference(a) #dr = {13, 21}
# print (c, u, i, dl, dr)

# s = frozenset(a) 

list1 = [1,2,3,4,5]
print(list1.pop()) #извлекает и удаляет последний элемент из списка 
print(list1)
print(list1.pop(2)) #извлекает и удаляет третий элемент из списка 
print(list1.insert(2, 11)) #добавляет третьим элеменом число 11 
print(list1)
print(list1.append(11)) #добавляет в конец списка число 11 
print(list1)