'''
===== Your Expense Records =====
No expenses on record yet.

How many expenses would you like to log? 2

---Expense 1 ---
Description: Rent
Amount: 1500
Category: Necessities

---Expense 2 ---
Description: Wal-Mart
Amount: 184.57
Category: Food

===== Your Expense Records =====
Date        Description                   Amount    Category    
----------------------------------------------------------------------
2026-09-19  Rent                          1500.00   Necessities 
2026-09-19  Wal-Mart                      184.57    Food        '''
#PS C:\Users\nicpa\AppData\Local\Programs\Microsoft VS Code> & C:\Users\nicpa\AppData\Local\Programs\Python\Python314\python.exe c:/Users/nicpa/Lewis/Fall26/Programming/Week-4-Assignment/paugys_personal_expense_tracker.py
'''
===== Your Expense Records =====
Date        Description                   Amount    Category    
----------------------------------------------------------------------
2026-09-19  Rent                          1500.00   Necessities 
2026-09-19  Wal-Mart                      184.57    Food        

How many expenses would you like to log? 1

---Expense 1 ---
Description: Grocery shopping in preparation for Thanksgiving
Amount: 320.43
Category: Food

===== Your Expense Records =====
Date        Description                   Amount    Category    
----------------------------------------------------------------------
2026-09-19  Rent                          1500.00   Necessities 
2026-09-19  Wal-Mart                      184.57    Food        
2026-09-19  Grocery shopping in preparatio320.43    Food        '''
#PS C:\Users\nicpa\AppData\Local\Programs\Microsoft VS Code> & C:\Users\nicpa\AppData\Local\Programs\Python\Python314\python.exe c:/Users/nicpa/Lewis/Fall26/Programming/Week-4-Assignment/paugys_personal_expense_tracker.py
'''
===== Your Expense Records =====
Date        Description                   Amount    Category    
----------------------------------------------------------------------
2026-09-19  Rent                          1500.00   Necessities 
2026-09-19  Wal-Mart                      184.57    Food        
2026-09-19  Grocery shopping in preparatio320.43    Food        

How many expenses would you like to log? 0

===== Your Expense Records =====
Date        Description                   Amount    Category    
----------------------------------------------------------------------
2026-09-19  Rent                          1500.00   Necessities 
2026-09-19  Wal-Mart                      184.57    Food        
2026-09-19  Grocery shopping in preparatio320.43    Food   '''

import os
import datetime

#formats user input and returns a string of the record to be written to the file
def build_records(description, amount, category):
    cost = float(f"{amount:.2f}")
    explanation = description[:30]
    date = str(datetime.date.today())
    all_data = [date, explanation, str(cost), category]
    return ",".join(all_data)

#takes file as input and returns list of records, each record is a list of values
def load_records(filename):
    records = []
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if line == "":
                    continue
                record = line.split(",")
                records.append(record)
    except FileNotFoundError:
        return []
    return records

#Take text file input and display records in a table by indexing through the list that reading through the file creates
def display_records(records):
    print("\n===== Your Expense Records =====")
    if not records:
        print("No expenses on record yet.")
        return
    print(f"{'Date':<12}{'Description':<30}{'Amount':<10}{'Category':<12}")
    print("-" * 70)
    for record in records:
        money = "{:.2f}".format(float(record[2]))
        print(f"{record[0]:<12}{record[1]:<30}{money:<10}{record[3]:<12}")
   

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    if os.path.isdir("expenses.txt"):
        raise SystemExit("Error: 'expenses.txt' is a folder, not a file. Rename or delete it and run again.")
    if os.path.exists("expenses.txt") and not os.access("expenses.txt", os.R_OK | os.W_OK):
        raise SystemExit("Error: no permission to read/write 'expenses.txt'.")
    if not os.path.exists("expenses.txt") and not os.access(".", os.W_OK):
        raise SystemExit("Error: can't create 'expenses.txt' in this folder (no write permission).")

    current_records = load_records("expenses.txt")
    display_records(current_records)
 
    try: 
        num_expenses = int(input("\nHow many expenses would you like to log? "))
    except ValueError:
        num_expenses = 0
 
    for i in range(num_expenses):
        print(f"\n---Expense {i + 1} ---")  
        description = input("Description: " )
        amount = float(input("Amount: "))
        category = input("Category: ")
 
        record = build_records(description, amount, category)
        with open("expenses.txt", "a") as file:
            file.write(record + "\n")

    current_records = load_records("expenses.txt")
    display_records(current_records)