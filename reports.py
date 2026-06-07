import pandas as pd
from database import connect_db

def total_expense():
    conn = connect_db()
    df = pd.read_sql_query("SELECT*FROM expenses",conn)
    total = df["amount"].sum()
    
    print("Total Expense",total)
    
    conn.close()
    
    
def category_report():
    conn = connect_db()
    df = pd.read_sql_query("SELECT*FROM expenses",conn)
    report = df.groupby("category")["amount"].sum()
    print(report)
    
    conn.close()
    
    