import random
rock='''
    _______
___'   ____)
       (____)
       (_____)
       (____)
---.___(___)
'''
paper='''
    _______
___'    ___)____
           _____)
          _______)
         _______)
---'___________)
'''
scissors='''
   _______
___'   ____)___
         ______)
        ________)
        (____)
---,____(---)
'''

game_images=[rock,paper,scissors]
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors(RootIpV6)\n "))
print(game_images[user_choice])
computer_choice=random.randint(0,2)
print("Computer chose")
print(game_images[computer_choice])

if user_choice >=3 or user_choice <0:
    print("You typed an invalid number.You Lose!!")
elif user_choice == 0 and computer_choice == 2:
    print("User wins!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")
