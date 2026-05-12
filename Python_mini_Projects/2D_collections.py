  # 1
fruits=["Apple","Orange","Kivi","Mango"]
vegetables=["celery","potatos","tomato"]
meats=["chicken","fish","Mutton"]

groceries=[fruits,vegetables,meats]
fruits[0]="Pinnapple"
print(groceries)

# if we have to print first coloumn then we use this
fruits=["Apple","Orange","Kivi","Mango"]
vegetables=["celery","potatos","tomato"]
meats=["chicken","fish","layla"]

groceries=[fruits,vegetables,meats]


print(groceries[0][0])
print(groceries[0][1])
print(groceries[0][2])
print(groceries[1][0])
print(groceries[1][1])
print(groceries[1][2])
print(groceries[2][0])
print(groceries[2][1])
print(groceries[2][2])
print(groceries[2])


groceries=[["Apple","Orange","Kivi","Mango"],
           ["celery","potatos","tomato"],
           ["chicken","fish","layla"]]
for collection in groceries:
    for food in collection:
        print(food,end=" ")
    print()

#  2
 #  Let create 2D keyboard of numbers (with help of tuple)

num_pad=((1,2,3),
         (4,5,6),
         (7,8,9),
         ("*",0,"#"))
for row in num_pad:
    for num in row:
        print(num,end=" ")
    print()

num_pad=(("A","B","C","D","F","G"),
         ("H","I","J","K","L","M"),
         ("N","O","P","Q","R","S"),
         ("T","V","W","X","Y","Z"))
for row in num_pad:
    for num in row:
        print(num,end=" ")
    print()