class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def info(self):
        return f"My name is {self.name}, I'm a {self.age} years, old"
        
    def human(self):
        return "I'm a man"

class Child(Person):
    def human(self):
        return "I'm a children"

bob = Person('Bob', 33)
ann = Child('Ann', 2)

print(bob.info(), bob.human())
print(ann.info(), ann.human())








# ml = []
# num = []
# while True:
#     inp = input('Enter a something: ')
#     if inp == 'stop':
#         break
#     if inp.isalpha():
#         ml.append(inp)
#     if inp.isdigit():
#         num.append(inp)
        
# ml.sort()
# num.sort()        
# print(ml)
# print(num)





