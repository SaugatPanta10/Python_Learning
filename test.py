import os
while True:
        
    print("""
        --------------------------
        1. Add Product
        2. Show all products
        3. Search product by name 
        4. Exit
        --------------------------
    """)

    product= []
    while True:
        user_input = (input("\nEnter the options above (1/2/3/4): "))
        
      
        if user_input == "1":
            while True:
                npn = input("\nEnter the name of the product that you want to add: ")
                npp = float(input(f"Enter the price of {npn}: "))
                npd = input(f"Provide the description of {npn}: ")
                npdic = {
                    "Name": npn,
                    "Price": npp,
                    "Description": npd
                }

                product.append(npdic)
                print("\nProduct added successfully\n")

                while True :
                    choice = input("\nDo you want to add more items? (Yes/No): ").strip().lower()
                    if choice == "yes":
                        break
                    elif choice == "no":
                        break
                    else:
                        print("Please enter either yes or no.")
                        continue
                
        elif user_input == "2": 
            print("-------------Product List-----------\n")
            for i in product:
                print(f"""
                    ------------------------------------
                    Name: {i["Name"]}
                    Price: {i["Price"]}
                    Description: {i["Description"]}
                    ------------------------------------""")
                
        elif user_input == "3": 
            print("-------------Search Product--------------\n")
            search = input("Enter the product that you want to search: ").lower().strip()
            for i in product:
                if search in i["Name"]: 
                    print("\n Product Found!!!\n")
                    print(f"""
                        -------------------------
                            Name: {i["Name"]} 
                            Price: {i["Price"]}
                            Description: {i["Description"]}
                        -------------------------
                        """)
                        
                    
                
        elif user_input == "4":
            print("\nthank you. Bye!\n")
                


