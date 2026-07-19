# Number guessing game
import random
computer = random.randint(1,100)
while True:
    try:
         choice=int(input("Guess the number in between the range(1,100):"))
         if choice > computer :
              print("Too high!")
         elif choice < computer:
             print("Too low!")
         elif computer==choice:
              print("Congratulations! You guessed the number")
              break
   
    except:
         print("Enter valid input.")
    



 

