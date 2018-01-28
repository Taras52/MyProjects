import os

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))

def search_data_in_file(input_data, search_list):
    aux_list = []
    for file in search_list:
        with open(os.path.join(current_dir, migrations, file)) as f:
            data = f.read()
            if input_data in data:
                aux_list.append(file)
    search_list = aux_list
    return search_list


if __name__ == '__main__':
    filelist = [f for f in os.listdir(os.path.join(current_dir, migrations)) if f.endswith('.sql')]
    while True:
        searching_data = input('Введите строку:')
        filelist = search_data_in_file(searching_data, filelist)
        for file in filelist:
            print(file)
        print('Всего', len(filelist))
