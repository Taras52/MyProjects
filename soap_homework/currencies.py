import osa


def travel_cost(file_path):
    client = osa.Client('http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?wsdl')
    with open(file_path) as f:
        costs = []
        amount = 0
        for way in f:
            trip = way.strip().split(' ')
            costs.append(trip)
            amount += client.service.ConvertToNum('', trip[2], 'RUB', int(trip[1]), False, '', '')
    return round(amount)


print('Общая сумма перелетов {} руб.'.format(travel_cost('currencies.txt')))
