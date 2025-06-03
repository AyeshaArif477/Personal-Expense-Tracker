import json
from datetime import datetime

DATA_FILE = "expenses.json"

def load_expenses():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)

def add_expense(expenses):
    amount = float(input("Enter amount: "))
    category = input("Enter category (e.g., food, transport): ")
    date_str = input("Enter date (YYYY-MM-DD) or leave empty for today: ")
    if not date_str:
        date_str = datetime.now().strftime("%Y-%m-%d")

    expense = {
        "amount": amount,
        "category": category,
        "date": date_str
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added!")

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    total = 0
    print("All Expenses:")
    for exp in expenses:
        print(f"{exp['date']} - {exp['category']}: ${exp['amount']:.2f}")
        total += exp['amount']

    print(f"\nTotal Expenses: ${total:.2f}")

def main():
    expenses = load_expenses()
    while True:
        print("\nOptions:")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
