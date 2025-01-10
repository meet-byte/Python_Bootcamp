# import csv
# from Expense_management import Expense
# print("Welcome to the expense management application")
# def checkuser(user):

#     with open("user.csv",mode="r",newline="") as file:
#         reader=csv.reader(file)
#         flag=0
#         for line in reader:
#             if user in line[0]:
#                 flag=1
#                 filename=f"{user}.csv"
#                 return filename
                
#         if flag==0:
#             return False

# def createuser(user):
#     with open("user.csv",mode="a",newline="") as file:
#             writer=csv.writer(file)
#             data=[user]
#             writer.writerow(data)
#             checkuser(user)

# inp=int(input('''
#         1. enter 1 to add the Expense 
#         2. enter 2 to read the expense
#         3. enter 3 to calculate the total expense
#         4. enter 4 to create a new user
#       '''))
# name=input("enter the name of the expense: ")
# amount=input("enter the amount of the expense: ")
# type=input("enter the type of the expense: ")
# mode=input("enter the mode of the transaction: ")
# obj=Expense(name,amount,type,mode)
# username=input("enter the name of the user: ")
# filename=checkuser(username)
# if filename==False:
#     filename=createuser(username)
# if inp==1:
#     obj.addexpense(name,amount,type,mode,filename)
# if inp==2:
#     obj.readexpense(filename)
# if inp==3:
#     obj.calexpe(filename)
# if inp==4:
#     obj.createuser()
# if inp==5:
#     date1=input("enter the first date")
#     date2=input("enter the second date")
#     obj.diffbtdate(filename,date1,date2)
# month=(input("enter the month eg.01::::"))
# year=(input("enter the year eg.2025::::"))
# str=year+"-"+month
# obj.betmnnyr(str,"temp1.csv")

import csv
from Expense_management import Expense

# Function to check if a user exists and return the corresponding file name
def check_user(user):
    with open("user.csv", mode="r", newline="") as file:
        reader = csv.reader(file)
        for line in reader:
            if user in line[0]:  # Check if user exists
                return f"{user}.csv"
    return False

# Function to create a new user and save to "user.csv"
def create_user(user):
    with open("user.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([user])  # Save new user
    return check_user(user)

# Main program function
def main():
    print("Welcome to the Expense Management Application")

    # User input for action choice
    inp = int(input(''' 
        1. Enter 1 to add an expense
        2. Enter 2 to read the expense
        3. Enter 3 to calculate the total expense
        4. Enter 4 to create a new user
        5. Enter 5 to calculate expenses between two dates
        6. Enter 6 to calculate expenses for a specific month and year
    '''))

    
    
    # Creating an Expense object
    expense_obj = Expense()

    # Getting user name and checking if they exist
    username = input("Enter the name of the user: ")
    filename = check_user(username)

    if not filename:  # If user does not exist, create a new user
        filename = create_user(username)

    # Based on the input choice, perform the corresponding action
    if inp == 1:
        # Getting expense details from the user
        name = input("Enter the name of the expense: ")
        amount = input("Enter the amount of the expense: ")
        type = input("Enter the type of the expense: ")
        mode = input("Enter the mode of the transaction: ")
        expense_obj.add_expense(name, amount, type, mode, filename)
    elif inp == 2:
        expense_obj.read_expenses(filename)
    elif inp == 3:
        expense_obj.calculate_expenses(filename)
    elif inp == 4:
        expense_obj.create_user(username)
    elif inp == 5:
        # Input date range for filtering expenses
        date1 = input("Enter the first date (YYYY-MM-DD): ")
        date2 = input("Enter the second date (YYYY-MM-DD): ")
        expense_obj.expenses_between_dates(filename, date1, date2)
    elif inp == 6:
        # Input month and year for filtering monthly expenses
        month = input("Enter the month (MM): ")
        year = input("Enter the year (YYYY): ")
        month_year_str = f"{year}-{month}"
        expense_obj.expenses_in_month(month_year_str, filename)

# Run the main function
if __name__ == "__main__":
    main()
