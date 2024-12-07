#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv  


class Employee:
    def __init__(self, employee_id, employee_name, employee_position, employee_salary, employee_email):
        # Initialize employee object with attributes
        self.id = employee_id
        self.name = employee_name
        self.position = employee_position
        self.salary = employee_salary
        self.email = employee_email
        
    def display_info(self):
        # Return employee information 
        return f"ID: {self.id}, Name: {self.name}, Position: {self.position}, Salary: {self.salary}, Email: {self.email}"



class EmployeeManager:
    file_name = 'employees.csv'  # CSV File to store employee data

    def __init__(self):
        # Initialize employee manager and load data from CSV file
        self.employees = {}  # Dictionary to store employees
        self.load_data()

    def load_data(self):
        # Load employee data from the CSV file into the employees dictionary
        try:
            with open(self.file_name, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    emp = Employee(row['ID'], row['Name'], row['Position'], row['Salary'], row['Email'])
                    self.employees[emp.id] = emp
        except FileNotFoundError:
            print("file not found")

    def save_data(self):
        # Save current employee data to the CSV file
        with open(self.file_name, mode='w', newline='') as file:
            fieldnames = ['ID', 'Name', 'Position', 'Salary', 'Email']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()  # Write the header row
            for emp in self.employees.values():
                # Write each data as a new row in CSV file
                writer.writerow({'ID': emp.id, 'Name': emp.name, 'Position': emp.position,
                                 'Salary': emp.salary, 'Email': emp.email})

    def add_employee(self):  # Add a new employee 
        
        employee_id = input("Enter Employee ID: ")
        if employee_id in self.employees:
            print("Employee already exists")  # Check if the employee ID already exists
            return
        employee_name = input("Enter Employee Name: ")
        employee_position = input("Enter Employee Position: ")
        employee_salary = input("Enter Employee Salary: ")
        employee_email = input("Enter Employee Email: ")

        if "@" not in employee_email and ".com" not in employee_email:
            print("Email Error")  # Validate email format
            return

        try:
            if float(employee_salary) <= 0:  # Validate salary
                print("Salary error")
                return
        except ValueError:
            print("Salary must be a positive number")
            return

        emp = Employee(employee_id, employee_name, employee_position, employee_salary, employee_email)
        self.employees[employee_id] = emp  # Add the new employee to the dictionary
        self.save_data()  # Save data to file
        print("Successfully Added Employee ")

    def update_employee(self):
        # Update an existing employee information
        employee_id = input("Enter Employee ID to update: ")
        if employee_id not in self.employees:
            print("There is no such Employee")  # Check if employee exists
            return

        emp = self.employees[employee_id]
        new_name = input(f"Enter new Employee Name ({emp.name}): ")
        new_position = input(f"Enter new Employee Position ({emp.position}): ")
        new_salary = input(f"Enter new Employee Salary ({emp.salary}): ")
        new_email = input(f"Enter new Employee Email ({emp.email}): ")

        if new_email and ("@" not in new_email and ".com" not in new_email):
            print("Email Error")  # Validate new email
            return

        if new_salary:
            try:
                if float(new_salary) <= 0:  # Validate new salary
                    print("Salary Error")
                    return
            except ValueError:
                print("Salary must be a positive number")
                return

        # Update the employee's information
        emp.name = new_name 
        emp.position = new_position 
        emp.salary = new_salary
        emp.email = new_email 
        self.save_data()  # Save the updated data to the file
        print("Employee updated Successfully ")

    def delete_employee(self):
        # Delete an employee by their ID
        employee_id = input("Enter Employee ID to delete: ")
        if employee_id in self.employees:
            del self.employees[employee_id]  # Remove employee from dictionary
            self.save_data()  # Save changes to the file
            print("Employee deleted!")
        else:
            print("No such Employee")

    def search_employee(self):
        # Search and display employee by ID
        employee_id = input("Enter Employee ID to search: ")
        emp = self.employees.get(employee_id)
        if emp:
            print(f"ID: {emp.id}, Name: {emp.name}, Position: {emp.position}, Salary: {emp.salary}, Email: {emp.email}")
        else:
            print("No such Employee")

    def list_all_employees(self):
        # List all employees in the system
        if self.employees:
            for emp in self.employees.values():
                print(f"ID: {emp.id}, Name: {emp.name}, Position: {emp.position}, Salary: {emp.salary}, Email: {emp.email}")
        else:
            print("No employees found")

# Main program with CLI (Command-Line Interface)
def main():
    manage = EmployeeManager()  #  instance of EmployeeManager
    while True:
        # Display the menu with options
        print("\nMenu:")
        print("A. Add Employee")
        print("B. Update Employee")
        print("C. Delete Employee")
        print("D. Search Employee")
        print("E. List All Employees")
        print("F. Exit")

        choose = input("Choos from the menu: ")
        if choose == 'A' or 'a':
            manage.add_employee()
        elif choose == 'B'or 'b':
            manage.update_employee()
        elif choose == 'C' or 'c':
            manage.delete_employee()
        elif choose == 'D' or 'd':
            manage.search_employee()
        elif choose == 'E' or 'e':
            manage.list_all_employees()
        elif choose == 'F' or 'e':
            print("Program will Exit")  # Exit the program
            break
        else:
            print("Invalid choice, please try again")  # Handle invalid choice

if __name__ == "__main__":
    main()  # Start the program


# In[ ]:


import csv


class Employee:
    def __init__(self, employee_id, employee_name, employee_position, employee_salary, employee_email):
        # Initialize employee object with attributes
        self.id = employee_id
        self.name = employee_name
        self.position = employee_position
        self.salary = employee_salary
        self.email = employee_email

    def display_info(self):
        # Return employee information as a formatted string
        return f"ID: {self.id}, Name: {self.name}, Position: {self.position}, Salary: {self.salary}, Email: {self.email}"


class EmployeeManager:
    file_name = 'employees.csv'  # CSV file to store employee data

    def __init__(self):
        # Initialize employee manager and load data from CSV file
        self.employees = {}  # Dictionary to store employees
        self.load_data()

    def load_data(self):
        # Load employee data from the CSV file into the employees dictionary
        try:
            with open(self.file_name, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    emp = Employee(row['ID'], row['Name'], row['Position'], row['Salary'], row['Email'])
                    self.employees[emp.id] = emp
        except FileNotFoundError:
            print("File not found. Starting fresh.")

    def save_data(self):
        # Save current employee data to the CSV file
        with open(self.file_name, mode='w', newline='') as file:
            fieldnames = ['ID', 'Name', 'Position', 'Salary', 'Email']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()  # Write the header row
            for emp in self.employees.values():
                writer.writerow({'ID': emp.id, 'Name': emp.name, 'Position': emp.position,
                                 'Salary': emp.salary, 'Email': emp.email})

    def add_employee(self):
        # Add a new employee
        employee_id = input("Enter Employee ID: ")
        if employee_id in self.employees:
            print("Employee already exists!")
            return
        employee_name = input("Enter Employee Name: ")
        employee_position = input("Enter Employee Position: ")
        employee_salary = input("Enter Employee Salary: ")
        employee_email = input("Enter Employee Email: ")

        if "@" not in employee_email or ".com" not in employee_email:
            print("Invalid email format.")
            return

        try:
            employee_salary = float(employee_salary)
            if employee_salary <= 0:
                print("Salary must be a positive number.")
                return
        except ValueError:
            print("Salary must be a valid number.")
            return

        emp = Employee(employee_id, employee_name, employee_position, employee_salary, employee_email)
        self.employees[employee_id] = emp
        self.save_data()
        print("Employee added successfully.")

    def update_employee(self):
        # Update an existing employee's information
        employee_id = input("Enter Employee ID to update: ")
        if employee_id not in self.employees:
            print("No such employee exists.")
            return

        emp = self.employees[employee_id]
        
        new_name = input(f"Enter new Employee Name : ") or emp.name
        new_position = input(f"Enter new Employee Position : ") or emp.position
        new_salary = input(f"Enter new Employee Salary : ")
        new_email = input(f"Enter new Employee Email : ") or emp.email

        if new_salary:
            try:
                new_salary = float(new_salary)
                if new_salary <= 0:
                    print("Salary must be a positive number.")
                    return
            except ValueError:
                print("Salary must be a valid number.")
                return
        else:
            new_salary = emp.salary

        if "@" not in new_email or ".com" not in new_email:
            print("Invalid email format.")
            return

        # Update employee details
        emp.name = new_name
        emp.position = new_position
        emp.salary = new_salary
        emp.email = new_email
        self.save_data()
        print("Employee updated successfully.")

    def delete_employee(self):
        # Delete an employee by their ID
        employee_id = input("Enter Employee ID to delete: ")
        if employee_id in self.employees:
            del self.employees[employee_id]
            self.save_data()
            print("Employee deleted.")
        else:
            print("No such employee exists.")

    def search_employee(self):
        # Search and display an employee by ID
        employee_id = input("Enter Employee ID to search: ")
        emp = self.employees.get(employee_id)
        if emp:
            print(emp.display_info())
        else:
            print("No such employee found.")

    def list_all_employees(self):
        # List all employees in the system
        if self.employees:
            for emp in self.employees.values():
                print(emp.display_info())
        else:
            print("No employees found.")


# Main program with CLI (Command-Line Interface)
def main():
    manager = EmployeeManager()
    while True:
        # Display the menu with options
        print("\nMenu:")
        print("A. Add Employee")
        print("B. Update Employee")
        print("C. Delete Employee")
        print("D. Search Employee")
        print("E. List All Employees")
        print("F. Exit")

        choice = input("Choose from the menu: ").lower()
        if choice == 'a':
            manager.add_employee()
        elif choice == 'b':
            manager.update_employee()
        elif choice == 'c':
            manager.delete_employee()
        elif choice == 'd':
            manager.search_employee()
        elif choice == 'e':
            manager.list_all_employees()
        elif choice == 'f':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


# In[ ]:




