# Для натурального N создать словарь индекс-значение, 
# состоящий из элементов последовательности 3k + 1.
# Для N = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
def DICTIONARY(N):
    list = []
    for N in range(1, N+1):
        DICTIONARY = {N: 3*N+1}
        N+=1
        list.append(DICTIONARY)
    return(list)
print(DICTIONARY(6))
