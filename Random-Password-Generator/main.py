#random password generate of 8 length

import random
import string

pass_len = int(input("Enter The Length to generate Password: "))

char_Value = string.ascii_letters + string.digits + string.punctuation


password = "".join(random.choice(char_Value) for i in range(pass_len))

print("Your Random Password is: ", password)