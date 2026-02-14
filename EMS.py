def add_employee(employees):
    """Adds a new employee with a unique ID."""
    print("\n--- Add New Employee ---")
    while True:
        try:
            emp_id = int(input("Enter Employee ID: "))
            if emp_id in employees:
                print(f"Error: ID {emp_id} already exists. Please use a unique ID.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numeric ID.")

    name = input("Enter Name: ")

    while True:
        try:
            age = int(input("Enter Age: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric age.")

    department = input("Enter Department: ")

    while True:
        try:
            salary = float(input("Enter Monthly Salary: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric salary.")

    # Storing data in the nested dictionary
    employees[emp_id] = {
        'name': name,
        'age': age,
        'department': department,
        'salary': salary
    }
    print(f"\nSuccess: Employee '{name}' added successfully!")


def view_employees(employees):
    """Displays all employees in a formatted table."""
    print("\n--- All Employees ---")
    if not employees:
        print("No employees available.")
        return

    # Table Header
    print(f"{'ID':<10} {'Name':<15} {'Age':<10} {'Department':<15} {'Salary':<10}")
    print("-" * 60)

    for emp_id, info in employees.items():
        print(f"{emp_id:<10} {info['name']:<15} {info['age']:<10} {info['department']:<15} {info['salary']:<10.2f}")


def search_employee(employees):
    """Searches for a specific employee by their ID."""
    print("\n--- Search Employee ---")
    try:
        emp_id = int(input("Enter Employee ID to search: "))
        if emp_id in employees:
            emp = employees[emp_id]
            print(f"\nEmployee Found:")
            print(f"ID: {emp_id}")
            print(f"Name: {emp['name']}")
            print(f"Age: {emp['age']}")
            print(f"Department: {emp['department']}")
            print(f"Salary: ${emp['salary']:,.2f}")
        else:
            print("Employee not found.")
    except ValueError:
        print("Invalid input. Please enter a numeric ID.")


def main_menu():
    """Main loop for the menu system."""
    # Step 1: Initialize with sample data
    employees = {
        101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000.0}
    }

    while True:
        print("\n==============================")
        print("  Employee Management System  ")
        print("==============================")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")

        choice = input("\nSelect an option (1-4): ")

        if choice == '1':
            add_employee(employees)
        elif choice == '2':
            view_employees(employees)
        elif choice == '3':
            search_employee(employees)
        elif choice == '4':
            print("Thank you for using the EMS. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main_menu()