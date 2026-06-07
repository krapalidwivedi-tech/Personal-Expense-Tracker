from database import connect_db
def add_expense():          
    conn = connect_db()
    cursor = conn.cursor()
     
    date = input("Date(YYYY-MM-DD):")
    category = input("category:")
    amount = float(input("Enter amount:"))
    description = input("Description:")
    
    cursor.execute("""INSERT INTO expenses(date,category,amount,description)VALUES(?,?,?,?)""",(date,category,amount,description))
    
    conn.commit()
    conn.close()
    
def view_expense():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT*FROM expenses")
    expenses = cursor.fetchall()
    
    for expense in expenses:
        print(f"ID:{expense[0]}|"
              f"Dtae:{expense[1]}|"
              f"Category:{expense[2]}|"
              f"Amount:{expense[3]}|"
              f"Description:{expense[4]}"
              )
        
    conn.close()
    
def delete_all_expenses():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM expenses")

    conn.commit()
    conn.close()

    print("✔ All previous expenses deleted!")