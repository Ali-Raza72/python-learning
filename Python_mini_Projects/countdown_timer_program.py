import time
my_time=int(input("Enter time in seconds:"))
for x in range(my_time,0,-1):
    print(x)
    time.sleep(1)
print("Start UP's")

time.sleep(2)
print("HEYY!")


my_time=int(input("Enter time in seconds:"))
for x in range(0,my_time):
    print(x)
    time.sleep(1)

print("Time UP's")


my_time=int(input("Enter time in time:"))
for x in range(my_time,0,-1):
    seconds=x % 60
    minutes=int(x/60) %60
    hours=int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time UP's")
fruits=["apple","banana"]
print(help(fruits))
print(dir(fruits))