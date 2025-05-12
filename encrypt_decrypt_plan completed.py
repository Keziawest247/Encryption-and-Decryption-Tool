"""Encryption and Decryption program Plan."""

def read_text_file(filename: str) -> str:
    with open(filename, mode="r") as text_file:
        return text_file.read().lower()

def encrypt_text(plain_text: str, shift: int) -> list: # plain text = text that hasn't been encrypted
    encrypted = []
    for char in plain_text:
        encrypted.append(str(ord(char) + shift))
        # print(char, ord(char) + shift) # every char has a numerical value; give me the value this character.
    return encrypted

def write_encrypted_file(cypher_text: list, filename: str) -> None:
    cypher_text_string = " ".join(cypher_text) # string method; join everything in this interval.
    cypher_file_name = "ENCRYPTED_" + filename # make the file name
    with open(cypher_file_name, mode="w") as file: # open the file
        file.write(cypher_text_string)

def decrypt_cyphertext(cypher_text: list, shift: int) -> None:

    character_list = cypher_text.split() # take this and convert into a list
    decrypt_text = ""
    for char in character_list:
        print(chr(int(char) - shift))

    print("Decrypted:", decrypted_text)

def driver_function(filename: str, shift: int, encrypt: bool = True): # by default we're encrypting
    print("Filename", filename)
    print("Shift", shift)

    try: # opens the file
        file_contents = read_text_file(filename) #try to accept a string
    except FileNotFoundError:
        print(f"'{filename}'does not exist.")
        return # stop hear if stuff goes wrong unexpectedly

    if encrypt:
        encrypted_text = encrypt_text(file_contents, shift)
        write_encrypted_file(encrypted_text, filename) # list of string numbers
    else:
        decrypt_cyphertext(file_contents, shift)


filename = "ENCRYPTED_hello.txt"
shift = 4
driver_function(filename, shift, encrypt=True)

# decrypt mode encrypt=False
# encrypt mode encrypt=True





