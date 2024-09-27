alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt,"
                  " type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# Create a function called 'decrypt()' that takes 'original_text'
#  and 'shift_amount' as inputs.

# Inside the 'decrypt()' function,
#  shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.

# def decrypt(original_text, shift_amount):
#     output_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) - shift_amount
#         shifted_position %= len(alphabet)
#         output_text += alphabet[shifted_position]
#
#     print(f"Here is the decoded result: {output_text}")

# Combine the 'encrypt()' and 'decrypt()' functions
#  into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine
#  which functionality to use.


def caesar(message, original_text, shift_amount):
    output_text = ""

    if message == "decode":
        shift_amount *= -1

    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]

    print(f"Here is the {message}d result: {output_text}")


# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]
#     print(f"Here is the encoded result: {cipher_text}")


caesar(message=direction, original_text=text, shift_amount=shift)
