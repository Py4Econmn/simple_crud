
# pip install tk
# pip install sqlalchemy
# pip install psycopg2-binary
# pip install pyinstaller
# pyinstaller --onefile main.py




import tkinter as tk
from tkinter import ttk
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database setup
engine = create_engine('postgresql://postgres:postgres@localhost/postgres')
Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    salary = Column(Integer)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# GUI setup
root = tk.Tk()
root.title("Employee Database")

# Function to add employee to the database
def add_employee():
    session = Session()
    new_employee = Employee(name=name_entry.get(), salary=int(salary_entry.get()))
    session.add(new_employee)
    session.commit()
    session.close()
    display_records()

# Function to display employee records in the table
def display_records():
    session = Session()
    employees = session.query(Employee).all()
    session.close()

    for i in tree.get_children():
        tree.delete(i)
    
    for employee in employees:
        tree.insert("", "end", values=(employee.id, employee.name, employee.salary))

# Create GUI elements
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

salary_label = tk.Label(root, text="Salary:")
salary_label.grid(row=1, column=0)
salary_entry = tk.Entry(root)
salary_entry.grid(row=1, column=1)

add_button = tk.Button(root, text="Add Employee", command=add_employee)
add_button.grid(row=2, column=0, columnspan=2)

# Create table to display employee records
tree = ttk.Treeview(root, columns=("ID", "Name", "Salary"))
tree.heading("#0", text="ID")
tree.heading("#1", text="Name")
tree.heading("#2", text="Salary")
tree.grid(row=3, column=0, columnspan=2)

# Display initial records
display_records()

root.mainloop()
