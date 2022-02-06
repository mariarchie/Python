# Помните игру с конфетами из модуля "Математика и Информатика"? 
# Создайте такую игру для игры человек против человека
# Добавьте игру против бота
# Подумайте как наделить бота "интеллектом" 


N = int(input('Введите количество оставшихся кофет:  '))
M = int(input('Сколько конфет можно взять максимально:  '))
def CandyGame(N,M):
    if N<=M:
        res = 'Забирайте все конфеты, вы выиграли'   
    elif N % (M+1) == 0:
        res = 'Нет оптимального решения'    
    else:
        res = 'Возьмите {} конфет'.format(N % (M+1))
    return res
print(CandyGame(N, M))