from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(option, plain_text, shift_amount):
    if option == "decode":
        shift_amount *= -1
    new_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            new_text += new_letter
        else:
            new_text += char
    print(f"You choose to {option} and the result is: {new_text}")
   

should_exit = False
while not should_exit:

    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(option=direction, plain_text=text, shift_amount=shift)

    restart = input("Press any key to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f'The encoded text is {cipher_text}')
#     ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         plain_text += new_letter
#     print(f'The encoded text is {plain_text}')

# if direction == 'encode':
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == 'decode':
#     decrypt(cipher_text=text, shift_amount=shift)