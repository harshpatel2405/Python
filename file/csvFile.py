import csv

# ==========================================
# WRITE DATA INTO CSV FILE
# ==========================================

# Open CSV file in write mode
with open("students.csv", "w", newline="") as f:

    # Create CSV writer
    writer = csv.writer(f)

    # Write header
    writer.writerow(["Name", "Age", "City"])

    # Write student data
    writer.writerow(["Harsh", 22, "Ahmedabad"])
    writer.writerow(["raj", 23, "Anand"])
    writer.writerow(["Jeel", 21, "Vadodara"])


# ==========================================
# READ DATA FROM THE SAME CSV FILE
# ==========================================

# Open the same file in read mode
with open("students.csv", "r") as f:

    # Create CSV reader
    reader = csv.reader(f)
    # print(list(reader))

    # Read each row
    for row in reader:
        print(row)