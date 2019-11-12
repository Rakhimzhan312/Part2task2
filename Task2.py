print('Введите количество студентов:')
students = int(input())
print('Введите количество яблок:')
apples = int(input())
rest = apples % students
kazhdomu = apples // students
print('Остаток яблок:', rest , 'Досталось каждому студенту:', kazhdomu)


