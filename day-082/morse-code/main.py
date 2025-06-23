from data import MORSE_CODE_DICT

GAP_BETWEEN_LETTERS = " "
GAP_BETWEEN_WORDS = "    "

message_to_convert = input("Type a string to be converted to Morse code: ")

morse_code_output = ""
for char in message_to_convert.upper():
    if char == " ":
        morse_code_output += GAP_BETWEEN_WORDS
    elif char not in MORSE_CODE_DICT:
        print(f"Skipping {char} as it not available in Morse code.")
    else:
        morse_code_output += MORSE_CODE_DICT[char]
        morse_code_output += GAP_BETWEEN_LETTERS

print(morse_code_output)
