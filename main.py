import sqlite3 
import datetime

conn = sqlite3.connect("expenses.sqlite")
cur = conn.cursor()

#function to add a user
def select_user_by_username(username):
    cur.execute("SELECT user_id FROM users WHERE username = ?", (username,))
    user = cur.fetchone()
    if user:
        return user[0]
    else:
        print(f"No user found with the username '{username}'")
        return None

def select_budgets(user_id):
    cur.execute("SELECT category, amount FROM budgets WHERE user_id = ?", (user_id,))
    budgets = cur.fetchall()
    if budgets:
        print(f"Budgets for user {user_id}:")
        for budget in budgets:
            print(f"Category: {budget[0]}, Amount: {budget[1]}")
    else:
        print("No budgets found.")

def select_expenses(user_id):
    cur.execute("SELECT date, description, category, amount FROM expenses WHERE user_id = ?", (user_id,))
    expenses = cur.fetchall()
    if expenses:
        print(f"Expenses for user {user_id}:")
        for expense in expenses:
            print(f"Date: {expense[0]}, Description: {expense[1]}, Category: {expense[2]}, Amount: {expense[3]}")
    else:
        print("No expenses found.")

def select_total_expenses(user_id):
    cur.execute("SELECT SUM(amount) FROM expenses WHERE user_id = ?", (user_id,))
    total_expenses = cur.fetchone()[0]
    if total_expenses:
        print(f"Total expenses for user {user_id}: {total_expenses}")
    else:
        print("No expenses recorded.")

def select_budget_by_category(user_id, category):
    cur.execute("SELECT amount FROM budgets WHERE user_id = ? AND category = ?", (user_id, category))
    budget = cur.fetchone()
    if budget:
        return budget[0]
    else:
        print(f"No budget found for category '{category}'")
        return None

def main():
    while True:
        print("\nSelect an option:")
        print("1. Select user by username")
        print("2. View budgets")
        print("3. View expenses")
        print("4. View total expenses")
        print("5. View budget for a specific category")
        print("6. Exit")

        choice = int(input())

        if choice == 1:
            username = input("Enter your username: ")
            user_id = select_user_by_username(username)
        elif choice == 2:
            username = input("Enter your username: ")
            user_id = select_user_by_username(username)
            if user_id:
                select_budgets(user_id)
        elif choice == 3:
            username = input("Enter your username: ")
            user_id = select_user_by_username(username)
            if user_id:
                select_expenses(user_id)
        elif choice == 4:
            username = input("Enter your username: ")
            user_id = select_user_by_username(username)
            if user_id:
                select_total_expenses(user_id)
        elif choice == 5:
            username = input("Enter your username: ")
            user_id = select_user_by_username(username)
            if user_id:
                category = input("Enter the category: ")
                budget = select_budget_by_category(user_id, category)
                if budget:
                    print(f"Budget for {category}: {budget}")
        elif choice == 6:
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

# Close the connection when done
conn.close()

