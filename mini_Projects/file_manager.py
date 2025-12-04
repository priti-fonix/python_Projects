import os

def create_file(filename):

    try:
        with open(filename,'x') as f:
            print(f"{filename} has been created")
    except FileExistsError:
        print(f"file already exist")
    except Exception as e:
        print("An error occured")

def view_files():
    files = os.listdir()
    if not files:
        print("no files found")
    else:
        print("files in directory are :\n ")
        for file in files:
            print(file)
       
def delete_file(filename):
    try:
      os.remove(filename)
      print(f"file {filename} deleted successfully")
    except FileNotFoundError:
        print("file not found")
    except Exception as e:
        print("an error occured")

def read_file(filename):
    try:
      with open(filename,'r') as f:
        content = f.read()
        print(f"content of file {filename} are:\n{content}")
    except FileNotFoundError:
        print("file not found")
    except Exception :
        print("an error occured")

def edit_file(filename):
    try:
      with open(filename,'a') as f:
        content = input("enter data to be edited =")
        f.write(content +"\n")
        print(f"content edited of file {filename} successfully \n")
    except FileNotFoundError:
        print("file not found")
    except Exception :
        print("an error occured")
        

def main():
    while True:

        print("--------------FILE MANAGEMENT APP----------")

        print("1.create file")
        print("2.read file")
        print("3.edit file")
        print("4.delete file")
        print("5.view file")
        print("6.exit ")

        choice = input("enter your choice(1-6)=")

        if choice == "1":
            filename = input("enter file name to be created: ")
            create_file(filename)
        elif choice == "2":
            filename = input("enter file name to be read: ")
            read_file(filename)
        
        elif choice == "3":
            filename = input("enter file name to be edited: ")
            edit_file(filename)
        elif choice == "4":
            filename = input("enter file name to be deleted: ")
            delete_file(filename)

        elif choice == "5":
            view_files()
        elif choice == "6":
            print("You exited successfully")
            break
        else:
            print("Invalid choice. Please enter 1-6.")
            

        

if __name__ == "__main__":
    main()


    