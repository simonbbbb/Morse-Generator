# Coding Challange #380 - r/dailyprogrammer
# Morse translator

def smorse(word):
    morse = {}
    morse_abc = '.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..'
    letters = 'abcdefghijklmnopqrstuvwxyz'


    for num, letter in enumerate(morse_abc.split(' ')):
        morse[letters[num]] = letter

    result = ''
    for letter in word:  # For each letter in the inputed sequence
        result += morse[letter] + ' '  # Added whitespace padding for clarity
    print(result)


smorse(input('Input a word: '))