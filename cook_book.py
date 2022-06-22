import pprint


file_name = "book.py"

def catalog_reader(file_name):
    with open(file_name, encoding = 'utf - 8') as file:
        cook_book ={}
        for line in file:
            dish =line.strip()
            ingr = []
            for item in range(int(file.readline())):
               ing = file.readline()
               ing_list = ing.split(" | ")
               ing_dict = {}
               ing_dict['ingredient_name'] = ing_list[0]
               ing_dict['quantity'] = int(ing_list[1])
               ing_dict['measure'] = ing_list[2].strip()
               ingr.append(ing_dict)
            cook_book[dish] = ingr
            file.readline()
        return   cook_book

catalog =  catalog_reader(file_name)
pprint.pprint(catalog ,width= 100, sort_dicts=False )


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        new_shop_list_item = dict(ingredient)
        new_shop_list_item['quantity'] *= person_count
        if new_shop_list_item['ingredient_name'] not in shop_list:
            shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
        else:
            shop_list[new_shop_list_item['ingredient_name']]['quantity'] +=new_shop_list_item['quantity']

    return shop_list


def print_shop_list(shop_list):
   for shop_list_item in shop_list.values():
      print('{} {} {}'.format(shop_list_item['ingredient_name'], shop_list_item['quantity'],
                                shop_list_item['measure']))


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете '
                   'на одного человека (через запятую): ').lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes,person_count)
    print_shop_list(shop_list)



create_shop_list()
