text = input('What is the Answer to the Great Question of Life, the Universe, and Everything? ')

if text.strip() == '42':
    print('Yes')
elif text.lower().strip() == 'forty-two':
    print('Yes')
elif text.lower().strip() == 'forty two':
    print('Yes')
else:
    print('No')