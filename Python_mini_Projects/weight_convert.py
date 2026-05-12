weight=float(input("Enter ur Weight: "))
unit=input("Kilograms or Pounds (K,L): ").capitalize()

if unit =="K":
    weight=weight* 2.02
    unit="Lbs."
    print(f"UR weight is {round(weight,1)} {unit}")
elif unit=="L":
    weight=weight/2.02
    unit="Kgs."
    
else:
    print(f"{unit} was invalid")
    print(f"UR weight is {round(weight,1)} {unit}")
