import random as rd 
import array

# initializing the sets of different characters that our randomly generated password will utilise 
DIGITS = ['0','1','2','3','4','5','6','7','8','9']

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


COMBINED_LIST = []


# collecting user input from the user 
password_length = int(input('Hello - Please Enter Length of Desired Password: '))
temp_pass = rd.choice(DIGITS) + rd.choice(SYMBOLS) + rd.choice(LOWERCASE_CHARACTERS) + rd.choice(UPPERCASE_CHARACTERS)

for x in range(password_length - 4):
    gen_rand = rd.randint(1,4)

    switch={
        1:rd.choice(DIGITS),
        2:rd.choice(SYMBOLS),
        3:rd.choice(LOWERCASE_CHARACTERS),
        4:rd.choice(UPPERCASE_CHARACTERS)
    }

    temp_pass += switch.get(gen_rand)
    temp_pass_list = array.array('u', temp_pass)
    rd.shuffle(temp_pass_list)


password = ""
for char in temp_pass_list:
    password += char


print(f'Password of Length {password_length} : {password}')
