def divide (a,b):
    quotient = a // b
    remainder = a % b 
    return quotient, remainder #packing

result = divide(5,2)

ans1 , ans2 = result #unpacking 
print(result, type(result))