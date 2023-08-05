from faker import Faker
import json
from employee import Employee

fake = Faker()


def generate_fake_data(num_employees=1):
    employees = []
    for _ in range(num_employees):
        name = fake.name()
        age = fake.random_int(min=20, max=65)
        position = fake.job()
        salary = fake.random_int(min=30000, max=100000)
        employee = Employee(name, age, position, salary)
        employees.append(employee.to_dict())

    with open('employees.json', 'w') as f:
        json.dump(employees, f, indent=2)


if __name__ == "__main__":
    generate_fake_data(num_employees=100)
