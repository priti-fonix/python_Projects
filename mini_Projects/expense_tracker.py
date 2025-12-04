# expense tracker
expenses=[]
print("-------Expense tracker-----")
while True :
    print("--Welcome to the expense tracker----")
    print("1. enter the expenses")
    print("2. view the expenses")
    print("3. View total spending")
    print("4. Exit")

    choice = int(input("enter the choice according to the above options: "))

    if(choice == 1):
        date= input("enter the date : ")
        category = input("enter the category (travel,stationary,rent,etc) : ")
        description = input("enter the description : ")
        amount = float(input("enter total expenses : "))

        expense = {
            "date" : date,
            "category" : category,
            "description" : description,
            "amount" : amount
             
        }
        expenses.append(expense)
        print("\n expenses added successfully.")
    
    #2 VIEW ALL EXPENSES
    elif(choice == 2):
        if(len(expenses) == 0):
            print("No spendings done yet ")
        else:
            print("here is the expenses you have done")
            count = 1
            for eachspending in expenses:
                    print(f"spendings are {count} ->  {eachspending["date"]}, {eachspending["category"]},{eachspending["description"]}, {eachspending["amount"]}")

            count +=1
    #3 VIEW TOTAL EXPENSES

    elif(choice == 3):
        print("here is the total spending")
        total = 0
        for eachspend in expenses:
          total += eachspend["amount"]
        

        print(" Total Kharcha :- " ,total)

    #4 -----EXIT-----
    elif(choice == 4):
        print("THANKS FOR USING THIS APP")
    else:
        print("you successfully existed")
        
