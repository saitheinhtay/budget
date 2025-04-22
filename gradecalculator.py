from numpy.ma.extras import average

print("\t\t\t GRADE CALCULATOR")
scores = []
while True:
    score = input("Enter a test score : ")
    if score.lower() == "done":
        print("Goodbye!")
        break

    scores.append(float(score))
    average = sum(scores) / len(scores)
    print(f"Average score: {average: .1f}")
    if average >=90:
        print('Grade A ')
    elif average >= 80:
        print('Grade B')
    elif average >= 70:
        print('Grade C')
    else:
        print('Grade D or F')