#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 20 15:15:34 2025

@author: michaelabessolo
"""

import os

# Global list to store employees
employees = []
filename = "employees.txt"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    print("\n------------------------ Employee Management System ---------------------------")
    print(f"There are ({len(employees)}) employees in the system.")
    print("-------------------------------------------------------------------------------------------")
    print("1. Add new employee")
    print("2. View all employees")
    print("3. Search employee by SSN")
    print("4. Edit employee information")
    print("5. Export employees’ information into a text file")
    print("6. Import employees’ information from a text file")
    print("7. Exit")
    print("-------------------------------------------------------------------------------------------")

def add_employee():
    print("\n--- Add New Employee ---")
    name = input("Enter Employee's Name: ")
    ssn = input("Enter Employee's SSN: ")
    phone = input("Enter Employee's Phone: ")
    email = input("Enter Employee's Email: ")
    try:
        salary = float(input("Enter Employee's Salary: "))
    except ValueError:
        print("Invalid salary input. Employee not added.")
        return

    employee = {
        "name": name,
        "ssn": ssn,
        "phone": phone,
        "email": email,
        "salary": salary
    }
    employees.append(employee)
    print(f"{name} has been added.")

def display_employee(emp):
    print(f"\n---------------------------- {emp['name']} -----------------------------")
    print(f"SSN: {emp['ssn']}")
    print(f"Phone: {emp['phone']}")
    print(f"Email: {emp['email']}")
    print(f"Salary: ${emp['salary']:,.2f}")
    print("------------------------------------------------------------------------")

def view_all_employees():
    if not employees:
        print("\nNo employees in the system.")
    else:
        for emp in employees:
            display_employee(emp)

def search_employee_by_ssn():
    ssn = input("Enter SSN to search: ")
    for emp in employees:
        if emp["ssn"] == ssn:
            display_employee(emp)
            return emp
    print("Employee not found.")
    return None

def edit_employee():
    emp = search_employee_by_ssn()
    if emp:
        print("Leave field blank to keep current value.")
        new_name = input(f"Enter new name (current: {emp['name']}): ")
        new_phone = input(f"Enter new phone (current: {emp['phone']}): ")
        new_email = input(f"Enter new email (current: {emp['email']}): ")
        new_salary = input(f"Enter new salary (current: {emp['salary']}): ")

        if new_name: emp['name'] = new_name
        if new_phone: emp['phone'] = new_phone
        if new_email: emp['email'] = new_email
        if new_salary:
            try:
                emp['salary'] = float(new_salary)
            except ValueError:
                print("Invalid salary. Keeping old value.")
        print("\nUpdated employee information:")
        display_employee(emp)

def export_employee_data():
    try:
        with open(filename, "w") as file:
            for emp in employees:
                file.write(f"{emp['name']},{emp['ssn']},{emp['phone']},{emp['email']},{emp['salary']:.2f}\n")
        print("Employee data exported successfully.")
    except Exception as e:
        print(f"Error exporting data: {e}")

def import_employee_data():
    try:
        with open(filename, "r") as file:
            for line in file:
                name, ssn, phone, email, salary = line.strip().split(',')
                employees.append({
                    "name": name,
                    "ssn": ssn,
                    "phone": phone,
                    "email": email,
                    "salary": float(salary)
                })
        print("Employee data imported successfully.")
    except FileNotFoundError:
        print("No existing employee data found.")
    except Exception as e:
        print(f"Error importing data: {e}")

def main():
    while True:
        display_menu()
        option = input("Choose an option (1-7): ")

        if option == '1':
            add_employee()
        elif option == '2':
            view_all_employees()
        elif option == '3':
            search_employee_by_ssn()
        elif option == '4':
            edit_employee()
        elif option == '5':
            export_employee_data()
        elif option == '6':
            import_employee_data()
        elif option == '7':
            print("Exiting the system.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
