my_list = [1234, 6.666, 'True', 'str', [12345]]
def my_type(i):
    for i in range(len(my_list)):
        print(type(my_list[i]))
    return
my_type(my_list)