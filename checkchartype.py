print("\t\t\t CHARACTER TYPE CHECKER")
char = input("Enter a single character : ")

if char.isalpha():
    print("This is a latter.")
elif char.isdigit():
    print("This is a digit.")
else:
    print("This is a special character.")
