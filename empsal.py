# Function to create an employee details dictionary
def create_employee_details(name, salary, leaves, week_offs):
    return {
        "Name": name,
        "Salary": salary,
        "Leaves": leaves,
        "Week-offs": week_offs,
    }

# Function to print employee details
def print_employee_details(employee_details):
    print("Employee Details for March:")
    for key, value in employee_details.items():
        print(f"{key}: {value}")

# Example usage
employee = create_employee_details(
    name="Akshatha",
    salary=45000,   # Monthly salary
    leaves=2,       # Leaves taken in March
    week_offs=["Saturday", "Sunday"]  # Week-off days
)

# Print the employee details
print_employee_details(employee)