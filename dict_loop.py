ages = {'Tod' : 35,
        'Jane' : 23,
        'Paul' : 62}

print(ages)

for key in ages.keys():
    print(key)

for value in ages.values():
    print(value)

for key in ages.keys():
    print('{}의 나이는 {}입니다.'.format(key, ages[key]))

for key, age in ages.items():
    print('{}의 나이는 {}입니다.'.format(key, age))