num = []

while True:
    inp = input('Enter a somwthing: ')
    if inp == 'stop':
        break
    if inp.isdigit():
        num.append(inp)

print(num)

for i in range(len(num)):
    for j in range(len(num) - 1):
        if num[j][-1:] > num[j + 1][-1:]:
            num[j], num[j + 1] = num[j + 1], num[j]
    
print(num)

x = []
for i in num:
    x.append(int(i))
x.sort()

print('sorted: ', x)

print('max num: ', max(x))