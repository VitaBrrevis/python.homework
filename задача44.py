from random import randint
ar = []
i = 1
till = int(input('Веедіть диапазон чисел: '))
for j in range(20):
    ar.append(randint(0,till)*i)
    i = i * -1 
print(ar)
while True:
    answer = input('Ввведите число: ')
    if answer == 'Goodbye':
        break
    number = int(answer)
    print('Число {} повторяется в массиве {} раз'.format(number, ar.count(number)))