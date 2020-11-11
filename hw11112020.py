# retrieve data from a file
def getFile(fileName):
    file = open(fileName)
    return file.read()

def getObjects(jsonString):
    specSymbols = ('[', ']', '{', '}', ':', ',')

    parts = []
    value = ""
    for symbol in jsonString:
        tmpValue = value.strip()
        #print(symbol)
        if len(tmpValue) < 1 and symbol in specSymbols:
            parts.append(symbol)
        else:
            value += symbol

        if len(tmpValue) > 0:
            if symbol == "\"":
                parts.append(tmpValue[1:])
                value = ""
            elif symbol in (',', '}', ']') and "\"" not in value:
                parts.append(float(value[:-1]))
                parts.append(symbol)
                value = ""
    return parts

def parseArray(data):
    jsonArray = []
    data = data[1:]

    if data[0] == ']':
        return jsonArray, data[1:]

    while True:
        value, data = tryParseObject(data)
        jsonArray.append(value)

        if data[0] == ']':
            return jsonArray, data[1:]
        elif data[0] != ',':
            raise Exception('Expected comma after value')

        data = data[1:]


def parseObject(data):
    jsonObject = {}
    data = data[1:]

    if data[0] == '}':
        return jsonObject, data[1:]

    while True:
        key = data[0]

        if data[1] != ':':
            raise Exception('Expected colon after key')

        value, data = tryParseObject(data[2:])
        jsonObject[key] = value

        if data[0] == '}':
            return jsonObject, data[1:]
        elif data[0] != ',':
            raise Exception('Expected comma after value')

        data = data[1:]
    

def tryParseObject(data, root = False):
    if root and data[0] not in ('{', '['):
        raise Exception('Incorrect structure')

    result = (data[0], data[1:])
    if data[0] == '{':
        result = parseObject(data)
    elif data[0] == '[':
        result = parseArray(data)
    
    return result[0] if root else result


jsonString = getFile(r"C:\Users\Vitalina\Downloads\Car_Model_List_Full.json")
data = getObjects(jsonString)
data = tryParseObject(data, True)
print(data)
print(type(data))
allbrands = []

for i in data:
    if i['Make'] not in allbrands:
        allbrands.append(i['Make'])
        #print('Бренд: {}'.format(i['Make']))
print()
allbrands.sort(key=None, reverse=True)
for i in allbrands:
    print('Бренд: {}'.format(i))
brand = input('vvedite nazvanie avto: ')
name = input("vvedite im`ya: ")
yearFrom = int(input('vvedite god from: '))
yearTo = int(input('vvedite god to: '))

for i in data:
    if i['Make'] == brand:
        print('модель бренду: : {}'.format(i['Model']))
    if i['Model'] == name:
        print('Id: {}'.format(i['objectId']))
    if yearFrom <= i['Year'] and i['Year'] <= yearTo and i['Make'] == brand:
        print('всі моделі за проміжок часу: {}'.format(i['Model']))
print()
part = input('Enter part of Model or Maker: ')
for i in data:
    if i['Make'].find(part) != -1:
        print('{} знайдено у Бренді: {}'.format(part,i['Make']))
    if i['Model'].find(part) != -1:
        print('{} знайдено у моделі: {}'.format(part,i['Model']))

counter = 0
for i in data:
    if i['Make'] == brand:
        print(('модель бренду: : {}'.format(i['Model'])))
        counter += 1
    if counter == 5:
        input('nazmite enter dlya prodolzenya')
        counter = 0    

