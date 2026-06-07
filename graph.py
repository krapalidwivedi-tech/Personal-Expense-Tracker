import pandas as pd
import matplotlib.pyplot as plt

from database import connect_db

def expense_pie_chart():
    conn = connect_db()
    df = pd.read_sql_query("SELECT*FROM expenses",conn)
    
    data = df.groupby("category")["amount"].sum()
    data.plot(kind = "pie",autopct = "%1.1f%%")
    plt.title("Expense Distribution")
    plt.show()
    
    conn.close()