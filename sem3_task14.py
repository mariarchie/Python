# Подсчитать сумму цифр в вещественном числе.

number = 1.48604
string_num = str(number)
total = 0
for i in string_num:
    if i == '.':
        total +=0
    else:
        total = total + int(i)
print(total)