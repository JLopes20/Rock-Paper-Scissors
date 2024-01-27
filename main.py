import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock,paper,scissors]
game_on = True

while game_on == True:

    user_choice = (input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))
    choices_len = len(choices)
    computer_choice_number= random.randint(0,choices_len-1)
    computer_choice_as_image = choices[computer_choice_number]


    if user_choice == "0":
        print(f"You've chosen rock!\n{choices[0]}")
        print(f"Computer choice is:\n{computer_choice_as_image}")
        if computer_choice_as_image == choices[0]:
            print("It's a tie!")
        elif computer_choice_as_image == choices[1]:
            print("You've lost! Paper beats rock")
        else:
            print("You've won! Rock beats scissors!")
        
    elif user_choice == "1":
        print(f"You've chosen Paper!\n{choices[1]}")
        print(f"Computer choice is:\n{computer_choice_as_image}")
        if computer_choice_as_image == choices[1]:
            print("It's a tie!")
        elif computer_choice_as_image == choices[2]:
            print("You've lost! Scissors beats Paper")
        else:
            print("You've won! Paper beats rock")
    elif user_choice == "2":
        print(f"You've chosen Scissors!\n{choices[2]}")
        print(f"Computer choice is:\n{computer_choice_as_image}")
        if computer_choice_as_image == choices[2]:
            print("It's a tie!")
        elif computer_choice_as_image == choices[0]:
            print("You've lost! Rock beats Scissors")
        else:
            print("You've won! Scissors beats Paper")
    else:
        print("Not a valid option! Try Again. Please, choose 0 for Rock, 1 for Paper, 2 for Scissors\n\n ")
        
    new_game= input("Try Again? Type 'yes' to continue, 'no' to cancel\n").lower()
    if new_game == "no":
        print("Game Over! It was nice playing with you!")
        game_on = False
    elif new_game == "yes":
        print("Let's go")
        game_on= True
        
    else: 
        print("Not a valid option!")  
        game_on=False
        
    
        
      
        








        
        

        
