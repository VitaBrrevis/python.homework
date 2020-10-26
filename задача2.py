
number = input('напишите любое число: ')
digits = [int(item) for item in number]
numbers = [ ['один',  'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять'],
            ['десять','двадцять', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто'],
            ['сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'девятьсот']]
ten_to_twenty = ['одинадцять', 'дванадцять']

dlength = len(digits)
if dlength == 2 and digits[0] == 1:
    numstr = ten_to_twenty[digits[1]-1]
else:
    numstr = ''
    i=1
    for dig in digits:
        numstr = numstr+numbers[dlength-i][dig-1]+' '
        i=i+1
print(numstr)