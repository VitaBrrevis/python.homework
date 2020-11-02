import string
filename = input('vvedite file name: ')
fileptr = open(filename, "r")
text = fileptr.read()
textw = text.split ()
textw1 = textw.copy()
counter = 0

number = len(textw)
percent = (counter/number)*100

ar = []

x = len(textw[0])
e = textw[0]

qty_most_common = 0

for i in textw:
    ar.append(i[0])

for i in textw:
    if i[0] == 'z':
        counter += 1
    elif i[0] == 'Z':   
        counter += 1

    qty = ar.count(str.lower(i[0]))+ar.count(str.capitalize(i[0]))
    if qty > qty_most_common :
        qty_most_common = qty
        most_common = i[0]

    qty1 = len(i)
    if qty1 < x :
        x = qty1
        e = i

print('процент слов, начинающихся на "z": {}'.format(counter))
print('Чаще всего встречаются слова на букву: {}/{}'.format(str.lower(most_common), str.capitalize(most_common)))   
print('Самое короткое слово: {}'.format(e))

for i in textw:
    n = textw.index(i)
    if n%2:
      del textw[n]
print(*textw, sep = ' ')
textw1[-1], textw1[0] = textw[0], textw[-1]
print()
print(*textw1, sep = ' ')
