import sys
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar():
    types = input("Would you like to \"encode\" or \"decode\"?\n").lower()
    text = input("Enter text: \n").lower()
    shift = int(input("By how many digits would you like to shift? \n"))
    if types == "encode":
        encrypt(text,shift)
    if types == "decode":
        decrypt(text,shift)

def encrypt(text,shift):
    encrypted_text = ""
    for letter in text:
        if letter in alphabet:
            pos = alphabet.index(letter)
            new_pos = pos + shift
            if new_pos >= len(alphabet):
                index2 = new_pos - len(alphabet)
            elif new_pos < len(alphabet):
                index2 = new_pos
            encrypted_text += alphabet[index2]
        else:
            encrypted_text += letter

    print("YOUR ENCRYPTED TEXT IS: ",encrypted_text)
    now = input("ENTER \'Y\' TO CONTINUE OR \'N\' TO QUIT:\n")
    if now == "Y":
        caesar()
    elif now == "N":
        sys.quit()

def decrypt(text,shift):
    decrypted_text = ""
    for letter in text:
        if letter in alphabet:
            pos = alphabet.index(letter)
            new_pos = pos - shift
            if new_pos < 0:
                index2 = new_pos + len(alphabet)
            elif new_pos >= 0:
                index2 = new_pos
            decrypted_text += alphabet[index2]
        else:
            decrypted_text += letter

    print("YOUR DECRYPTED TEXT IS: ",decrypted_text)
    now = input("ENTER \'Y\' TO CONTINUE OR \'N\' TO QUIT:\n")
    if now == "Y":
        caesar()
    elif now == "N":
        sys.quit()

caesar()

    