
ALPHABET_SIZE: int = 26

message: str = input("Message: ")  
key: int = int(input("Key: "))

ciphertext: str = ""
shifted: int

# Encryption loop
for character in message: 
    if "A" <= character <= "Z":     #check whether our character is between "A" and "Z" 
        shifted = ord(character) + key  
        if shifted > ord("Z"):
            shifted -= ALPHABET_SIZE
        ciphertext += chr(shifted)

    elif "a" <= character <= "z":    #check whether our character is between "a" and "z" (Lowercase letters)
        shifted = ord(character) + key  
        if shifted > ord("z"):
            shifted -= ALPHABET_SIZE
        ciphertext += chr(shifted)

    else: 
         ciphertext += character

print("Ciphertext: ",ciphertext)

plaintext: str = ""

# Decryption loop
for character in ciphertext: 
    if "A" <= character <= "Z":              
        shifted = ord(character) - key  
        if shifted < ord("A"):
            shifted += ALPHABET_SIZE
        plaintext += chr(shifted) 

    elif "a" <= character <= "z":
        shifted = ord(character) - key  
        if shifted < ord("a"):
            shifted += ALPHABET_SIZE
        plaintext += chr(shifted)
     
    else: 
        plaintext += character

print("Plaintext: ",plaintext)
        
# Check if the message equals the plaintext
assert message == plaintext, "The encryption-decryption loop doesn't close"