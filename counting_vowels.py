text  = input("Enter the text that you want to check vowels: ").strip().lower()
vowels = "aeiou"
count = 0

for i in text:
    if i in vowels:
        count +=  1

print(f"There are {count} number of vowels.")