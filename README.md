## Please carefullyread this guide -- DANIEL IBANGA

### Python (Jupyter Notebook)
1. **Setup:**
   - Ensure you have Python 3.x installed.
   - Install the required Python packages if not already installed:
     ```
     pip install pandas
     ```
2. **Usage:**
   - Open the `employee_profile.ipynb` file in Jupyter Notebook.
   - Confirm that `salary_data.csv` is in the same directory.
   - Execute the cells sequentially.
   - The notebook will:
     - Import the salary data.
     - Process the data into a dictionary.
     - Define a function to retrieve an employee's details.
     - Export the details of a specified employee to a CSV file.
     - Zip the CSV file into `Employee_Profile.zip`.

### R Script
1. **Setup:**
   - Ensure you have R installed on your system.
2. **Usage:**
   - Open the `Unzip_Employee_Profile.R` script in your R environment (e.g., RStudio).
   - Run the script. It will:
     - Pass the path containing the zip file
	 - Unzip `Employee_Profile.zip` into a folder named `Employee_Profile`.
     - List the extracted files.
     - Read and display the contents of the CSV file containing employee details.