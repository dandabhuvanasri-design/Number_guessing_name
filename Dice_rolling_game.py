# dice rolling game
import random
while True:
    choice=input("roll the dice(Enter yor n):")
    if (choice == "y" or choice =="Y") :
          die1=random.randint(1,6)
          die2= random.randint(1,6)
          print(f'({die1},{die2})')
    elif choice =="n":
          print("Thank you for playing the game!")
          break
    else:
         print("Enter valid input.")
         
      
    

