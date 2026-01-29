import pandas

phonetic = pandas.read_csv("nato_phonetic_alphabet.csv") #reads the file and creates the dataframe  titles/columns of letter, code   rows of for example 0  A  'Alpha' , 1  B  'Bravo'
phonetic_dict = {row.letter.upper():row.code for (index,row) in phonetic.iterrows()} # creates a dictionary from the dataframe. Using iterrows to loop through each row.
# eg row.letter gets us 'A' , row.code gets us 'Alpha'

word = input("Enter a Word: ").upper()
output = [phonetic_dict[letter] for letter in word] #loops through each letter in 'word' , finds the letter and using it as the key gives us the value from phonetic_dict eg 'F' is 'Foxtrot'
print(output)


