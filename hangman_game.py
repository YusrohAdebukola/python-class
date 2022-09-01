from ntpath import join


print('Hello!, Welcome to the Hangman')
guess_word = 'Maldives'
guess_lives = 3
variable = '********'
variable = list(variable)
print(variable)
Hint = 'M--d--e-'
print (Hint)
Hint = list(Hint)
while guess_lives >= 0:
    guess_input = input('Guess a city: ')
    if guess_input in guess_word:
        print ('correct')
        letter_index = guess_word.index(guess_input)
        variable[letter_index] = guess_input
        variable = ''.join(variable)
        print(variable)
    else:
        print('Try again')
        guess_lives -= 1

    

    