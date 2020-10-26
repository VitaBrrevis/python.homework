date = input("введите дату вида : ")

number_of_days = {'01' : '31', '02' : '28', '03' : '31', '04' : '30', '05' : '31', '06' : '30', '07' : '31', '08' : '31', '09' : '30', '10' : '31', '11' : '30', '12' : '31'}
name_of_mounth= {'01' : 'Январе', '02' : 'Феврале', '03' : 'Марте', '04' : 'Апреле',
 '05' : 'Мае', '06' : 'Июне', '07' : 'Июле', '08' : 'Августе', '09' : 'Сентябре', '10' : 'Октябре', '11' : 'Ноябре', '12' : 'Декабре'}
data = list(date)
data.remove('-')
data.remove('-')

data[0]=data[0]+data[1]

data[1]=data[2]+data[3]
data[2]=data[4]+data[5]+data[6]+data[7]
if int(data[2])%4 == 0:
    number_of_days['02'] = '29' 
  
print('в {1} {2} года дней {0}'.format(number_of_days[data[1]], name_of_mounth[data[1]], data[2])) 
code_of_month = {'01' : 1, '02' : 4, '03' : 4, '04' : 0, '05' : 2, '06' : 5, '07' : 0, '08' : 3, '09' : 6, '10' : 1, '11' : 4, '12' : 6}
year = list(data[2])
code_of_the_year = ((6 + int(year[2]+year[3])+(int(year[2]+year[3])//4))%7)
day = ((int(data[0])+(code_of_month[data[1]])+code_of_the_year)%7)

if day == 1 or day == 0:
    print('{2}.{1}.{0} - выходной'.format(data[2], data[1], data[0]))
else:
    print ('{2}.{1}.{0} - рабочий'.format(data[2], data[1], data[0]))     