import random


with open('file.txt', 'r') as f:
    ml = f.read()
ml = ml.split()
ml.sort(key=len)
ml = ' '.join(ml)
with open('file.txt', 'a') as f:
    f.write('\n'+ str(ml))
    
    
# with open('file.txt', 'r') as f:
#     ml = f.readlines()
# for el in ml:
#     el = el.split()
#     el.sort(key=len)
#     el = ' '.join(el)
#     with open('file.txt', 'a') as f:
#         f.write('\n'+ str(el))


# with open('file.txt', 'r') as f:
#     ml = f.read()
# ml = ml.split()   
# word = ''
# c = 0
# for el in ml:
#     if len(el) > len(word):
#         word = el
#         c = len(el)
# print(word, c)
# with open('file.txt', 'r') as f:
#     ml = f.read()
# ml = ml.split()
# w = max(ml, key=len)
# print(w, len(w))


# num = random.randint(1, 10)


# i = 0  
# while i < 3:
#     inp = int(input('Enter a number: '))
#     if inp >= num +10 and inp < num + 20 or inp >= num - 20 and inp < num - 10:
#         print(num,'hot')
#     if inp < num + 10 and inp > num or inp < num  and inp > num - 10:
#         print(num, 'very hot')
#     if inp > num + 20 and inp <= 100 or inp < num - 20 and inp > num - 100:
#         print('cold')
#     if inp > num + 100 or inp < num - 100:
#         print(num,'very cold')
#     if inp == num:
#         print(num,'right')
#         break
#     i += 1
   