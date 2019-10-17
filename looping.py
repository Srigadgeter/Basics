# >>>>> While Loops <<<<<
i = 1
while i <= 3:
    print('@' * i, i)
    i = i + 1
print('While ends & this statement is out of while loop')
# =========================================
# Game 1
secret_number = 3
guess_count = 1
guess_limit = 3
print('You have three chances to guess the secret number occur between 0 and 10')
# else block for the while loop will execute after the while loop iterations finished
# else block for the while loop won't execute if the while loop breaks in the middle of iterations
while guess_count <= guess_limit:
    guess = int(input('Guess ' + str(guess_count) + ': '))
    if guess == secret_number:
        print('You Found :)')
        break
    else:
        guess_count += 1
else:
    print('You guessed wrong for the given chances :(')
# =========================================
# Game 2
isQuit = False
isBikeStarted = False
print('Game started')
while not isQuit:
    entered_command = input('> ').lower()
    if entered_command == 'quit':
        print('You quit the game')
        isQuit = True
    elif entered_command == 'help':
        print('''
Commands List to operate the bike:
    help - To see the commands list
    start - To start the bike
    stop - To stop the bike
    quit - To exit the game
        ''')
    elif entered_command == 'start':
        if isBikeStarted == True:
            print('Yeah, Bike is already started')
        else:
            isBikeStarted = True
            print('Bike started... Ride speed to get thrill')
    elif entered_command == 'stop':
        if not isBikeStarted == True:
            print('Yeah, Bike is already stopped')
        else:
            isBikeStarted = False
            print('Bike stopped')
    else:
        print("I don't understand your command")
# =========================================
# >>>>> For Loops <<<<<
for item in 'Gamer':
    print(item)

for item in ['i', 'am', 'python', 'programmer']:
    print(item)

# range(start_number, end_number, increment_number) <<== end_number is exclusive
for item in range(5):
    print(item)

for item in range(5, 10):
    print(item)

for item in range(2, 10, 3):
    print(item)

for x in range(3):
    for y in range(2):
        print(f'({x}, {y})')

for x in [5, 2, 5, 2, 2]:
    liner = ''
    for y in range(x):
        liner += 'x'
    print(liner)
