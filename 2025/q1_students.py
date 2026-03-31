import csv
import os


class Student:
    """Task 1.1: Student class"""
    def __init__(self, student_id, name, house, year, grade):
        self.student_id = student_id
        self.name = name
        self.house = house
        self.year = year
        self.grade = grade
    
    def __str__(self):
        return (f"ID: {self.student_id}, Name: {self.name}, House: {self.house}, "
                f"Year: {self.year}, Grade: {self.grade}")


def LoadStudents(filename="students.csv"):
    """Task 1.1: Load students from CSV file"""
    students = {}
    
    if not os.path.exists(filename):
        print(f"Error: {filename} not found")
        return students
    
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        
        for row in reader:
            student_id = row[0]
            students[student_id] = Student(row[0], row[1], row[2], 
                                          int(row[3]), row[4])
    
    print(f"Loaded {len(students)} students")
    return students


def DisplayAllStudents(students):
    """Task 1.1: Display all students"""
    print("\nAll Students:")
    print("-" * 80)
    for student in students.values():
        print(student)


def DisplayStudentsByHouse(house, students):
    """Task 1.2: Display students by house"""
    found = []
    for student in students.values():
        if student.house.lower() == house.lower():
            found.append(student)
    
    if found:
        print(f"\nStudents in {house}:")
        for student in found:
            print(f"  {student}")
    else:
        print(f"No students found in house {house}")
    
    return found


def DisplayStudentsByYear(year, students):
    """Task 1.2: Display students by year"""
    found = []
    for student in students.values():
        if student.year == year:
            found.append(student)
    
    if found:
        print(f"\nStudents in Year {year}:")
        for student in found:
            print(f"  {student}")
    else:
        print(f"No students found in Year {year}")
    
    return found


def DisplayStudentsByGrade(grade, students):
    """Task 1.2: Display students by grade"""
    found = []
    for student in students.values():
        if student.grade.lower() == grade.lower():
            found.append(student)
    
    if found:
        print(f"\nStudents with grade {grade}:")
        for student in found:
            print(f"  {student}")
    else:
        print(f"No students found with grade {grade}")
    
    return found


def SearchStudentsByName(search_term, students):
    """Task 1.2: Search students by name (partial match)"""
    found = []
    search_lower = search_term.lower()
    
    for student in students.values():
        if search_lower in student.name.lower():
            found.append(student)
    
    if found:
        print(f"\nStudents matching '{search_term}':")
        for student in found:
            print(f"  {student}")
    else:
        print(f"No students found matching '{search_term}'")
    
    return found


def AddNewStudent(student_id, name, house, year, grade, students):
    """Task 1.3: Add a new student"""
    if student_id in students:
        print(f"Student ID {student_id} already exists")
        return False
    
    students[student_id] = Student(student_id, name, house, year, grade)
    print(f"Added student: {name}")
    return True


def UpdateStudentGrade(student_id, new_grade, students):
    """Task 1.3: Update student grade"""
    if student_id in students:
        old_grade = students[student_id].grade
        students[student_id].grade = new_grade
        print(f"Updated {students[student_id].name} grade from {old_grade} to {new_grade}")
        return True
    
    print(f"Student {student_id} not found")
    return False


def UpdateStudentHouse(student_id, new_house, students):
    """Task 1.3: Update student house"""
    if student_id in students:
        old_house = students[student_id].house
        students[student_id].house = new_house
        print(f"Updated {students[student_id].name} house from {old_house} to {new_house}")
        return True
    
    print(f"Student {student_id} not found")
    return False


def DeleteStudent(student_id, students):
    """Task 1.3: Delete a student"""
    if student_id in students:
        removed = students.pop(student_id)
        print(f"Deleted student: {removed.name}")
        return True
    
    print(f"Student {student_id} not found")
    return False


def SaveStudents(filename, students):
    """Task 1.4: Save all students to CSV file"""
    with open(filename, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["StudentID", "Name", "House", "Year", "Grade"])
        
        for student in students.values():
            writer.writerow([student.student_id, student.name, student.house,
                           student.year, student.grade])
    
    print(f"Saved {len(students)} students to {filename}")


def CountStudentsByHouse(students):
    """Task 1.4: Count students by house"""
    houses = {}
    
    for student in students.values():
        if student.house not in houses:
            houses[student.house] = 0
        houses[student.house] += 1
    
    print("\nStudents by house:")
    for house, count in sorted(houses.items(), key=lambda x: x[1], reverse=True):
        print(f"  {house}: {count}")
    
    return houses


def CountStudentsByYear(students):
    """Task 1.4: Count students by year"""
    years = {}
    
    for student in students.values():
        if student.year not in years:
            years[student.year] = 0
        years[student.year] += 1
    
    print("\nStudents by year:")
    for year, count in sorted(years.items()):
        print(f"  Year {year}: {count}")
    
    return years


def CountStudentsByGrade(students):
    """Task 1.4: Count students by grade"""
    grades = {}
    
    for student in students.values():
        if student.grade not in grades:
            grades[student.grade] = 0
        grades[student.grade] += 1
    
    print("\nStudents by grade:")
    for grade, count in sorted(grades.items()):
        print(f"  Grade {grade}: {count}")
    
    return grades


def GetAverageYear(students):
    """Task 1.4: Calculate average year"""
    if not students:
        return 0
    
    total = sum(student.year for student in students.values())
    avg = total / len(students)
    print(f"Average year: {avg:.1f}")
    return avg


def FindTopStudents(n, students):
    """Task 1.4: Find top n students by grade"""
    grade_order = {'A*': 0, 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'U': 6}
    
    sorted_students = sorted(students.values(), 
                            key=lambda s: grade_order.get(s.grade, 7))
    
    top = sorted_students[:n]
    
    print(f"\nTop {n} students:")
    for student in top:
        print(f"  {student.name}: {student.grade}")
    
    return top


if __name__ == "__main__":
    students = LoadStudents("students.csv")
    
    if students:
        DisplayAllStudents(students)
        
        print("\n" + "=" * 80)
        print("Task 1.2: Search and Filter")
        print("=" * 80)
        DisplayStudentsByHouse("Gryffindor", students)
        DisplayStudentsByYear(12, students)
        DisplayStudentsByGrade("A", students)
