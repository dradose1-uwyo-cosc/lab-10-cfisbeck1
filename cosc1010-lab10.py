# Connor Fisbeck
# UWYO COSC 1010
# 11/20/2024
# Lab10
# Lab Section: 15
# Sources, people worked with, help given to: 
# Lecture slides
# python crash course

#import modules you will need 

from hashlib import sha256 
from pathlib import Path

def get_hash(to_hash):
    """You can use """
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()



# Files and Exceptions

# For this assignment, you will be writing a program to "crack" a password. You will need to open the file `hash` as this is the password you are trying to "crack."

# To begin, you will need to open the 'rockyou.txt' file:
# - This file contains a list of compromised passwords from the rockyou dump.
# - This is an abridged version, as the full version is quite large.
# - The file contains the plaintext version of the passwords. You will need to hash them to check against the password hash you are trying to crack.
#   - You can use the provided `get_hash()` function to generate the hashes.
#   - Be careful, as "hello" and "hello " would generate a different hash.

# You will need to include a try-except-catch block in your code.
# - The reading of files needs to occur in the try blocks.


# - Read in the value stored within `hash`.
#   - You must use a try and except block.


# Read in the passwords in `rockyou.txt`.
# - Again, you need a try-except-else block.
# Hash each individual password and compare it against the stored hash.
# - When you find the match, print the plaintext version of the password.
# - End your loop.
#####################################################################################################

#specify file paths
hash_file = Path('hash')
rockyoufile = Path('rockyou.txt')

#open and read the hash file
keep_going = True
try:
    given_hash = hash_file.read_text()
except FileNotFoundError:
    print(f"'{hash_file}' file not found.")
    keep_going = False
else: 
    HashToCrack = given_hash

if keep_going == True:
    try:
        passwords = rockyoufile.read_text()
    except FileNotFoundError:
        print(f"'{rockyoufile}' file not found.")
    else:
        # split rockyou.txt into lines
        rockyouLines = passwords.splitlines()
        
        #check lines one at a time converting the password to a hash 
        for line in rockyouLines:
            password = line.strip()
            new_hash = get_hash(password)
            
            #if created hash is the given hash, print the password
            if new_hash == HashToCrack:
                print(f"The password is {password}")
                break