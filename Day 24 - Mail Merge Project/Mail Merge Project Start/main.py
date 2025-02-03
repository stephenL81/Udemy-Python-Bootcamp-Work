with open("Input/Names/invited_names.txt") as names:
    names_list = names.readlines()

with open("Input/Letters/starting_letter.txt",mode="r") as letter:
    template = letter.read()

for person in names_list:
    with open(f"Output/ReadyToSend/Letter_for_{person}.txt",mode="w") as letter:
        letter.write(template.replace("[name]",person.strip("\n")))



