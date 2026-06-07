from database import create_table

from operations import(
    add_expense,
    view_expense,
    delete_all_expenses
)

from reports import(
    total_expense,
    category_report
)

from graph import(
    expense_pie_chart
)


create_table()

while True:
    print("\n====EXPENSE TRACKER====")
    
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Category Report")
    print("5. Pie Chart")
    print("6.Delete Expense")
    print("7. Exit")
    
    choice = input("Enter Choice: ")

    if choice == "1":
        add_expense()
        print("\n✔ Expense Added Successfully!")

    elif choice == "2":
        print("\n===== ALL EXPENSES =====")
        view_expense()

    elif choice == "3":
        print("\n===== TOTAL EXPENSE =====")
        total_expense()

    elif choice == "4":
        print("\n===== CATEGORY REPORT =====")
        category_report()

    elif choice == "5":
        print("\nOpening Chart...")
        expense_pie_chart()
        
    elif choice == "6":
        print("Delete All Expenses")
        delete_all_expenses()

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice! Try again.")