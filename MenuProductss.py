menu = """
        -----------------
        1. Add Products
        2. Show all products
        3. Search products by name 
        4. Exit
        -----------------
"""
products = []

while True:
    print(menu)
    user_choice = (input("Enter a choice (1/2/3/4): "))

    if user_choice == "1":
        print("-------Enter product details--------")
        pr = input("Enter the name of the product that you want to add: ")
        Price = float(input("Enter the price in npr: "))
        des = input("Describe your product: ")

        new_products = {
            "Name": pr,
            "Price": Price,
            "Description": des
        }

        products.append(new_products)

        print("-------------Product added successfully------------")

    elif user_choice == "2":
        print("--------Product List---------")
        for i in products:
            print(f"""
                name: {i["Name"]}
                Price: {i["Price"]},
                Description: {i["Description"]}
                """)

    elif user_choice == "3":
        print("-------Product Search----------")

        search_name = input("Enter the product name that you want to search: ").strip().lower()
        for product in products:
            if search_name in product["Name"].strip().lower():
                print("-------Product found---------")
                print(f"""
                        "Name": {product["Name"]},
                        "Price":{product["Price"]},
                        "Description":{product["Description"]}
                    """)
            
    elif user_choice == "4":
        print("Thank you for using our services.")
        break

    else:
        print("Please choose either 1 or 2 or 3 or 4.")