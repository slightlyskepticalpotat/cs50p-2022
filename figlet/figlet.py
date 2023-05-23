import sys, random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(figlet.getFonts()))
elif len(sys.argv) == 2:
    sys.exit("Invalid usage")
elif len(sys.argv) == 3:
    if sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Invalid usage")
    if sys.argv[2] not in figlet.getFonts():
        sys.exit("Invalid usage")
    figlet.setFont(font=sys.argv[2])
print(f"Output: {figlet.renderText(input('Input: '))}")
