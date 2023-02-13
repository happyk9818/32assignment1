import a1p1
import os
from pathlib import Path

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


def Command(user_input, user_directory):
    if user_input == "L":
        option = input() #-r, -f, -s, -e options
        return a1p1.L_Input(user_directory, option) #List the contents of the user specified directory. -> L_command
    
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
