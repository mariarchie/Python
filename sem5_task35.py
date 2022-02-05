# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие 
# A[i] - 1 = A[i-1]. Найти его.
path = 'file35.txt'
data = open(path, 'r')
for line in data:
    a = line.split()
data.close()
for i in range(0, len(a)-1):
    if int(a[i]) != int(a[i+1])-1:
        print(int(a[i])+1)
            


        

