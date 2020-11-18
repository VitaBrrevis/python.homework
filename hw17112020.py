# retrieve data from a file
import random
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

jsonString = getFile(r"C:\Users\Vitalina\Downloads\Prices.json")
data = getObjects(jsonString)
data = tryParseObject(data, True)
priceslow = []
peiceshigh = []
brands = []
print('| name \t estimate |')
for i in data['prices']:
    print('| {} \t {}|'.format(i['display_name'], i['estimate']))
print()


category = input('vvedite kategoriyu: ')
road = int(input(' vvedite rastoyanie: '))
for i in data['prices']:
    if i['display_name'] == category:
        price = random.randint(i['low_estimate'], i['high_estimate'])
finalprice = road*price    
print(' categoriya - {}. cena - {}. total cena - {}'. format(category, price, finalprice))
input('Start')
counter = 100
while counter <= road*1000 :
    print('podolana vidstan` {}'.format(counter))
    input('press enter')
    counter += 50
print('pruyihalu')

print('cena = {}'.format(finalprice))


         


#print('name  Estimate /n {}  '.format(prices)