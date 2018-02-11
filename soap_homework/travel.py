import osa


def travel_length(file_path):
    client = osa.Client('http://www.webservicex.net/length.asmx?WSDL')
    with open(file_path) as f:
        amount = 0
        for way in f:
            trip = way.strip().split(' ')
            amount += float(trip[1].replace(',', ''))
    return round(client.service.ChangeLengthUnit(amount, 'Miles', 'Kilometers'))


print('Общая длина перелетов {} км'.format(travel_length('travel.txt')))
