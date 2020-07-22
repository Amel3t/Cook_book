def read_cook_book(filename):
    dishes = {}
    with open('Чтение данных.txt', encoding='utf8') as f:
        while 'True':
            dish_name = f.readline() #читаем первою строку
            if len(dish_name) == 0:
                break

            dish_name = dish_name.strip()
            if len(dish_name) == 0:
                continue
         
            count = int(f.readline().strip()) #читаем вторую строку
            i = 0
            ingredients = []
            while i < count:
                line = f.readline().strip()
                line_1 = line.split('|')
                ingredient_info = {'ingredients_name': line_1[0],
                        'quantiny': int(line_1[1]),
                        'measure': line_1[2]
                }
                ingredients.append(ingredient_info)
                i += 1

            dishes[dish_name] = ingredients
    return dishes

def get_shop_list_by_dishes(cook_book, dishes, person_count):
    def ingredients_by_portions(ingredient_info):
        ingredient_info['quantiny'] *= person_count
        return ingredient_info

    shop_list = {}
    for dish in dishes:
        dish_ingridients = cook_book.get(dish)
        if dish_ingridients == None:
            continue

        for ingredient_info in dish_ingridients:
            ingredients_name = ingredient_info['ingredients_name']
            if shop_list.get(ingredients_name) == None:
                shop_list[ingredients_name] = {
                    'quantiny': ingredient_info['quantiny'] * person_count,
                    'measure': ingredient_info['measure']}
            else:
                shop_list[ingredients_name]['quantiny'] += ingredient_info['quantiny'] * person_count

    return shop_list

cook_book = read_cook_book('Чтение данных.txt')

shop_list = get_shop_list_by_dishes(cook_book, ['Омлет', 'Фахитос'], 2)

print(shop_list)