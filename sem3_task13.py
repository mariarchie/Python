# Пользователь задаёт две строки. Определить количество количество вхождений одной строки в другой
s1 = 'qwertqwerqwerqwqw'
s2 = 'qw'
index = s1.find(s2)
# print(index)
# pos = index + len(s2)
# print(pos)
# print(s1)
# s1 = s1[pos:]
# print(s1)
# print()

def counter(s1, s2):
    t = s1
    count = 0
    while len(t) != 0:
        index = t.find(s2)
        if (index != -1):
            count +=1
            t = t[index + len(s2):]
        else:
            break
    return count
print(counter(s1, s2))


