def add(*a):
    sum=0
    for i in a:sum=sum+i
 
    return sum

def information(**data):
    for key,value in data.items():
        print("{}: {}".format(key,value))

import function_example1
function_example1.add(67,89)


