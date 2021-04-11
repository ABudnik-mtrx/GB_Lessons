my_list = input('Введите значения: ')
my_list = my_list.split()


a = str(my_list[-1])



if len(my_list)%2 == 0:
    my_list[::2], my_list[1::2] = my_list[1::2],my_list[::2]
    str = " ".join([str(a) for a in my_list])
    print (str)
else:
    new_my_list = my_list[:-1]
    new_my_list[::2], new_my_list[1::2] = new_my_list[1::2], new_my_list[::2]
    q= new_my_list
    str = " ".join([str(a) for a in q])
    str = str + ' ' +a
    print (str," ")







