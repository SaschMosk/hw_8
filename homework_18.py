import osa

#task 1

client = osa.Client('http://www.webservicex.net/ConvertTemperature.asmx?WSDL')

def convert_to_C(data):
    return round(client.service.ConvertTemp(data, FromUnit='degreeFahrenheit', ToUnit='degreeCelsius'), 2)

tempo = dict()
with open('temps.txt') as f:
    temps_values = []
    for line in f:
        line = line.split(' ')
        temps_values.append(int(line[0]))

def mean_C(tempo):
    tempo_C = []
    for temp in tempo:
        tempo_C.append(convert_to_C(temp))
    return sum(tempo_C)/len(tempo_C)

print(mean_C(temps_values))

#task 2

client = osa.Client("http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL")

help(client.service)

expenses = dict()
with open('currencies.txt') as f:
    for line in f:
        line = line.split(' ')
        money = [line[1], line[2][0:3]]
        expenses[line[0]] = money

def convert_to_rubl(currency, amount):
    if currency in client.service.Currencies(licenseKey=''):
        return round(client.service.ConvertToNum(licenseKey='', fromCurrency=currency, toCurrency='RUB', amount=amount,
                                           rounding=True), 0)

def calculate_expenses_rubl(expenses_list):
    expenses_in_rubl = []
    for expense in expenses_list.items():
        expenses_in_rubl.append(convert_to_rubl(expense[1][1], expense[1][0]))
    return sum(expenses_in_rubl)

print(calculate_expenses_rubl(expenses))

#task 3

client = osa.Client('http://www.webservicex.net/ConvertLength.asmx?WSDL')

distances = dict()
with open('currencies.txt') as f:
    for line in f:
        line = line.split(' ')
        distances[line[0]] = line[1]
print(distances)

def convert_to_km(distance):
    return round(client.service.ChangeLengthUnit(distance, FromUnit='mi', ToUnit='km'), 2)

help(client.service)

def calculate_distance(distances):
    distances_in_km = []
    for distance in distances.items():
        distances_in_km.append(convert_to_km(distance[1]))
    return sum(distances_in_km)

print(calculate_distance(distances))