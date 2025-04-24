print("\t\t\tVOWEL COUNTER")

#***********************Easy****************************************

# while True:
#     text = input("\nEnter some text (or 'quit'): ")
#     if text.lower() == "quit":
#         print("GOODBYE !")
#         break
#
#     vowel_count = 0
#     for letter in text.lower():
#         if letter in ["a","e","i","o","u"]:
#             vowel_count +=1
#
#     print(f"In this sentence  :  {vowel_count} vowels include had count.")

#***********************ADVANCED****************************************
while True:
    text = input("\nEnter some text (or 'quit'): ")
    if text.lower() == "quit":
        print("GOODBYE !")
        break

    vowels = sum(1 for char in text.lower() if char in "aeiou")
    print(f"In this sentence  : {vowels} vowels include had count.")