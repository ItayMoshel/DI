from employee import Employee
from database import create_table, add_employee, get_employees, update_employee, delete_employee
from data_generator import generate_fake_data
from api_interaction import get_github_user_info
import json

create_table()

generate_fake_data(100)

with open('employees.json', 'r') as f:
    employees_data = json.load(f)
    for emp_data in employees_data:
        employee = Employee(emp_data["name"], emp_data["age"], emp_data["position"], emp_data["salary"])
        add_employee(employee)

employees = get_employees()
for employee in employees:
    print(f"Name: {employee.name}, Age: {employee.age}, Position: {employee.position}, Salary: {employee.salary}")

employee_to_update = employees[0]
employee_to_update.age = 30
employee_to_update.position = "Senior Developer"
employee_to_update.salary = 90000
update_employee(employee_to_update)

print(
    f"Name: {employee_to_update.name}, Age: {employee_to_update.age}, Position: {employee_to_update.position}, Salary: {employee_to_update.salary}")

delete_employee(employee_to_update.name)
print("Remaining Employees:")
remaining_employees = get_employees()
for employee in remaining_employees:
    print(f"Name: {employee.name}, Age: {employee.age}, Position: {employee.position}, Salary: {employee.salary}")

github_username = 'ItayMoshel'
github_user_info = get_github_user_info(github_username)
if github_user_info:
    print(f"\nGitHub User Info for {github_username}:")
    print(f"Name: {github_user_info['name']}")
    print(f"Public Repositories: {github_user_info['public_repos']}")
    print(f"Followers: {github_user_info['followers']}")
    print(f"Following: {github_user_info['following']}")

