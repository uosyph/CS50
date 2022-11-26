text = input('Gretting: ').lower().strip()

if 'hello' in text:
    print('$0')
elif 'h' == text[0]:
    print('$20')
else:
    print('$100')