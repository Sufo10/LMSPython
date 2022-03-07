import datetime

#function to read the inventory file and print it
def read_file():
    with open("stock.txt","r") as file:
        print(file.read())

#function to read the inventory file and print in a styled manner
def show_details():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("===========================Library Management System==============================================")
    print("BookID.         Book Name                   Author             No Of Books       Price")
    print("--------------------------------------------------------------------------------------------------")
    with open("stock.txt","r") as file:
        book_id = 1
        for line in file:
            print(" ",book_id,"\t\t"+line.replace("," , "\t\t"))
            book_id = book_id + 1
    print("---------------------------------------------------------------------------------------------------")

#function to create list for book name, author name, cost and price
def list_creation():
    global book_name
    global author_name
    global quantity
    global cost
    book_name = []
    author_name = []
    quantity = []
    cost = []
    with open("stock.txt","r") as file:  
        lines = file.readlines()
        lines = [x.strip('\n') for x in lines]
        for i in range(len(lines)):
            num = 0
            for a in lines[i].split(','):
                if(num == 0):
                    book_name.append(a)
                elif(num == 1):
                    author_name.append(a)
                elif(num == 2):
                    quantity.append(a)
                elif(num == 3):
                    cost.append(a.strip("$"))
                num += 1

#function to show date
def showDate():
    now = datetime.datetime.now
    return str(now().date())

#function to show time
def showTime():
    now = datetime.datetime.now
    return str(now().time())


    
