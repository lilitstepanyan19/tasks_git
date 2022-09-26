

def info(file):
    with open(file, 'r') as f:
        c = f.readlines()
        return c
    

def get_country_list(arg):
    d = {}
    for el in arg:
        if ':' in el:
            k = el[:-1]
            d[k] = []
        else:
            d[k].append(el[1:-1])
    return d

def get_country_lenght(arg):
    d = {}
    for k,v in arg.items():
        lenght = 0
        ml = []
        for el in v:
            nl = []
            if el == '':
                continue
            el = el.split('/')
            el[0] = el[0].split('-')
            lenght += int(el[1])
            nl.append(el[0][0])
            nl.append(el[0][1])
            nl.append(el[1])
            ml.append(nl)
        ml.append(lenght)
        d[k] = ml
    return d    


def get_ans(inp_1, inp_2, arg):
    d = {}
    for k,v in arg.items():          
        if inp_1.lower() in k.lower() and inp_2.lower() in k.lower():
            inp_ans = input('Where arw you now: ')
            for el in v:
                if type(el) == str:
                    if inp_ans.lower() == inp_1:
                        traveled = int(v[-1])
                        print(f'you have traveled {traveled} km')
                    elif inp_ans.lower() == inp_2:
                        traveled = 0
                        print(f'you have traveled {traveled} km')
                    elif inp_ans.lower() == el[0].lower():
                        traveled = int(v[-1]) - int(el[-1])
                        print(f'you have traveled {traveled} km')
    return d


# num = []
# word = []
# count = []
# p = []
# while True:
#     inp = input("Enter something ")
#     if inp == '0':
#         break
#     if inp.isdigit():
#         num.append(inp)
#         num.sort()
        
    # else:
    #     word.append(inp)
    #     word.sort()    
    
    # if inp.isalpha() and len(inp) > 3:
    #     count.append(inp) 
        
    # if inp[:1] == inp[-1]:
    #     p.append(inp)
        
def write_file(fname, ml):        
    with open(fname, 'w') as f:
        f.write(str(ml))      
        f.close() 
    return f
    
      
def main():    
    inp_1 = input('1: ')
    inp_2 = input('2: ')
   
    info_file = info('routes.txt')
    country_name = get_country_list(info_file)
    c_len = get_country_lenght(country_name)
    
    print(get_ans(inp_1, inp_2, c_len))
    
    # print(c_len)
        
    # write_file('num.txt', num)
    # write_file('word.txt', word)
    # write_file('count.txt', count)
    # write_file('p.txt', p)
    # print(info('num.txt'))
    # print(info('word.txt'))
    # print(info('count.txt'))
    # print(info('p.txt'))
print(main())