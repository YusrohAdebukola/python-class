print('Hello!, Welcome to the Hangman game')
introduction_2 = 'There are five options, pick an option of your choice!'
print(introduction_2)
guess_lives = 5
options = {'1':'movies','2':'cities','3':'foods','4':'carbrands','5':'fruits' }
print(options)
guess_lives = 5
movies = ('Purple Hearts','Moana','Mulan','Encanto','Matilda' )
cities = ('Lagos','Maldives','Washington','Alabama','Oyo')
foods = ('Lasagne','Burritos','Croissant','Kebab','Pizza')
carbrands = ('Bugatti','Toyota','Lamborghini','Honda','Mercedes Benz')
fruits = ('Tamarind','Cucumber','Apples','Mandarine','Kiwi')
hint_1 = 'Movie genre was not considered'
hint_2 = 'Cities all over the world'
hint_3 = 'Foods you will find delicious'
hint_4 = 'Popular carbrands'
hint_5 = 'Some fruits included are pretty popular, you might have to think a little depper for others'
while guess_lives > 0:
    guess_input = input('Enter an option: ').lower()
    if guess_input in '1':
        print(hint_1)
        guess_input = input('Enter a movie: ').lower()
        import random
    if guess_input in movies:
        print('correct')
    else:
        print('Incorrect!, Try Again')
        guess_lives -= 1

        # if guess_input in 2:
        #     print(hint_2)
        #     guess_input = input('Enter a city')
        #     import random


# variable_1= {'*****'}
# variable_2 = {'*******'}
# variable_3 = {'**********'}
# variable_4 = {'*******'}
# variable_5 = {'***'}
# variables = list(variable)
# print(variables)
# Hint = '----i-e-'
# print(Hint)
# Hint = list(Hint)
# while guess_lives > 0:
#     guess_input = input('Guess a city: ').lower()
#     if guess_input in guess_word:
#         letter_index = guess_word.index(guess_input)
#         variables[letter_index] = guess_input
#         variable = ''.join(variables)
#         print(variable)
#     else:
#             print('Incorrect!,Try Again')
#             guess_lives -= 1


