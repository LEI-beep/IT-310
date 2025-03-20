print("Welcome to the Grade Calculator")
name = input("Enter your name: ")
grades = []
units = []

while True:
    try:
        unit = input("Enter the number of units (or type 'done' to finish): ")
        if unit.lower() == 'done':
            break
        unit = int(unit)
        if unit > 0:
            unit_grades = []
            for i in range(unit):
                while True:
                    try:
                        grade = float(input(f"Enter grade {i+1} for these {unit} units: "))
                        if 0 <= grade <= 100:
                            unit_grades.append(grade)
                            break
                        else:
                            print("Grade must be between 0 and 100.")
                    except ValueError:
                        print("Invalid input. Please enter a valid grade.")
            average_grade = sum(unit_grades) / unit
            grades.append((average_grade, unit))
            units.append(unit)
        else:
            print("Units must be a positive integer.")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if grades:
    total_weighted_score = sum(grade * unit for grade, unit in grades)
    total_units = sum(units)
    weighted_average = total_weighted_score / total_units
    
    if 97 <= weighted_average <= 100:
        college_grade = 1.0
    elif 94 <= weighted_average < 96:
        college_grade = 1.25
    elif 91 <= weighted_average < 93:
        college_grade = 1.50
    elif 88 <= weighted_average < 90:
        college_grade = 1.75
    elif 85 <= weighted_average < 87:
        college_grade = 2.00
    elif 82 <= weighted_average < 84:
        college_grade = 2.25
    elif 79 <= weighted_average < 81:
        college_grade = 2.25
    elif 76 <= weighted_average < 78:
        college_grade = 2.75
    elif 75 <= weighted_average < 75:
        college_grade = 3.0
    elif 60 <= weighted_average < 74:
        college_grade = 5.0
    else:
        college_grade = 5.0 
    
    if college_grade == 1.0:
        description = "Excellent"
    elif college_grade == 1.5:
        description = "Very Good"
    elif college_grade == 2.0:
        description = "Good"
    elif college_grade == 2.5:
        description = "Satisfactory"
    elif college_grade == 3.0:
        description = "Passed"
    elif college_grade == 3.5:
        description = "passed"
    elif college_grade == 4.0:
        description = "maybe"
    elif college_grade == 4.5:
        description = "failed"
    elif college_grade == 5.0:
        description = "very failed"
    else:
        description = "Failing"
    
    print("\n--- Grade Summary ---")
    print(f"Name: {name}")
    print(f"Weighted Average Grade: {weighted_average:.2f}")
    print(f"College Grade Equivalent: {college_grade:.1f}")
    print(f"Description: {description}")
else:
    print(f"No grades entered. Goodbye, {name}!")
