def create_file(file_name, content):
    with open("./"+file_name+".txt","a") as file:
        file.write(content)

create_file("try1", "Hello !!")