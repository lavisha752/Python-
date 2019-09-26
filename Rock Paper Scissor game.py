# condition is true
while (1):
        print("what is your choice: rock|paper|scissor:" )

# user input for player_A and player_B
        player_A= input("Please enter your choice:")
        player_B= input("Please enter your choice:")

# check if the statement is true and test for diffrent choices
        if(player_A=='rock' and player_B=='rock'):
            print("Its a tie")

        elif (player_A == 'rock' and player_B == 'paper'):
             print("Player_A wins")

        elif (player_A == 'rock' and player_B == 'scissor'):
             print("Player_A wins")

        elif (player_A == 'paper' and player_B == 'paper'):
             print("Its a tie")

        elif (player_A == 'paper' and player_B == 'scissor'):
             print("Player_B wins")

        elif (player_A == 'paper' and player_B == 'rock'):
             print("Player_B wins")

        elif (player_A == 'scissor' and player_B == 'scissor'):
             print("Its a tie")

        elif (player_A == 'scissor' and player_B == 'paper'):
             print("Player_A wins")

        elif (player_A == 'scissor' and player_B == 'rock'):
             print("Player_B wins")

        else:
         print("invalid input")

# checking if user want to try again
        decision = input("Do you want to restart the game again?: ")
        if decision == 'yes' or 'Yes':
         decision == True
        else:
         decision == False
# or exit from the program
        print('Exit Game')

