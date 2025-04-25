import random

print("\t\t\tRECEIPT GENERATOR")

proteins = ["chicken","beef","tofu","eggs"]
veggies = ["broccoli","carrots","spinach","mushrooms"]
carbs = ["rice","pasta","potatoes","bread"]
methods = ["baked","grilled","stir-fried","roasted"]
flavors =["garlic","lemon","spicy","herb"]

while True:
    protein = random.choice(proteins)
    veggie = random.choice(veggies)
    carb = random.choice(carbs)
    method = random.choice(methods)
    flavor = random.choice(flavors)

    print(f"\nYour random recipe : {flavor} {method} {protein} with {veggie} and {carb} .")

    if not input("\nGenerate another one? (y/n)").lower().startswith('y'):
        print("GOODBYE ! ")
        break