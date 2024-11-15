absolute_file_path = "/Users/renankin/Desktop/my_file.txt"
relative_file_path = "../../../Desktop/my_file.txt"
with open(relative_file_path) as file:
    contents = file.read()
    print(contents)

# with open("new_file.txt", mode="w") as file:
#     file.write("New text.")
