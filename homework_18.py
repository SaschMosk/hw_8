import osa
import os

#task 1

# client = osa.Client('http://www.webservicex.net/ConvertTemperature.asmx?WSDL')
#
# def convert_to_C(data):
#     return round(client.service.ConvertTemp(data, FromUnit='degreeFahrenheit', ToUnit='degreeCelsius'), 2)
#
# tempo = []
# with open('temps.txt', 'r') as temps:
#     for line in temps:
#         tempo.append(int(line[0:1]))
# print(tempo)
#
#
# def mean_C(tempo):
#     tempo_C = []
#     for temp in tempo:
#         tempo_C.append(convert_to_C(temp))
#     return sum(tempo_C)/len(tempo_C)
#
# mean_C(tempo)

#task 2

client = osa.Client("http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL")

help(client.service)

expenses = []
with open('travel.txt', 'r') as travel:
    for line in travel:
        expenses.append(line)
print(expenses)

def convert_to_rubl(data):
    return client.service.ConvertToNum(data, FromCurrency=expenses['Currency'], toCurrency='RUB', amount=1000,
                                       rounding=True)

def calculate_expenses_rubl(expenses):
    for expense in expenses:
        convert_to_rubl(expense)
        return sum(expenses)

#task 3

