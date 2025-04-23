import csv
from datetime import datetime
from collections import defaultdict

FILENAME = "expenses.csv"

def add_expense():
    date = input("Enter date (YYYY-MM-DD) [Leave empty for today]: ")
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')
    amount = input("Enter amount: ")
    category = input("Enter category (e.g., food, travel, bills): ")
    notes = input("Add notes (optional): ")

    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, notes])
    
    print("✅ Expense added!\n")

def view_expenses():
    try:
        with open(FILENAME, mode='r') as file:
            reader = csv.reader(file)
            print("\n📋 All Expenses:\n")
            print(f"{'Date':<12} {'Amount':<10} {'Category':<15} Notes")
            print("-" * 50)
            for row in reader:
                print(f"{row[0]:<12} ₹{row[1]:<10} {row[2]:<15} {row[3]}")
            print()
    except FileNotFoundError:
        print("❌ No expenses recorded yet.\n")

def summary_report():
    try:
        category_totals = defaultdict(float)
        total = 0
        with open(FILENAME, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                amount = float(row[1])
                category = row[2]
                category_totals[category] += amount
                total += amount

        print("\n📊 Summary Report:")
        print("-" * 30)
        for category, amount in category_totals.items():
            print(f"{category:<15}: ₹{amount:.2f}")
        print("-" * 30)
        print(f"{'Total':<15}: ₹{total:.2f}\n")
    except FileNotFoundError:
        print("❌ No data found for summary.\n")

def main():
    print("🧾 Welcome to Python Expense Tracker!")
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Summary Report")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")
        print()

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            summary_report()
        elif choice == '4':
            print("👋 Exiting... Stay on budget!")
            break
        else:
            print("⚠️ Invalid option. Try again.\n")

if __name__ == "__main__":
    main()
