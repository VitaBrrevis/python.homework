import string
text = input('введите текст: ')
textl = list(text)
counter = 0
for i in textl:
    if i == '.' or i == '!' or i == '?' :
        counter += 1
print('колл-во предлодений в тексте: {}'.format(counter))    
textw = text.split ()
counter1 = 0
for u in textw:
    if u == 'quis' :
        counter1 += 1
print('колл-во слова quis: {}'.format(counter1)) 
counter2 = 0
for o in textl:
    if o != ' ':
        counter2 += 1
print('колл-во  символов без пробелов: {}'.format(counter2)) 
print('колл-во  символов с пробелами: {}'.format(len(textl))) 
text120 = text[0:119]

if (textl[120] in string.ascii_lowercase or textl[120] in string.ascii_uppercas) and \
    (textl[119] in string.ascii_lowercase or textl[119] in string.ascii_uppercas):
    last_space = text120.rfind(' ')
    text120 = text[0 : last_space]

print( text120 + '...')
