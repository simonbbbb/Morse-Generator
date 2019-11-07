def smorse(word):
    morse = {}
    morse_abc = '.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.. .---- ..--- ...-- ....- ..... -.... --... ---.. ----. ----- '
    letters = 'abcdefghijklmnopqrstuvwxyz1234567890 '


    for num, letter in enumerate(morse_abc.split(' ')):
        morse[letters[num]] = letter

    result = ''
    for letter in word:  # For each letter in the inputed sequence
        result += morse[letter] + ' '  # Added whitespace padding for clarity
    print(result)

morselower = input('Input a word or number: ')
smorse(morselower.lower())