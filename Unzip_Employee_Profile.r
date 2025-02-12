unzip(zipfile = "Pass in the zip file location here", 
      exdir = "Employee_Profile")

# List the files in the unzipped folder
files <- list.files("Employee_Profile", full.names = TRUE)
cat("Files extracted:\n")
print(files)

# Read the CSV file
if (length(files) > 0) {
  employee_data <- read.csv(files[1])
  cat("Employee Details:\n")
  print(employee_data)
} else {
  cat("No files found in the unzipped folder.\n")
}