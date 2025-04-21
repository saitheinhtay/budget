print("\t\tSTEP COUNTER ")
dailyGoal= int(input("What is your daily step goal? "))
currentStep = int(input("How many steps have you taken today?"))

remaining = dailyGoal-currentStep
if remaining > 0:
    print(f"You need {remaining} more steps to reach your goal!")
elif currentStep == dailyGoal:
    print(f"Congratulation! You get your goal . Current Step Is {currentStep} steps")