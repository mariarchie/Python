# Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число

lists = []
N = int(input('Введите N: '))
for i in range(-N, N+1):
    lists.append(i)
print(lists)

path = 'file.txt'   
data = open(path, 'r')
for line in data:
    print(line) 
data.close()


production = 1
for j in range(0, len(lists), 1):
    if j == int(line):
        production*= lists[j]
print(production)





    