
#This was part of the way I originally went about writing the high score to a separate file.
#I have since changed it so it is all done within the scoreboard class.
def read():
    with open("data.txt", mode="r") as file:
        read_data = file.read()
        return(read_data)

def write(new_score):
    with open("data.txt", mode="w") as file:
        file.write(new_score)