
# num = "Contoso" == "contoso"
# print(num)


# 1.
# num = ord("G") # character -> number
# print(num)

# letter = chr(78) # number -> character
# print(letter)

# 2.
# key = 3
# plaintext_letter = "M" # "MEET AT NOON" (plaintext)

# shifted_number = ord(plaintext_letter) + key
# letter = chr(shifted_number)

# # print(letter)

# ciphertext_letter = "P" # "=" storing (i.e assignment)

# assert letter == ciphertext_letter
# # "==" equality operater (compare two things)

# 3.
# output: "print"
# input: "input"
# type: "data type of the variable"


# print(type(message))
# print(type(key))

# message: str = input("Message: ")
# key: int = int(input("Key: "))

# # # 'str' -> STRING (words)
# # # 'int' -> INTEGER (whole numbers)

# ciphertext = ""

# for letter in message: # loop
#     ciphertext_letter = chr(ord(letter) + key)
#     # print(ciphertext_letter, end="")
#     ciphertext += ciphertext_letter



# print(ciphertext)

# message = "UPDATE"

# "U" -> "X"
# "P" -> "S"
# "D" -> "G"
# "A" -> "D"
# "T" -> "W"
# "E" -> "H"

# "" -> "" + "X" -> "X"
# "X" -> "X" + "S" -> "XS"
# "XSG"
# "XSGD"

# 4.
ALPHABET_SIZE = 26

message: str = input("Message: ")
key: int = int(input("Key: "))

ciphertext = ""

for letter in message: 
    shifted = ord(letter) + key
    if shifted > ord("Z"):
        shifted -= ALPHABET_SIZE
    ciphertext += chr(shifted)
    


    # If ciphertext_letter goes beyond "Z", the corresponding answer will be wrong
    

print(ciphertext)