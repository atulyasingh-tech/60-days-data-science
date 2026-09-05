
def calculate_average(marks):
    return sum(marks) / len(marks)
n = int(input("Enter number of subjects: "))

marks = []
for i in range(n):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

average = calculate_average(marks)

if average >= 75:
    result = "Distinction"
elif average >= 40:
    result = "Pass"
else:
    result = "Fail"


print("\n--- Student Result ---")
print("Marks:", marks)
print("Average:", round(average, 2))
print("Result:", result)
