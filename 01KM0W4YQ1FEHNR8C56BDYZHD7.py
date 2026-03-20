# Function

# product = {
#     'name': 'mobile',
#     'price': 25000,
#     'descriptions': ""
# }


# def show_product_detail(): # function defination
#     print(f"""
#         ------------------------------
#         Name: {product["name"]}
#         Price: NPR {product["price"]}
#         Desc: {product["descriptions"]}
#         -------------------------------
#     """)


# show_product_detail() # function call



# show_product_detail() # function call


# 

# def welcome_user():
#     print(f"""
          
#     ~~~~~   W E L C O M E    H O M E  ~~~~~
          
#           """)
    
    
# welcome_user()
# welcome_user()
# welcome_user()
# welcome_user()
# welcome_user()
# welcome_user()

# def welcome_user(name): # parameters, formal parameter
#     print(f"""
          
#     ~~~~~   W E L C O M E  {name}  ~~~~~
          
#           """)



# welcome_user("RAM")  # Actual data, i.e. "RAM" is called as argument, actual parameter
# welcome_user("HARI")
# welcome_user()

# name = input("Username: ")

# welcome_user()


# Multiple parameters
# def welcome_user(name, greeting): # parameters, formal parameter
#     print(f"""
          
#     ~~~~~   {greeting}  {name}  ~~~~~
          
#           """)
    

# welcome_user("HARI", "GOOD MORNING")
# welcome_user("SHYAM", "GOOD EVENING")


# Keyword arguments
# def welcome_user(name, greeting): # parameters, formal parameter
#     print(f"""
          
#     ~~~~~   {greeting}  {name}  ~~~~~
          
#           """)
    

# welcome_user("HARI", "GOOD MORNING")
# welcome_user("GOOD MORNING", "HARI")
# welcome_user("SHYAM", "GOOD EVENING")

# welcome_user(greeting="GOOD MORNING", name="HARI")


# # Default argument
# def welcome_user(name, contacts , greeting="WELCOME"): # parameters, formal parameter
#     print(f"""        
#     ~~~~~   {greeting}  {name}  ~~~~~
#           """)
    
#     # isinstance checks whether the given data matches the given data type
#     if isinstance(contacts, list):    
#         for contact in contacts:
#             print("   Contact: ", contact)
#     else:
#         print("Improper data type in contacts")
    
    
# welcome_user("HARI")

# Note: While keeping default argument, make sure, default arguments/parameter comes after all the non default parameters/arguments

# welcome_user("HARI", ["980000000", "9800000001"])
# welcome_user("HARI", 5) # invalid data


# print("this is data to show")
# [].sort() -> ascending
# [].sort(reverse=True) -> descending

# Return statement


# Default argument
# def welcome_user(name, greeting="WELCOME"): # parameters, formal parameter
#     print(f"""        ~~~~~   {greeting}  {name}  ~~~~~""")
#     return "welcome message shown successful"


# result = welcome_user("HARI")

# print(result)

# Just show the output
# def add(a,b):
#     print(a+b)


# No, just showing output is not  enough, we need that output for further use
# def add(a,b):
#     add_result = a+b
#     return add_result
    

# result = add(45, 45)
# print(add(10, 5))

# print(result)

# if result>90:
    



def reverse_given_number(org_number):
    rev_number = 0
    while org_number != 0:
        print("--------------New Loop-----------------")
        print(f"Step 1: {org_number} % 10 = {org_number % 10}")
        remainder = org_number % 10 # 789 -> 9
        
        print(f"Step 2: {rev_number} * 10 + {remainder} = {rev_number * 10 + remainder}")
        rev_number = rev_number * 10 + remainder # 9
        
        print(f"Step 3: {org_number} // 10 = {org_number // 10}")
        org_number = org_number // 10
        
    return rev_number    



# print(reverse_given_number(456))

# org_number = int(input("Orginal number: "))

# print(reverse_given_number(org_number))