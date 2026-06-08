def add_log(message):
    with open("output.txt","a") as file:
        file.write(message+'\n')

add_log("User logged in")
add_log("File Uploaded")