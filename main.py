import random as rd
import array
import pyperclip

# initializing the sets of different characters that our randomly generated password will utilise
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

LOWERCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                        'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                        'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                        'z']

UPPERCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                        'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                        'Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']


# collecting user input from the user
password_length = int(
    input('Hello - Please Enter Length of Desired Password: '))
temp_pass = rd.choice(DIGITS) + rd.choice(SYMBOLS) + \
    rd.choice(LOWERCASE_CHARACTERS) + rd.choice(UPPERCASE_CHARACTERS)

# generating the rest of the password once characters from all categories have been selected at least once
for x in range(password_length - 4):
    gen_rand = rd.randint(1, 4)

    # will randomly choose one of the sets of characters to choose a random character from
    switch = {
        1: rd.choice(DIGITS),
        2: rd.choice(SYMBOLS),
        3: rd.choice(LOWERCASE_CHARACTERS),
        4: rd.choice(UPPERCASE_CHARACTERS)
    }

    # append to temp_pass and shuffle to ensure no pattern can be detected
    temp_pass += switch.get(gen_rand)
    temp_pass_list = array.array('u', temp_pass)
    rd.shuffle(temp_pass_list)

# converting the list to a string
password = ""
for char in temp_pass_list:
    password += char

# outputting the password to the user
print(f'Password of Length {password_length} : {password}')

# giving them the option to copy and paste newly generated password to their clipboard
copy_to_clipboard = input(
    'Would you like to copy this to your clipboard [Y or N]: ')

if copy_to_clipboard == 'Y':
    pyperclip.copy(password)
    print('Password copied to clipboard!')
