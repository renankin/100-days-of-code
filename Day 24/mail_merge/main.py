PLACEHOLDER = "[name]"

# Extract names from invited list
with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

# Open example letter and store lines in a list
with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        new_letter = letter_content.replace(PLACEHOLDER, name.strip())
        # Create new letter with replaced headings
        with open(f"Output/ReadyToSend/letter_for_{name.strip()}.txt",
                  mode="w") as file:
            file.write(new_letter)
