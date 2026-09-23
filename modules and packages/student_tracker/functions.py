import data


def add_student( student_id, name, initial_marks):
    m = {
        student_id: {
            "name": name,
            "marks": initial_marks,
        }
    }
    data.students_db.append(m)
    print("Data Stored Successfully for the student")


#     # (database, student_id, name, initial_marks): Checks if the ID already exists; if not, creates the student record in the dictionary.
# def add_marks():
# # (database, student_id, new_mark): Finds the student by ID and adds a new mark to their list.
# def calculate_average():
# # (database, student_id): Computes the average score for a specific student.
# def display_report():
# # (database): Loops through all records and prints every student's details and average score.
