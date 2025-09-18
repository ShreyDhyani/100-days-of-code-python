height = float(input("Enter your height.\n").strip())
weight = float(input("Enter your weight.\n").strip())

bmi = round(weight/(height*height), 4);
print(f"Your BMI is {bmi}")
