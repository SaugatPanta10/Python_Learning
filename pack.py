menu = """
---------------
1. Data Pack
2. Voice Pack
3. Unlimited
4. Summer Pack
#. Exit
---------------
"""
print(menu)

show_menu = True
while show_menu:
    print(menu)
    user_choice=input("Enter your choice (1,2,3,4,#): ")
    print("User choosed services:", user_choice)
    if user_choice == "#":
        print("Thank you for using Ncell.")
        show_menu = False