# Shopping cart Program

foods=[]
prices=[]
total=0

while True:
    food=input("Enter a food to buy (q to quite):")
    if food.lower()=="q":
        break
    else:
        price=float(input(f"Enter the price of {food}: $"))
        foods.append(food)
        prices.append(price)

print("\n---THE FOOD CART---")
for food in foods:
    print(food ,end=" "),"\n"

for price in prices:
    print(price,end=" ")
    total+=price
print()
print(f"Your total is ${total}:")



