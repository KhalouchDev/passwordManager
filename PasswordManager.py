from cryptography.fernet import Fernet

def write_key():    #Use this function to get a key
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip() #.rstrip() removes the "\n" so there will be no empty line when printing to terminal
            user, passw = data.split("|")   #.split("|") will split the string in half on the "|", and return a list with the values in this case the user and the password (khaled|p@ssw0rd --> ["khaled", "p@ssw0rd"])
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())

def add():
    name = input("Account Name: ")
    password = input("Password: ")

    with open('password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")

#write_key() #This is used to get the key, only run once

while True:     #It is put in a while so it keeps on repeating(i.e. if user wants to see the list after adding a password)
    mode = input("What mode do you want to enter? (view, add), or press q to quit ")
    if mode == "q" or mode == "Q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Mode not found.")
        continue    #This means that it will go back to the while loop (repeat) and not stop