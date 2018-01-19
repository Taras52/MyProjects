import os

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    filelist = [f for f in os.listdir(os.path.join(current_dir, migrations)) if f.endswith('.sql')]
    while True:
        searching_data = input('Введите строку:')
        for file in filelist:
            with open(os.path.join(current_dir, migrations, file)) as f:
                data = f.read()
                if searching_data in data is False:
                    filelist.remove(file)
        for file in filelist:
            print(file)
        print('Всего', len(filelist))
    pass
