total_bill = float(input("What was the total bill?: "))

percent = float(input("What percent tip would you like to give?: "))

people = float(input("How many people are there?: "))

per_person = round((total_bill + (percent/100) * total_bill) / people, 2)
                                #gives decimal version of percent
                                
print(f"Each person should pay: {per_person}")