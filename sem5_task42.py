# Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# входные и выходные данные хранятся в отдельных файлах
path = 'file42.txt'
data = open(path, 'r')
for line in data:
    a = line
data.close()
def encode(a):
    encoded_message=''
    i = 0
    while (i <= len(a)-1):
        count = 1
        ch = a[i]
        j = i
        while (j < len(a)-1):
            if (a[j] == a[j+1]):
                count = count+1
                j = j+1
            else:
                break
        encoded_message+=str(count)+ch
        i = j+1
    return encoded_message
with open('file42out.txt', 'w') as f:
    print(encode(a), file = f)
