# Написать программу, получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

def fact(n):
    i = 1
    list = []
    res = 1
    while i <= n:
        res = i*res
        i+=1
        list.append(res)
    return list

print(fact(12))

