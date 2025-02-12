import pandas as pd
import os
import zipfile

salary_file = r'Employee_Payroll.csv'

try:
    df = pd.read_csv(salary_file)
    print("Salary data imported successfully.")
except FileNotFoundError:
    print(f"Error: {salary_file} not found. Please ensure the file is in the working directory.")
    raise

employee_dict = {}

for index, row in df.iterrows():
    name = row['EmployeeName']
    employee_dict[name] = row.to_dict()

print("Employee data has been processed into a dictionary.")

def get_employee_details(name):
    """
    Given an employee name, return their details.
    Raises a ValueError if the employee is not found in the dataset.
    This is advantage of using dictionaries(data structure)
    """
    try:
        details = employee_dict[name]
        return details
    except KeyError:
        raise ValueError(f"Employee '{name}' not found in the dataset.")


# Example usage:
# Change this to an actual employee name that exists in your salary_data.csv
employee_name = "GARY JIMENEZ"

try:
    details = get_employee_details(employee_name)
    print(f"Details for {employee_name}:")
    print(details)
except ValueError as e:
    print(e)
    details = None  # Ensure details is set to None if not found

if details is not None:
    # Creating a CSV filename based on the employee's name
    output_csv = f"{employee_name.replace(' ', '_')}_profile.csv"

    try:
        emp_df = pd.DataFrame([details])
        emp_df.to_csv(output_csv, index=False)
        print(f"Employee details exported to {output_csv}.")
    except Exception as e:
        print(f"Error exporting employee details: {e}")

    zip_filename = "Employee_Profile.zip"

    try:
        # Creates a zip file here...
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:

            #adding the csv file to the zip
            zipf.write(output_csv)
        print(f"{output_csv} has been zipped into {zip_filename}.")
    except Exception as e:
        print(f"Error creating zip file: {e}")
else:
    print("Employee details could not be exported because the employee was not found.")