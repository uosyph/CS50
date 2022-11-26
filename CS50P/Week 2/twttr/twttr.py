text = input('Input: ')
vowels = 'aeiouAEIOUE'
for char in vowels:
    text = text.replace(char, '')

print(text)