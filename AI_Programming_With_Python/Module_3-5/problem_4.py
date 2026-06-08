def  read_from_position(filename, position):
    with open(filename+".txt", "r") as file:
        file.seek(position)
        print(file.read())

read_from_position("try1", 4)