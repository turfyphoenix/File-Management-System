from pathlib import Path
import os
def createfile():
    try:
        filename = input("Enter the filename: ")
        path  = Path(filename)
        if not path.exists():
            with open(filename, "w") as fs:
                data = input("Enter the data to be written in the file")
                fs.write(data)
        else:
            print("File already exists")
    except Exception as err:
        print(f"An error has occured {err}")

def readfile():
    try:
        filename = input("Enter the filename: ")
        path = Path(filename)
        if path.exists():
            with open (filename,"r") as fs:
                content = fs.read()
                print(f"Your content is \n {content}")
        else:
            print("No such file exists")
    except Exception as err:
        print(f"An error has occured {err}")

def updatefile():
    try:
        filename = input("Name the file to update ")
        path = Path(filename)

        if path.exists():
            print("To Rename the file press 1:")
            print("To Append the file press 2:")
            print("To Overwrite the file press 3:")
            choice2 = int(input("Enter the choice"))
            if choice2 == 1:
                newname = input("Enter the New File Name: ")
                new_path = Path(newname)
                if not new_path.exists():
                    path.rename(new_path)
                    print("Renamed Successfuly")
                else:
                    print("The File already exists")
            elif choice2 == 2:
                with open(filename, "a") as fs:
                    data = input("Enter the data to be appended: ")
                    fs.write("\n"+ data)
                print("Success")
            elif choice2 == 3:
                with open(filename, "w") as fs:
                    data = input("Enter the data to be appended: ")
                    fs.write("\n"+data)
                print("Success")
    except Exception as err:
        print(f"An error has occured {err}")



def deletefile():
    try:
        filename = input("Enter the filename: ")
        path =  Path(filename)
        if path.exists():
            path.unlink()
            print("Success")
        else:
            print("No such file")
    except Exception as err:
        print(f"An error has occured {err}")

def exitfile():
    return

while True:
    print("\n===== FILE MANAGEMENT SYSTEM =====")
    print("1. Create a file")
    print("2. Read a file")
    print("3. Update a file")
    print("4. Delete a file")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        createfile()

    elif choice == "2":
        readfile()

    elif choice == "3":
        updatefile()

    elif choice == "4":
        deletefile()

    elif choice == "5":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 5.")
