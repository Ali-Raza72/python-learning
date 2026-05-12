  # Format specfier ={value:flags} format a vlaue based on what flags are inserted
price1=2.3343
price2=3.4324
price3=5.2215
print(f"price 1 is {price1:.2f}")
print(f"price 2 is {price2:.2f}")
print(f"price 3 is {price3:.2f}")

price1=23343
price2=34324
price3=52215
print(f"price 1 is {price1:,}")
print(f"price 2 is {price2:,}")
print(f"price 3 is {price3:,}")

price1=2.3343
price2=3.4324
price3=5.2215
print(f"price 1 is {price1:<10}")
print(f"price 2 is {price2:>10}")
print(f"price 3 is {price3:^10}")

price1=2.3343
price2=3.4324
price3=5.2215
print(f"price 1 is {price1:+,.2f}")
print(f"price 1 is {price2:-,.2f}")
print(f"price 1 is {price3:+,.2f}")