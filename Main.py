#main module run for working of the library system

import Return
import functions
import Borrow

functions.show_details()
functions.read_file()
print("")
print("")

#function to display a user-friendly library system
def start_menu():
    running = True
    while running:
        print("Enter 1. To borrow a book")
        print("Enter 2. To return a book")
        print("Enter 3. To exit")
        print("")
        try:
            x = int(input("Select a choice from 1-3: "))
            print("")
            if(x == 1):
                functions.list_creation()
                Borrow.borrow_book()
            elif(x == 2):
                functions.list_creation()
                Return.return_book()
            elif(x == 3):
                print("Thank you for using library management system. Come visit again.")
                break
            else:
                print("Please enter a valid choice from 1-3.")
        except ValueError:
            print("Please input as suggested.")
start_menu()
