a = int(input('Введите номер месяца: '))

w = [12, 1, 2]
s = [3,4,5]
smr = [6,7,8]
autm = [9,10,11]

if a in w:
    print ('Зима')
elif a in s:
    print ('Весна')
elif a in smr:
    print ('Лето')
else:
    print('Осень')


b = int(input('Введите номер месяца: '))

d= {'winter': [12,1,2],
    's':[3,4,5],
    'smr':[6,7,8],
    'autm':[9,10,11]
    }

if b in d['winter']:
    print ('Зима')
elif b in d['s']:
    print ('Весна')
elif b in d['smr']:
    print ('Лето')
else:
    print ('Осень')


