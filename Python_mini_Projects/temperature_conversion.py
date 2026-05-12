unit=input("Enter the unit in (C/F): ")
temp=float(input("Enter the temperature:"))

if unit=="C":
    temp=(5* temp)/9 +32
    print(f"Ur Temperature in Celius is {round(temp,1)}")
elif unit=="F":
    temp=(temp-32)* 5/9
    print(f"Ur Temperature in Celius is {round(temp,1)}")
else:
    print("Invalid Unit")