#a1p1.py

# Starter code for lab 3 in ICS 32 Programming with Software Libraries in Python
import os

def option_r(directory):
    option_input = input() #option의 input
    files = os.listdir(directory)
    for file in files:
            fullname_file = os.path.join(directory, file)
            if os.path.isdir(fullname_file):
                option_r(fullname_file)
            else:
                print(fullname_file)

def option_f(directory):
    files = os.listdir(directory)
    for file in files:
        if os.path.isdir(file) == True:
            name, ext = os.path.splitext(file)
            print(name + '\t' + ext)

def option_s(directory):
    file_name = input()
    files = os.listdir(directory)
    for file in files:
        fullname_file = os.path.join(directory, file)
        if file_name == fullname_file:
            print(fullname_file)           

def option_e(directory): #원하는 ext type을 호출하는 것이다.
    ext_type = input()
    files = os.listdir(directory)
    for file in files:
        fullname_file = os.path.join(directory, file)
        if file.endswith(ext_type):
            print(fullname_file)

def L_Input(user_directory, user_option):
    if user_option == "r":
        return option_r(user_directory) #Output directory content recursively
    elif user_option =="f":
        return option_f(user_directory) #Output only files, excluding directories in the results
    elif user_option == "s":
        return option_s(user_directory) #Output only files that match a given file name
    elif user_option == "e":
        return option_e(user_directory) #Output only files that match a given file extension
    else:
        print("Invalid option of the L -input.")

def Command(user_input, user_directory):
    if user_input == "L":
        files = os.listdir(user_directory)
        for file in files:
            fullname_file = os.path.join(user_directory, file)
            print(fullname_file) #List the contents of the user specified directory. *COMPLETE
            option = input() #-r, -f, -s, -e options
            return L_Input(user_directory, option) #List the contents of the user specified directory. -> L_command
    elif user_input == "Q":
        quit() #Quit the program. *COMPLETE

#[COMMAND] [INPUT] [[-]OPTION] [INPUT]

if __name__ == "__main__":
    user_input = input() #L or Q
    user_directory = input() # address of the file listing
    Command(user_input, user_directory)