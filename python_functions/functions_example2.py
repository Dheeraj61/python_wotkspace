def display(string):
    def message():
        return 'Hi How are you'
    return 'welcome '+string+' '+message()


print(display('dheeraj'))

def add(*a):
    return sum(a)
print(add(1,2,3,4,5))

def info(**data):
    for key,value in data.items():
        print("{}: {}".format(key,value))

info(name='dheeraj',num=234567788,loaction='india',age=30)