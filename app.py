def read_file():
    print("Reading file 'whitelist.txt'")
    f = open("whitelist.txt", "a+")

    for x in f.readlines():
        print(x)
    f.close()


def write_file():
    print("Writing to file..")
    f = open("Whitelist.txt", "a+")
    steamID = input("Type in Steam ID: " + "\n")
    f.write(steamID + ";" + "\n")
    f.close()


read_file()
print("\n")
write_file()
print("\n")
read_file()
