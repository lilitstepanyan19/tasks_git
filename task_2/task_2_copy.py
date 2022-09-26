

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


def get_info(inp_1, inp_2, y):
    d = {}
    for k,v in y.items():   
        print(f'{inp_1.lower()}-{inp_2.lower()}' not in k.lower())
        if inp_1.lower() in k.lower() and inp_2.lower() in k.lower():
            c = 0
            z = 0
            inp_ans = input('Where arw you now: ')
            for el in v:
                if el == '':
                    continue
                el = el.split('/')
                z += int(el[1])
            for el in v:
                if el == '':
                    continue
                el = el.split('/')
                c += int(el[1])
                if inp_ans.lower() in el[0].lower():
                    break  
            print(f'You have traveled {c} km, you have {z-c} km to go')
            
    for k,v in y.items(): 
        if f'{inp_1.lower()}-{inp_2.lower()}' not in k.lower():
            inp_update = input('Do you want to add a new route? - ')
            if inp_update == 'y':
                from_where = input('the main highway comes from - ').title()
                to_where = input('the main highway goes where - ').title()
                ml = []
                while True:
                    from_here = input('if the places are over enter END: name from here - ').title()
                    if from_here.lower() == 'end':
                        break
                    here = input('name here - ').title()
                    km = input('how many km - ')
                    while not km.isdigit():
                        print('km must be a number')
                        km = input('how many km - ')
                    ml.append(f'{from_here}-{here}/{km}')
                d[f'{from_where}-{to_where}'] = ml
            break
    return d

def main():    
    inp_1 = input('1: ')
    inp_2 = input('2: ')
    x = info('routes.txt')
    y = get_country_list(x)
    inf = get_info(inp_1, inp_2, y)
    print(inf)
    if inf:
        with open('routes.txt', 'a') as f:
            f.write(str(inf))
print(main())