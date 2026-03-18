org_number = int(input("Orginal number: "))
rev_number = 0

while org_number != 0:
    print("--------------New Loop-----------------")
    print(f"Step 1: {org_number} % 10 = {org_number % 10}")
    remainder = org_number % 10 # 789 -> 9
    
    print(f"Step 2: {rev_number} * 10 + {remainder} = {rev_number * 10 + remainder}")
    rev_number = rev_number * 10 + remainder # 9
    
    print(f"Step 3: {org_number} // 10 = {org_number // 10}")
    org_number = org_number // 10
    
print("rev ", rev_number)