'''6.Data Validation System – Character Identifier
A system needs to validate user input characters.
If the input is:
Alphabet → display "Alphabet"
Digit → display "Digit"
Otherwise → display "Special Character"
Write a program using inline if to classify the character.'''

ch = input("Enter Character = ")

print("Alphabet") if 'a' <= ch.lower() <= 'z' else print("Digit") if '0' <= ch <= '9' else print("Special Character")