# import csv
# from datetime import datetime
# import os
# class Expense:
#     def __init__(self,exp_name,amount,type,Transactionmode):
#         self.exp_name=exp_name
#         self.amount=amount
#         self.type=type
#         self.Transactionmode=Transactionmode
#         self.date=datetime.now()
#     def addexpense(self,exp_name,amount,type,Transactionmode,filename):
#         path_file=os.path.exists(filename)
#         if not path_file:
#             with open(filename,mode="x",newline="") as fs:
#                 fieldnames = ["Exp_name", "amount", "Type","Transactionmode","date"]
#                 writer = csv.DictWriter(fs, fieldnames=fieldnames)
#                 writer.writeheader()

#         ##data=Expense(exp_name,amount,type,Transactionmode)
       
#         date=date.now()
#         with open(filename,mode="a",newline="") as file:
#             writer=csv.writer(file)
#             data1=[exp_name,amount,type,Transactionmode,date]
#             writer.writerow(data1)

#     def readexpense(self,filename):
#         with open(filename,mode="r",newline="") as file:

#             reader=csv.reader(file)
#             for read in reader:
#                 print(read)
#                 print("------------------------------------------------------------------------------------------------")
#     def calexpe(self,filename):
#         sum=0
#         with open(filename,mode="r",newline="")as file:
#             reader=csv.reader(file)
#             for read in reader:
#                 sum+=int(read[1])
#             print(f"Total mentioned Expense till now is:- {sum}")
#     def diffbtdate(self,filename,date1,date2):
#         with open(filename,mode="r",newline="") as file:
#             reader=csv.reader(file)
#             sum=0
#             for read in reader:
#                 if read[4]>=date1 and read[4]<=date2:
#                     print(read[4])
#                     sum+=int(read[1])
#             print(f"sum between two date is:- {sum}")
#     def betmnnyr(self,str,filename):
#         with open(filename,mode="r",newline="") as file:
#             reader=csv.reader(file)
#             sum=0
#             for read in reader:
#                 if read[4][0:7]==str:
#                     sum+=int(read[1])
#         print(f"The Total Expense of given Month of the year is :{sum}")

# # e=Expense("panipuri1","300","Regular","Cashie")

# # e.addexpense("panipuri","200","Regular","Cash","temp1.csv")
# # e.addexpense("panipuri1","300","Regular","Cash","temp1.csv")

# # e.readexpense("temp1.csv")

import csv
from datetime import datetime
import os

class Expense:
    def __init__(self):
        
        pass
    def add_expense(self, exp_name, amount, type, transaction_mode, filename):
        """
        Adds an expense entry to the CSV file, creating a new file if it doesn't exist.
        """
        path_file = os.path.exists(filename)
        
        if not path_file:
            # Create a new file and write the header if the file doesn't exist.
            with open(filename, mode="x", newline="") as fs:
                fieldnames = ["Exp_name", "Amount", "Type", "Transaction_mode", "Date"]
                writer = csv.DictWriter(fs, fieldnames=fieldnames)
                writer.writeheader()

        # Get the current date and time for the entry
        date = datetime.now()

        # Write the new expense data into the file
        with open(filename, mode="a", newline="") as file:
            writer = csv.writer(file)
            data = [exp_name, amount, type, transaction_mode, date]
            writer.writerow(data)

    def read_expenses(self, filename):
        """
        Reads and prints all expenses from the CSV file.
        """
        with open(filename, mode="r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
                print("-" * 100)

    def calculate_expenses(self, filename):
        """
        Calculates and prints the total amount of all expenses recorded in the CSV file.
        """
        total_expense = 0
        with open(filename, mode="r", newline="") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                total_expense += int(row[1])
        print(f"Total expenses recorded: {total_expense}")

    def expenses_between_dates(self, filename, date1, date2):
        """
        Calculates and prints the total expenses between two given dates.
        """
        total_expense = 0
        with open(filename, mode="r", newline="") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                expense_date = datetime.strptime(row[4], "%Y-%m-%d %H:%M:%S.%f")
                if date1 <= expense_date <= date2:
                    print(row[4])  # Print the date of each matching expense
                    total_expense += int(row[1])
        print(f"Total expenses between {date1} and {date2}: {total_expense}")

    def expenses_in_month(self, month_str, filename):
        """
        Calculates and prints the total expenses for a given month of the year.
        """
        total_expense = 0
        with open(filename, mode="r", newline="") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                if row[4][:7] == month_str:  # Check the first 7 characters (YYYY-MM) for month match
                    total_expense += int(row[1])
        print(f"Total expenses in {month_str}: {total_expense}")
