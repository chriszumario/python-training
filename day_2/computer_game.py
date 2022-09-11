import random

options = ['rock', 'paper', 'scissors']
while True:
    print('''
Choose an Option
0. Rock
1. Paper
2. Scissors
3. Exit
    ''')
    computer = random.choice(options)
    option = int(input('=>'))
    if option == 3:
        break
    user = options[option]
    print(f'Computer: {computer}')
    print(f'User: {user}')
    if computer == options[0] and user == options[1]:
        print('Won')
    elif computer == options[1] and user == options[2]:
        print('Won')
    elif computer == options[2] and user == options[0]:
        print('Won')
    elif computer == options[1] and user == options[0]:
        print('You lost')
    elif computer == options[2] and user == options[1]:
        print('You lost')
    elif computer == options[0] and user == options[2]:
        print('You lost')
    elif computer == user:
        print('Equality')
