import random

# Constantes para representações visuais
ROCK = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
PAPER = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
SCISSORS = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Título do jogo
print("Welcome to Rock, Paper, Scissors!\n")

def get_player_choice():
    # Solicita a escolha do jogador
    player_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
    return player_choose

def display_choices(choice, name):
    # Exibe a escolha do jogador ou do computador com base na entrada
    choices = [ROCK, PAPER, SCISSORS]
    print(f"{name} chose:")
    print(choices[choice])

def get_computer_choice():
    # Gera a escolha aleatória do computador
    return random.randint(0, 2)

def determine_winner(player_choice, computer_choice):
    # Verifica o resultado do jogo com base nas escolhas do jogador e do computador
    if player_choice == computer_choice:
        return "It's a draw"
    elif player_choice == 0 and computer_choice == 1:
        return "Computer wins"
    elif player_choice == 0 and computer_choice == 2:
        return "You win :)"
    elif player_choice == 1 and computer_choice == 0:
        return "You win :)"
    elif player_choice == 1 and computer_choice == 2:
        return "Computer wins"
    elif player_choice == 2 and computer_choice == 0:
        return "Computer wins"
    elif player_choice == 2 and computer_choice == 1:
        return "You win :)"

# Loop principal do jogo
while True:
    player_choice = get_player_choice()
    if player_choice not in [0, 1, 2]:
        print("Invalid choice. Please enter 0, 1, or 2.")
        continue

    display_choices(player_choice, "You")
    computer_choice = get_computer_choice()
    display_choices(computer_choice, "Computer")

    winner = determine_winner(player_choice, computer_choice)
    print(winner)

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye!")
        break
