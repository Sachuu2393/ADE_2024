def addition(num1,num2):
    ans=num1+num2
    return ans

#Adding new function for subtraction and multiplication
def subtraction(num1,num2):
    ans=num1-num2
    return ans

def multi(num1,num2):
    ans=num1*num2
    return ans

add=addition(10,20)
print(f"Addition of two number is : {add} ")


sub=subtraction(20,10)
print(f"subtraction of two number is : {sub}")

mul=multi(10,20)

print(f"Multiplication of two number is : {mul} ")