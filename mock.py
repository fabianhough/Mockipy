

sentence = str(input('\nPlease enter a string to mockify:\n'))

new_sentence = ''
count = 0
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

for letter in sentence:
    if letter in alphabet:
        if count % 2 == 1:
            new_sentence += letter.upper()
        else:
            new_sentence += letter.lower()
        count += 1
    else:
        new_sentence += letter


print('\nMock Away!:\n{}\n'.format(new_sentence))