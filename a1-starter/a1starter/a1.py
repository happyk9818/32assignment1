# a1.py

# Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Taekyung
# taekyk1@uci.edu
# 44996270

import os
from pathlib import Path

def option_f(directory):
    files = os.listdir(directory)
    for file in files:
        fullname_file = os.path.join(directory, file)
        if os.path.isdir(file) == True:
            print(fullname_file)

def option_s(directory):
    file_name = input()
    files = os.listdir(directory)
    for file in files:
        fullname_file = os.path.join(directory, file)
        if file_name == fullname_file:
            print(fullname_file)           

def option_e(directory):
    ext_type = input()
    files = os.listdir(directory)
    for file in files:
        fullname_file = os.path.join(directory, file)
        if file.endswith(ext_type):
            print(fullname_file)

def option_r(directory, option_input):
    files = os.listdir(directory)
    for file in files:
            fullname_file = os.path.join(directory, file)
            if os.path.isdir(fullname_file):
                option_r(fullname_file, option_input)
                if option_input == "-f":
                    return option_f(fullname_file)
                elif option_input == "-s":
                    return option_s(fullname_file)
                elif option_input == "-e":
                    return option_e(fullname_file)
            else:
                print(fullname_file)


def read_text_file(directory):
    with open(directory, 'r') as f:
        print(f.read())


def option_C(directory, user_option, user_file_name):
    files = os.listdir(Path(directory) / user_file_name)
    if user_option == "-n":
        if not files.exists():
            os.makedirs(files)
            filename = user_file_name + '.dsu'
            with open(os.path.join(files, filename), 'wb') as temp_file:
                temp_file.touch(exist_ok=True)
        else:
            print("Name of the file aready exists, please enter valid name")
    else:
        print("Enter valid option")


def option_D(directory):
    files = os.listdir(Path(directory))
    if files.exists():
        if files.endswith(".dsu"):
            os.remove(os.path.join(directory, files))
        else:
            print("ERROR")
        return option_D(directory)
    else:
        print("file does not exsit")


def option_R(directory):
    files = os.listdir(Path(directory))
    if files.exists():
        if files.endswith(".dsu"):
            if os.path.getsize(files) == 0:
                print("EMPTY")
            else:
                read_text_file(directory)
        else:
            print("ERROR")
        return option_D(directory)
    else:
        print("file does not exsit")


def L_Input(user_directory, user_option):
    if user_option == "-r":
        option_input = input() #option의 input
        return option_r(user_directory, option_input) #Output directory content recursively
    elif user_option =="-f":
        return option_f(user_directory) #Output only files, excluding directories in the results
    elif user_option == "-s":
        return option_s(user_directory) #Output only files that match a given file name
    elif user_option == "-e":
        return option_e(user_directory) #Output only files that match a given file extension
    else:
        print("Invalid option of the L -input.")

def Command(user_input, user_directory):
    if user_input == "L":
        option = input() #-r, -f, -s, -e options
        return L_Input(user_directory, option) #List the contents of the user specified directory. -> L_command
    
    elif user_input == "C":
        option = input()
        file_name = input()
        #Create a new file in the specified directory.
        option_C(user_directory, option, file_name)
    elif user_input == "D":
        #Delete the file.
        option_D(user_directory)
    elif user_input == "R":
        #Read the contents of a file.
        option_R(user_directory)
    
    elif user_input == "Q":
        quit() #Quit the program. *COMPLETE

def main():
    user_input = input() #L or Q
    user_directory = input() # address of the file listing
    Command(user_input, user_directory)


#[COMMAND] [INPUT] [[-]OPTION] [INPUT]

if __name__ == "__main__":
    main()
