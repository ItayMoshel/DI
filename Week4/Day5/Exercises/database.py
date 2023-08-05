import sqlite3
from employee import Employee

DB_FILE = 'employee.db'


def create_table():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS employees
                 (name TEXT, age INTEGER, position TEXT, salary INTEGER)''')
    conn.commit()
    conn.close()


def add_employee(employee):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO employees VALUES (?, ?, ?, ?)",
              (employee.name, employee.age, employee.position, employee.salary))
    conn.commit()
    conn.close()


def get_employees():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM employees")
    rows = c.fetchall()
    conn.close()
    employees = []
    for row in rows:
        employee = Employee(row[0], row[1], row[2], row[3])
        employees.append(employee)
    return employees


def update_employee(employee):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("UPDATE employees SET age=?, position=?, salary=? WHERE name=?",
              (employee.age, employee.position, employee.salary, employee.name))
    conn.commit()
    conn.close()
    print("Updated Employee Information:")


def delete_employee(name):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("DELETE FROM employees WHERE name=?", (name,))
    conn.commit()
    conn.close()
