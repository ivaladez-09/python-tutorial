# my_file = open("Files/test.txt")
# print(my_file.readlines())
# my_file.close()

# Read/Write the file
try:
    with open("Files/test.txt", mode="a") as my_file:
        # Be carefull, if you open the file just for writting, it will override your content
        text = my_file.write("\nHey! It is me")
        print(text)
except (FileNotFoundError, IOError) as err:
    print(f"Error found: {err}")

    # print(my_file.readlines())
