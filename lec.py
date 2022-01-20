s = 'hello "world'
s1 = 'hello \'world'
s2 = 'hello \nworld'
value = None
a = 123 
b = 1.23
#print (a)
#print (b)

#print(type(value))
#print(type(a))
#print(type(b))
#print(s) #вывод строки
#print(s1)
#print(s2)

#print ('{} - {} - {}'.format(a, b, s))
##print (a, "-", b, '-', s)
#print (f'{a} - {b} - {s}')
#print ('{2} - {0} - {1}'.format(a, b, s))

#list = ['1', '2', '3']
#print (list)

#print ('Введите а')
#a = int(input())
#print ('Введите b')
#b = int(input())
#print (a, '+', b, '=', a+b)

#d = 1 < 4 or 5 > 7 > 3
#print (d)

a = int(input('a = '))
b = int(input('b = '))
if a > b:
    print(a)
else:
    print(b)

for i in 1,2,3,4,5:
    print(i**2)

for j in range (1, 10, 2):
    print(j)

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return
arg = 2.3
print(f(arg))
print(type(f(arg)))