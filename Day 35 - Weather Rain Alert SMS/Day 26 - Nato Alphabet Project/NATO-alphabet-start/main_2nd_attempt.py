import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter:row.code for index,row in data.iterrows() }
user_word = input("Enter a word: ").upper()
phonetic = [data_dict[letter] for letter in user_word]
print(phonetic)
