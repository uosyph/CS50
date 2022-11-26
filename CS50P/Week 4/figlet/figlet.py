import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 3:
    try:
        if sys.argv[1] == '-f' or sys.argv[1] == '--font':
            try:
                figlet.setFont(font=sys.argv[2])
            except:
                sys.exit('Invalid usage')
        else:
            sys.exit('Invalid usage')
    except IndexError:
        sys.exit('Invalid usage')
else:
    sys.exit('Invalid usage')

text = input()
print(figlet.renderText(text))