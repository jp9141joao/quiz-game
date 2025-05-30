import random
import os
import time

# Function to display questions and handle game logic
def Print_Questions(Question_Bank, Topic):
    Lives = 3  # Number of lives the player has
    Correct = 0  # Number of correct answers
    Total = len(Question_Bank)  # Total number of questions

    # Prompt the player to start the quiz
    while True:
        os.system('cls')
        Resp = input(f'\n* {Topic} Quiz *\n\nRemaining Lives: {Lives}\n\nType "1" to start\n\nR: ')
        
        Start = None
        if Resp.isdigit():
            Start = int(Resp)
        
        if Start is not None and Start == 1:
            break

    # Iterate through each question
    for Q in Question_Bank:

        # End the game if the player runs out of lives
        if Lives == 0:
            print('\nYou have run out of lives!')
            break

        # Display the question and options
        while True:
            os.system('cls')
            print(f'\n* {Topic} Quiz *\n\nRemaining Lives: {Lives}\n')
            print(f'{Q["Pergunta"]}\n')

            for i, Option in enumerate(Q['Opcao']):
                print(f'{i + 1}) {Option}')

            Resp1 = input('\nR: ')

            Resp2 = None
            if Resp1.isdigit():
                Resp2 = int(Resp1)

            # Check if the response is within valid options
            if Resp2 is not None and Resp2 > 0 and Resp2 <= len(Q['Opcao']):
                break

        # Check if the answer is correct
        selected = Q['Opcao'][Resp2 - 1]
        if selected == Q['Resposta']:
            Correct += 1
            print('\nCorrect answer!')
        else:
            Lives -= 1
            print('\nIncorrect answer!')

        # Prompt to continue to the next question
        while True:
            Resp = input('\nType "1" to continue\n\nR: ')
            
            Continue = None
            if Resp.isdigit():
                Continue = int(Resp)

            if Continue is not None and Continue == 1:
                break

    # End of game: show the total number of correct answers
    while True:
        os.system('cls')
        Resp = input(f'\nGame Over!\n\nNumber of correct answers: {Correct}\n\nType "1" to return\n\nR: ')
        
        Back = None
        if Resp.isdigit():
            Back = int(Resp)

        if Back is not None and Back == 1:
            break

# Main function to initiate the quiz
def Start():

    # Example: Geography question bank
    Geography_Bank = [
        {
            'Pergunta': 'How many continents are there in the world?',
            'Opcao': ['Five', 'Six', 'Seven', 'Eight'],
            'Resposta': 'Six'
        },
        {
            'Pergunta': 'What is the largest continent in the world?',
            'Opcao': ['Asia', 'Europe', 'North America', 'Africa'],
            'Resposta': 'Asia'
        },
        {
            'Pergunta': 'What is the smallest continent in the world?',
            'Opcao': ['North America', 'Oceania', 'Europe', 'Africa'],
            'Resposta': 'Oceania'
        }
        # Additional questions can be added here...
    ]

    while True:
        os.system('cls')
        Resp = input('\n* Quiz Menu *\n\n1- Geography Quiz\n2- Exit\n\nR: ')
        
        Menu = None
        if Resp.isdigit():
            Menu = int(Resp)
        
        if Menu is not None:
            if Menu == 2:
                print('\nQuiz ended!')
                break
            elif Menu == 1:
                Print_Questions(Geography_Bank, 'Geography')
            else:
                # If invalid option, prompt to return
                while True:
                    os.system('cls')
                    Resp = input('\nInvalid option!\n\nType "1" to return\n\nR: ')
                    
                    Back = None
                    if Resp.isdigit():
                        Back = int(Resp)
                    
                    if Back is not None and Back == 1:
                        break

# Start the game
Start()
