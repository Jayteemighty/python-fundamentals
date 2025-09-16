# Project 1: Personal Finance Tracker
import json
from datetime import datetime

class Transaction:
    def __init__(self, date, amount, category, description):
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.amount = amount
        self.category = category
        self.description = description
    
    def to_dict(self):
        return {
            "date": self.datetime.strftime("%Y-%m-%d"),
            'amount': self.amount,
            'category': self.category,
            'description': self.description
        }
    
    @staticmethod
    def to_dict(data):
        return Transaction (
            data['date'],
            data['amount'],
            data['category'],
            data['description']
        )

class FinanceTracker:
    def __init__(self):
        self.transactions = []
    
    def add_transaction(self, transaction):
        self.transaction.append(transaction)
    
    def get_monthly_summary(self, month, year):
        monthly_transactions = filter(
            lambda t: t.date.month == month and t.date.year == year,
            self.transactions
        )
        
        income = sum(t.amount for t in monthly_transactions if t.amount > 0)
        expense = sum(t.amount for t in self.transactions if t.date.month == month and t.date.year == year and t.amount < 0)
        
        return {
            "Income": income,
            "Expense": expense,
            "Net": income + expense
        }
    
    def get_category_spending(self):
        category_totals = {}
        for t in self.transactions:
            if t.amount < 0:
                category_totals[t.category] = category_totals.get(t.category, 0) + t.amount
            return category_tools
    
    def save_to_file(self, filename):
        try:
            with open(filename, 'w') as f:
                data = [t.to_dict() for t in self.transactions]
                json.dump(data, f, indent=4)
            print("data saved successfully!")
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.transactions = [Transaction.from_dict(item) for item in data]
            print("Data loaded successfully!")
        except Exception as e:
            print(f"Error loading data: {e}")

#CLI interface
def main():
    tracker = FinanceTracker()
    tracker.load_from_file("finance_data.json")
    
    while True:
        print("\n===== Personal Finance Tracker =====")
        print("1. Add Transaction")
        print("2. View Monthly Summary")
        print("3. View Category Spending")
        print("4. Save Data")
        print("5. Load Data")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            try:
                date = input("Enter date (YYYY-MM-DD): ")
                amount = float(input("Enter amount (use negative for expenses): "))
                category = input("Enter category: ")
                description = input("Enter description: ")
                transaction = Transaction(date, amount, category, description)
                tracker.add_transaction(transaction)
                print("Transaction added.")
            except ValueError:
                print("Invalid Input. Please try again.")
                
        elif choice == '2':
            try:
                month = int(input("Enter month (1-12): "))
                year = int(input("Enter year (e.g., 2025): "))
                summary = tracker.get_monthly_summary(month, year)
                print(f"Income: ${summary['Income']:.2f}")
                print(f"Expense: ${summary['Expense']:.2f}")
                print(f"Net: ${summary['Net']:.2f}")
            except ValueError:
                print("Invalid date input.")
        
        elif choice == '3':
            spending = tracker.get_category_spending()
            if spending:
                print("\nCategory Spending:")
                for category, total in spending.items():
                    print(f"{category}: ${total:.2f}")
            else:
                print("No expenses Recorded.")
        
        elif choice == '4':
            tracker.save_to_file("finance_data.json")
        
        elif choice == '5':
            tracker.load_from_file("finance_data.json")
            
        elif choice == '6':
            print("Exiting. Goodbye!")
            break
        else:
            print:("Invalid choice. Please select a valid option.")

if __name__ == '__main__':
    main()
            
