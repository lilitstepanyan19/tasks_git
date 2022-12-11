
ml = ['hello', 'all', 'world', 'by']

for j in range(len(ml)):
    for i in range(len(ml)-1):
        if len(ml[i]) > len(ml[i + 1]):
            ml[i], ml[i + 1] = ml[i + 1], ml[i]

print(ml)








