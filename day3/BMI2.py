height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))

bmi = round(weight / (height**2))

print(bmi)

if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal")
elif bmi < 30:
    print("overweight")
elif bmi < 35:
    print("obese")
else:
    print("clinically obese")