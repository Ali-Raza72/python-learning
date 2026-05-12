# Python Quiz Game

Questions=("1.Who developed Python Programming Language?",
           "2.Which of the following is a valid way to start a function in Python?",
           "3.What does the len() function do in Python?",
           "4.Which type of Programming does Python support?",
           "5.Is Python case sensitive when dealing with identifiers?"
           
           )

Options=(("A.Wick van Rossum","B.Rasmus Lerdorf","C.Guido van Rossum","D.Niene Stom"),
         ("A.def function():","B.function def():","C.function():","D.define function():"),
         ("A.Converts data to a string","B.Returns the number of elements","C.Sorts the list","D.Reverses the string"),
         ("A. object-oriented programming","B.structured programming","C.functional programming","D. all of the mentioned"),
         ("A.no","B.yes","C.all of these","D.None"))

answers=("C","A","B","A","B")
guesses=[]
score=0
question_num=0

for question in Questions:
    print("--------------")
    print(question)
    for option in Options[question_num]:  # our option in 2d tuple
     print(option)  # by this we get the option of first in every question so we increments
    guess=input("Enter (A,B,C,D):").upper()
    guesses.append(guess)
    if guess==answers[question_num]:
       score+=1
       print("Correct!")
    else:
       print("Incorrect!")
       print(f"{answers[question_num]} is the Correct Answer")
    question_num+=1
# Now we print the results
print("--------")
print("-----RESULT-----")
print("---------")

print("Answer:",end=" ")
for answer in answers:
   print(answer,end=" ")
print()

print("guesses:",end=" ")
for guess in guesses:
   print(guess,end=" ")
print()

score=int(score/ len(Questions) * 100)
print(f"Your score is {score}%")



