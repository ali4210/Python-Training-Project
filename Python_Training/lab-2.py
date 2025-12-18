import csv
import
# Open a file in write mode
with open('lab-1.py', 'w', newline='') as file:
    # Specify the fieldnames (columns)
    fieldnames = ["Name", "Age", "City"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # Write the header
    writer.writeheader()

    # Write data rows

    for row in data_dict:
        writer.writerow(row)