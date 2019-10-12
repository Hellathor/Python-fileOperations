
import os
import time


open_File = "1"
create_File = "2"
delete_File = "3"

add_To_File = "1"
edit_File = "2"
view_Content = "3"
back_To_Main_Menu = "4"

folderName = "files/"
file_Extension = ".txt"

pixels1 = "##" * 15
pixels2 = "**" * 11


designPrompt1 = "Choose from the options below:\n\nCHOICE: (1, 2, 3)\n" + pixels1 + "\n1. Open File\n2. Create \
a File\n3. Delete a file\n\tPress Enter to Exit.\n" + pixels1 + "\n"

designPrompt2 = "ACTION: (1, 2, 3, 4)\n" + pixels2 + "\n1. Add_To_File.\n2. Edit_File\n3. View Content\
\n4. Back to Main Menu\n" + pixels2 + "\n"



''' From 'choice' to 'operation' to 'action' to ...

'''

def quit():
    print("App Closed!\n")
    print(" Powered By:".rjust(56, "*"), "**"*23, "\n \t \t \t\t\tEne-Une Reuben OCHEDI\n", "All Rigths Reserved.".rjust(60, " "), "\n", "(c)October, 2019".rjust(56, " "))
    print("\n", "+-" * 51)
    print("\tEmail: rubycodes14@gmail.com\t  LinkedIn: Ene-une Ochedi\t  GitHub: RubyCodes14\n\tFacebook: Ene-une Reuben Ochedi\t\t\tWhatsApp: +2348136020460")
    print("\n", "==" * 51)
    time.sleep(5)
    exit()


def uppercase(text):
    if text.isupper():
        return text
    else:
        text = text.lower()
        return text

def choice():
    print(designPrompt1)
    options = input("Enter Choice: ")
    return options




def fileName(flag):
    global filename
    global filename_
    filename = input("\nEnter desired filename: ")
    if filename == "":
        quit()
    else:
        filename_ = uppercase(filename) + file_Extension
        filename = folderName + uppercase(filename) + file_Extension
        args = flag
        flag = str(flag)
        if flag.isdigit():
            if(os.access(filename, os.F_OK)):
                return filename
            else:            
                trials = "No such file exist.\nTry again\
(Or press enter to go back to menu \[Trials remaining " + str(3 - args) + "])"
                if args > 2:
                    trials = "No such file exist.\n[Trials remaining \
" + str(3 - args) + "]"
                    print(trials)
                    quit()
                elif args <= 2:
                    args += 1
                    print(trials)
                    fileName(args)
                                
                else:
                    print("Program terminated; unsuccessful\n")
                    quit()
        else:
            return filename
            
        

def _add():
    print("ADDING CONTENT TO ", filename_) 
    try:
        record = open(filename, "a")
        add_Data = input("Enter data: ")
        char = record.write(add_Data + "\n")
        print("Data Record added Successfully!\n[You just added\
", char, "characters to your file]")
        record.close()
        action()
    finally:
        record.close()
        

def edit():
    print("EDITING ", filename_)
    try:
        record = open(filename, "w")
        edit_Data = input("Enter data: ")
        chars = record.write(edit_Data + "\n")
        print("File Record edited Successfully!\n[You just added\
", chars, "characters to your file]")
        record.close()
        action()
    finally:
        record.close()

def _view():
    print("VIEWING THE CONTENT OF ", filename_)
    try:
        view = open(filename, "r")
        output = view.read()
        print("Here is the content of your file: ", filename_)
        print(output, "\n")
        view.close()
        action()
    finally:
        view.close()

        
def action():
    print(designPrompt2)
    task = input("Action: ")
    if task == add_To_File:
        _add()
    elif task == edit_File:
        print("NOTE: This will erase the previous data in the file.\nDo you \
wish to continue?")
        print("1. Yes\n2. No\n")
        cont = input("Enter: ")
        if cont == "1":
            edit()
        elif cont == "2":
            action()
        else:
            quit()
    elif task == view_Content:
        _view()
    elif task == back_To_Main_Menu:
        choice()
    else:
        quit()


def fileExist():
    if(os.access(filename, os.F_OK)):
        return True

def file_Status():    
    if fileExist():
        print("File Name already exist")
        return filename
    else:
        create = open(filename, "w")
        title = input("Enter the heading of your file: ")
        create.write(title + "\n")
        create.close()
        print("File \"", filename_, "\" created Successfully!\n")
        


_choice = choice()

def operation(): #Declare 'filename', 'file_Status' as global
    if _choice == open_File:
        print("OPENNING A FILE")
        flag = 0
        fileName(flag)
        print("File ", filename_, " opened")
        action()

    elif _choice == create_File:
        print("CREATING A FILE")
        flag = "create"
        fileName(flag)
        file_Status()
        action()

    elif _choice == delete_File:
        print("DELETING A FILE")
        flag = "delete"
        fileName(flag)
        if fileExist():
            os.remove(filename)
            print("File deleted successfully\n")
            chioce()
        else:
            print("Oops! The file does not even exist.\n")
            choice()
            
    else:
        quit()




while True:
    operation()
