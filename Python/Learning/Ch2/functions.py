# Basic Function

def func1():
    print("I am a function")

# Function That Takes Args

def func2(arg1, arg2):
    print (arg1, " ", arg2)

# Function The Returns a Value

def func3(x):
    return x*x*x

# Function With Default Value for an Arg

def func4(num, x = 1):
    result = 1
    for i in range(x):
        result = result * num
    return result

# Function With Variable Number of Args

def func5(*args):
    result = 0
    for x in args:
        result = result + x
    return result

#func1()
#print (func1())
#print (func1)

#func2(10, 20)
#print (func2(10, 20))
#print (func2)
#print(func3(3))

#func4(10)
#print(func4(10))
#print(func4(10, 4))
#print(func4(x = 3, num = 10))

#func5(1, 1, 1, 1)
#print(func5(1, 1, 1, 1))