def add(num1,num2):
    return num1+num2
def multiply(num1,num2):
    return num1*num2

def calculator(num1,num2,operator):
    return operator(num1,num2)


print(calculator(2,3,add))
print(calculator(2,3,multiply))