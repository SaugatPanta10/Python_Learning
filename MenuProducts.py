MENU = """
    --------------------------------
    1. Add product
    2. Show all products
    3. Search product by name
    4. Exit
    -------------------------------
"""

products = []


while True:
    # Step 1: show menu
    print(MENU)
    
    # Step 2: ask user to enter a choice
    choice = input("Choose (1/2/3/4):  ").strip()
    
    if choice == "1":
        # Ask user to input product details
        print("------------Enter product details--------------")
        name = input("Product Name: ")
        price = float(input("Product Price (in NPR): "))
        descriptions = input("Product desc: ") 
        
        # pack details into a dictionary
        new_product = {
            "name": name,
            "price": price,
            "descriptions": descriptions
        }
        
        # add newly created product dictionary to global product list
        products.append(new_product)
        
        print("----------New product added successfully---------")
        
    elif choice == "2":
        # show all products
        print("--------------Products List-------------")
        
        for product in products:        
            print(f"""
                  ------------------------------
                  Name: {product["name"]}
                  Price: NPR {product["price"]}
                  Desc: {product["descriptions"]}
                  -------------------------------
                  """)
            
    elif choice == "3":
        # search product by name
        print("------------Product Search----------")
        
        search_name = input("Search keyword:  ").strip().lower()
        
        for product in products:
            if search_name in product["name"].lower():
                print("Product found!!!!!")
                print(f"""
                  ------------------------------
                  Name: {product["name"]}
                  Price: NPR {product["price"]}
                  Desc: {product["descriptions"]}
                  -------------------------------
                  """)
                
    elif choice == "4":
        # exit
        print("Thank you for using our services")
        break  
    else:
        #  if user enters other than 1/2/3/4
        print("Please enter a valid choice")         
                

