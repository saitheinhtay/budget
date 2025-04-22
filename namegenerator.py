import random

first_parts = ["Sky","Star","Moon","Sun","Fire","Ice"]
last_parts = ["rider","walker","hunter","seeker","keeper","singer"]
print("\t\t\tFantasy name GENERATOR")
count = int(input("How many name do you want ? : "))
for i in  range(count):
    first_name = random.choice(first_parts)
    last_name = random.choice(last_parts)
    print(f"{first_name} {last_name}")