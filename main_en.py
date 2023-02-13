from random import randrange

start = int(input('Type the start of the range: '))
end = int(input('Type the end of the range: '))

number = randrange(start, end)
guess = 0
attempt = 0

while guess != number:
    guess = int(input('\nGuess the random number of the range: '))

    if guess < start or guess > end:
        print('Your guess is not a option. Try again.')
    elif number == guess:
        print(f'Congratulations, you guessed the number in {attempt} attempts!')
    elif number - guess > 3 or guess - number > 3:
        if number > guess:
            print('Too far! Try a higher number')
            attempt += 1
        else:
            print('Too far! Try a lower number.')
            attempt += 1
    else:
        print('Almost there! Try again.')
        attempt += 1
