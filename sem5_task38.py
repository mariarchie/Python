# Напишите программу, удаляющую из текста все слова содержащие "абв".
text = 'абволрп фражр олабв ужгрпж кол абв аорвп'
text2 = text.split()
print(*filter(lambda x:not'абв' in x, text2))



