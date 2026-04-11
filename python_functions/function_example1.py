def add(a,b):
    c=a+b
    print("The sum of",a,"and",b,"is",c)
    #return c
result = add(10,20)

def div1(q,w,e):
    d=q/w
    return d
print(div1(10,5,2))

def evenOrOdd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(evenOrOdd(10))
print(evenOrOdd(15))

def fact(n):
	""" to find factorial value """
	prod = 1
	while(n > 1):
		prod = prod * n
		n = n -1 
	return prod
for i in range(1,11):
	print("factorial of {} is {}".format(i,fact(i)))