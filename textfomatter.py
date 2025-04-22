from random import choice

print("\t\t\t TEXT CAPITALIZER ")
text = input("Enter some text ")
print('''
        1. UPPERCASE
        2. lowercase 
        3. Title Case
        4. Sentence Case
''')

choice = int(input("Choose option format 1-4 : "))

if choice == 1:
    print(text.upper())
elif choice == 2:
    print(text.lower())
elif choice == 3:
    print(text.title())
elif choice == 4:
    print(text.capitalize())