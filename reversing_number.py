num = int(input("Enter a number: "))
reversed_num = 0
temp = num

while temp > 0:
    digit = temp % 10        
    reversed_num = reversed_num * 10 + digit
    temp = temp // 10          

print("Reversed number:", reversed_num)