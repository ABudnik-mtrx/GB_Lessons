a = int(input("Введите количество товара "))
i = 1
my_dict = []
my_list = []
my_analys = {}
while i <= a:
    my_dict = dict({'название': input("Введите название "), 'цена': input("Введите цену "),
                    'количество': input('Введите количество '), 'eд': input("Введите единицу измерения ")})
    my_list.append((i, my_dict))
    i += 1

print(my_list)


