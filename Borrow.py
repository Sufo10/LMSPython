############## module for borrow operation ###################

import functions

#function to borrow books
def borrow_book():
    flag = False
    
    while True:
        first_name = input("Enter borrower's first name: ")
        if first_name.isalpha():
            break
        print("Please give a proper name.")
    while True:
        last_name = input("Enter borrower's last name: ")
        if last_name.isalpha():
            break
        print("Please give a proper name.")
            
    file_create = "Borrow-"+first_name+".txt"

    #code to give heading and write borrower name, date and time of borrow
    with open(file_create, "w+") as file:
        file.write("\tLibrary Management System  \n")
        file.write("\tBorrowed By: "+ first_name+" "+last_name+"\n")
        file.write("    Date: " + functions.showDate()+"    Time: "+ functions.showTime()+"\n\n")
        file.write("S.N. \t\t Book name \t      Author name \t\t Price\n" )

    
    while flag == False:
        print("Please select a option below:")
        for i in range(len(functions.book_name)):
            print("Enter", i, "to borrow book", functions.book_name[i])
        try:   
            a=int(input("Enter:"))
            try:
                if(int(functions.quantity[a]) > 0):
                    print("Book is available.")
                    
                    #code to write the borrowed information in the borrownote
                    with open(file_create, "a") as file:
                        file.write("1. \t\t"+ functions.book_name[a]+"\t\t  "+functions.author_name[a]+"\t\t $"+functions.cost[a]+"\n")
        
                    functions.quantity[a] = int(functions.quantity[a]) - 1
                    
                    #code to update inventory text file
                    with open("stock.txt","w+") as file:
                        for i in range(10):
                            file.write(functions.book_name[i]+","+functions.author_name[i]+","+str(functions.quantity[i])+","+"$"+functions.cost[i]+"\n")
                            
                    #code to borrow multiple books 
                    loop = True
                    count = 1
                    while loop == True:
                        choice = str(input("Do you want to borrow more books? However you cannot borrow same book twice. Press y for yes and n for no.")).lower()
                        if(choice == "y"):
                            count = count + 1
                            print("Please select an option below:")
                            for i in range(len(functions.book_name)):
                                print("Enter", i, "to borrow book", functions.book_name[i])
                                
                            a = int(input("Enter: "))
                            if(int(functions.quantity[a]) > 0):
                                print("Book is available.")

                                #code to write the borrowed information in the borrownote
                                with open(file_create, "a") as file:
                                    file.write(str(count) + ". \t\t"+ functions.book_name[a]+"\t\t  "+functions.author_name[a]+"\t\t $"+functions.cost[a]+"\n")

                                functions.quantity[a] = int(functions.quantity[a]) - 1

                                #code to update inventory text file
                                with open("stock.txt","w+") as file:
                                    for i in range(10):
                                        file.write(functions.book_name[i]+","+functions.author_name[i]+","+str(functions.quantity[i])+","+"$"+functions.cost[i]+"\n")
                            else:
                                loop = False
                                break
                        elif (choice == "n"):
                            print("")
                            print ("Thank you for borrowing books from us. ")
                            loop = False
                            flag = True
                        else:
                            print("Please choose as instructed.")
                            
                else:
                    print("Book is not available.")
                    borrow_book()
                    flag = False

                #code to calculate the total amount to be paid to borrow   
                total = 0.0    
                with open(file_create,"r") as file:
                    data=file.read()
                    
                for i in range(10):    
                    if functions.book_name[i] in data:
                            total += float(functions.cost[i])

                #writing total amount in the borrownote          
                with open(file_create, "a") as file:
                    file.write("\n")
                    file.write("Total borrow cost: $"+ str(total))
                
            except IndexError:
                print("")
                print("Please choose book according to their number.")
                
        except ValueError:
            print("")
            print("Please choose as suggested.")
       
