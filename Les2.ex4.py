a = input('Введите несколько слов: ')

a = a.split()

b = {a[i]:i for i in range (0,len(a))}


for k,v in enumerate(b):
    print (k,v)





