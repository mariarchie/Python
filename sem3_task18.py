# Реализовать алгоритм перемешивания списка. 
# алгоритм Фишера – Йейтса
import random
def MIX(list):
    for i in range (len(list)-1, 0, -1):
        j = random.randint(0, i + 1)
        k = list[i]
        list[i] = list[j]
        list[j] = k
    return list
print(MIX([1, 3, 6, 9, 3, 5, 8, 1, 5, 6]))