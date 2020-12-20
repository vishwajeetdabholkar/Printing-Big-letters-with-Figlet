from pyfiglet import Figlet
word = input("Enter the word to print in big letters:")
f = Figlet(font='slant')
print(f.renderText(word))
