# Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k. 
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
k = 2
from random import randint
import random
a = random.randint(1, 100)
numbers = [a]
for i in range(k):
    numbers.append(randint(0, 10))
print(numbers)
if numbers[1] == 0:
    line1 = ('{0}x^{1} + {2} = 0'.format(numbers[0], k, numbers[2]))
elif numbers[2] == 0:
    line1 = ('{0}x^{1} + {2}x = 0'.format(numbers[0], k, numbers[1]))
else:
    line1 = ('{0}x^{1} + {2}x + {3} = 0'.format(numbers[0], k, numbers[1], numbers[2]))
with open('file33.txt', 'w') as data:
    data.write(line1)
