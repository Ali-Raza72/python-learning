#  A=P(1+r/n) to power time't'
#   A= final amount
#   P= initial principle balance
#   r= interest rate
#   t= number of times

principle=0
rate=0
time=0

while principle <=0:
    principle= float(input("Enter ur principle amount: "))
    if principle <=0:
        print("principle can't be less than or equal to zero")

while rate <=0:
    rate= float (input("Enter ur interest rate: "))
    if rate <=0:
        print("rate can't be less than or equal to zero")

while time <=0:
    time= int(input("Enter ur time in year: "))
    if time <=0:
        print("time can't be less than or equal to zero")

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")

# we can also use 'True'

principle=0
rate=0
time=0

while True:
    principle= float(input("Enter ur principle amount: "))
    if principle <0:
        print("principle can't be less than  zero")
    else:
        break
while True:
    rate= float (input("Enter ur interest rate: "))
    if rate <0:
        print("rate can't be less than  zero")
    else:
        break

while True:
    time= int(input("Enter ur time in year: "))
    if time <0:
        print("time can't be less than zero")
    else:
        break

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")

