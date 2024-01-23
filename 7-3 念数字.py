a = input()
b = {
    '-': 'fu',
    '0': 'ling',
    '1': 'yi',
    '2': 'er',
    '3': 'san',
    '4': 'si',
    '5': 'wu',
    '6': 'liu',
    '7': 'qi',
    '8': 'ba',
    '9': 'jiu'}
for i in range(len(a) - 1):
    if a[i] == '-':
        print('fu' + ' ', end='')
    else:
        print(b[a[i]] + ' ', end='')
b = b[a[-1]]
print(b)