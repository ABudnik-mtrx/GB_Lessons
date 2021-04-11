a = int(input('Введите число: '))

my_list = [7,5,3,3,2]

i = 0

for i in range(len(my_list)):
    if my_list[i] == a:
        print (my_list.insert(i+1,a))
        break
    elif my_list[0] < a:
        my_list.insert(0, a)
    elif my_list[-1] > a:
        my_list.append(a)
    elif my_list[i] > a and my_list[i + 1] < a:
        my_list.insert(i + 1, a)
print(my_list)









