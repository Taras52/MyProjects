meals = {}
with open('dishes.txt') as f:
    for line in f:
        key_meal = line.strip().lower()
        meals[key_meal] = []
        meals_number = f.readline()
        ing_number = int(meals_number)
        i = 1
        ing_list_total = []
        while i <= ing_number:
            ing_list = f.readline().strip()
            ing_list = list(ing_list.split(' | '))
            ing_list[1] = int(ing_list[1])
            ing_dict = {'ingridient_name': ing_list[0], 'quantity': ing_list[1], 'measure': ing_list[2]}
            ing_list_total.append(ing_dict)
            i += 1
        meals[key_meal] = ing_list_total
        f.readline()
print(meals)
cook_book = meals


def get_shop_list_by_dishes(a, b):
    shop_list = {}
    for dish in a:
        for ing in cook_book[dish]:
            new_shop_list_item = dict(ing)
            new_shop_list_item['quantity'] *= b
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print(f'{shop_list_item["ingridient_name"]} {shop_list_item["quantity"]} {shop_list_item["measure"]}')


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)


create_shop_list()
