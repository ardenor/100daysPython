# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# with open("new_file.txt", "a") as file:
#     file.write("\ntesting")

PLACEHOLDER = "[name]"

with open("invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"{stripped_name}_output.txt", "w") as output_letter:
            output_letter.write(new_letter)