def read_lines(filename):
    with open(filename, "r") as file:
        content = file.readlines()
        for i in range(0, len(content)):
            print(str(i+1) +" "+ content[i])

read_lines("test_p2.txt")