key = int(input('Enter key:'))
message = input('Enter message:')
# mess = 'The quick brown fox jumps over the lazy dog.'
# key = 1
alphabet_lowercase = 'abcdefghijklmnopqrstuvwxyz'
alphabet_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
new_mess = ''
for letter in message:
    if letter not in alphabet_uppercase:
        t = alphabet_lowercase.find(letter)
        new_t = t + key
        if new_t >= (len(alphabet_lowercase)):
            new_t = abs( len(alphabet_lowercase) - t  - key )
        if t == -1:
            new_letter = letter
        else:
            new_letter = alphabet_lowercase[new_t]
        new_mess = new_mess + new_letter
    else:
        t = alphabet_uppercase.find(letter)
        new_t = t + key
        if new_t >= (len(alphabet_uppercase)):
            new_t = abs( len(alphabet_lowercase) - t  - key )
        if t == -1:
            new_letter = letter
        else:
            new_letter = alphabet_uppercase[new_t]
        new_mess = new_mess + new_letter

print('Result: ', new_mess)