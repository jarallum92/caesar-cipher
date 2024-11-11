# add your code here
alphabet = "abcdefghijklmnopqrstuvwxyz"

def caesar_cipher(text, shift):
    encrypted_sentence = ""


    for char in sentence:
        if char.islower():
            encrypted_sentence += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_sentence += char

    return encrypted_sentence
    
shift = 5
sentence = input("Please enter a sentence: ")
text = sentence.lower()

print("The encrpyted sentece is:", caesar_cipher(text, shift))