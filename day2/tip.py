amount = float(input("Bill: ").strip())
no_of_people = int(input("People: ").strip())
tip_percentage = float(input("Tip: ").strip())
tip_val = round(tip_percentage / 100, 4)

tip = round(amount * tip_val, 4)
bill_per_person = round((amount + tip)/no_of_people, 4)

print(f"Tip: {tip}")
print(f"Each person should pay: {bill_per_person}")