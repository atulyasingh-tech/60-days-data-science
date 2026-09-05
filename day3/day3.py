import csv

# Dictionary to store grade frequencies
grade_count = {}

# Read the CSV file
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        grade = row["Grade"]

        # Count the grade
        if grade in grade_count:
            grade_count[grade] += 1
        else:
            grade_count[grade] = 1

# Write the summary to a new CSV file
with open("grade_summary.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Header
    writer.writerow(["Grade", "Frequency"])

    # Grade frequencies
    for grade, frequency in grade_count.items():
        writer.writerow([grade, frequency])

print("Grade summary has been saved to grade_summary.csv")
