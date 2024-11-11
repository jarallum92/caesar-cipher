# add your code here
alphabet = "abcdefghijklmnopqrstuvwxyz"

def caesar_cipher(text, shift):
    encrypted_sentence = ""


    for char in sentence:
        if char.islower():
            # shifting the letters in the sentence
            encrypted_sentence += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_sentence += char 
            # keeping the non letters where they are

    return encrypted_sentence
    
shift = 5 
# the amount of letters shifting
sentence = input("Please enter a sentence: ")
text = sentence.lower()

print("The encrpyted sentece is:", caesar_cipher(text, shift))