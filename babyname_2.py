import random, string

#great to crete our own functions, 5 seperate random letters for 5 sep variables
def generator():
    letter1 = random.choice( string.ascii_lowercase )
    letter2 = random.choice( string.ascii_lowercase )
    letter3 = random.choice( string.ascii_lowercase )
    letter4 = random.choice( string.ascii_lowercase )
    letter5 = random.choice( string.ascii_lowercase )
    name = letter1 + letter2 + letter3 + letter4 + letter5
    return( name )

print(generator())

#lets now ask user for some input

letter_input_1 = input('Choose a letter..."w" for vowels, "c" for consonants, ""')