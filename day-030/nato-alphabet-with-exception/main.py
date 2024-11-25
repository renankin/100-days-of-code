import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dict = {row.letter: row.code for (index, row) in df.iterrows()}


def generate_phonetic():
    word = input("Type a word: ").upper()
    try:
        output_list = [nato_alphabet_dict[letter] for letter in word]
    except KeyError:
        print("Sorry only list in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
