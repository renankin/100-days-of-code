import pandas as pd

# Create a dictionary in this format using dictionary comprehension:
# {"A": "Alfa", "B": "Bravo"}
df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dict = {row.letter: row.code for (index, row) in df.iterrows()}

# Create a list of phonetic word that the user inputs
word = input("Type a word: ").upper()
output_list = [nato_alphabet_dict[letter] for letter in word]
print(output_list)
