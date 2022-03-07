################################## module for return operation ########################################

import functions

#function to return books
def return_book():
    
    name=input("Enter first name of borrower: ")
    borrow_file = "Borrow-"+name+".txt"

    #code to read borrow file and print it if available 
    try:
        with open(borrow_file,"r") as file:
            lines = file.readlines()
            lines = [a.strip("$") for a in lines]
    
        with open(borrow_file,"r") as file:
            data = file.read()
            print(data)
    except:
        print("The borrower name is incorrect.")
        return_book()

    #code to write heading, name of book returner, date and time of return
    file_create = "Return-"+name+".txt"
    with open(file_create,"w+")as file:
        file.write("\t\tLibrary Management System \n")
        file.write("\t\tReturned By: "+ name+"\n")
        file.write("    Date: " + functions.showDate()+"    Time: "+ functions.showTime()+"\n\n")
        file.write("S.N.\t\tbook_name\t\tCost\n")

    
    for i in range(10):    
        if functions.book_name[i] in data:
            with open(file_create, "a") as file:
                file.write(str(i+1)+"\t\t"+functions.book_name[i]+"\t\t$"+functions.cost[i]+"\n")
                
            functions.quantity[i] = int(functions.quantity[i])+ 1
    print("")
    print("The lending duration is 10 days.")
    print("Is the number of days the book was kept greater than 10?")
    choice = input("Press y for Yes and n for No: ").lower()

    #code to calculate file if the number of days book was kept > 10
    total = 0.0
    if(choice == "y"):
        lend_duration = 10
        print("")
        day = int(input("How many days was the book kept with the owner ?"))
        
        if day > lend_duration:
            fine = 2 * (day - lend_duration)
            
            with open(file_create, "a")as file:
                file.write("\n")
                file.write("The lending duration is 10 days. \n")
                file.write("Fine per day: $2 \n")
                file.write("So,fine for "+str(day - lend_duration)+" days late: $"+ str(fine)+"\n")
            total = total + fine
            print("")
            print("So, you will be charged fine at the rate of $2 per day after that.")
            print("Total fine to be paid: "+ "$"+str(total))
            print("")
                
    else:
        print("Thank you for returning the book in time.")
    
    with open(file_create, "a")as file:
        file.write("\n")
        file.write("Final Total amount to be paid: $"+ str(total))

    #code to update inventory text file
    with open("stock.txt","w+") as file:
        for i in range(10):
            file.write(functions.book_name[i]+","+functions.author_name[i]+","+str(functions.quantity[i])+","+"$"+functions.cost[i]+"\n")
