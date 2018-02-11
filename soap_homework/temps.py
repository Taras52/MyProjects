import osa


def avg_week_temp_convert(file_path):
    client = osa.Client('http://www.webservicex.net/ConvertTemperature.asmx?WSDL')
    with open(file_path) as f:
        temp_list = []
        for temp in f:
            temp = int(temp[:temp.find(' ')])
            temp_list.append(temp)
    avg_temp = client.service.ConvertTemp(sum(temp_list)/len(temp_list), 'degreeFahrenheit', 'degreeCelsius')
    print('Средняя температура за неделю {} C'.format(round(avg_temp, 2)))


avg_week_temp_convert('temps.txt')
