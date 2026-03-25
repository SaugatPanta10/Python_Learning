annual_fees = 150000
student1 = {
    "name": "ram",
    "age": 20, 
    "address": "ktm",
    "paid_fees": 10000
}

student2 = {
    "name": "hari", 
    "age" : 19, 
    "address": "itahari",
    "paid_fees": 80000
}

def show_info(student): 
    print(f"""
--------------------------------------
    Name : {student["name"]}
    Age : {student["age"]}
    Address : {student["address"]}
    Paid : Rs. {student["paid_fees"]}
---------------------------------------
    Remaining: Rs. {annual_fees - student["paid_fees"]}
""")
    
show_info(student1)