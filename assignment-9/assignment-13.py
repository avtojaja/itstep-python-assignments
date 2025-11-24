# შექმენით csv ფაილი, რომელშიც გექნებათ შემდეგი სტრუქტურის მონაცემები:

# id,name,age,grade,subject_name,mark
# 1,string,0,string,string,0
# 2,string,0,string,string,0

import csv
import os

# ფაილის სახელი
file_name = "data_folder/students.csv"
os.makedirs("data_folder", exist_ok=True)

# შემოწმება, რომ არ მოხდეს არსებული ფაილის გადაწერა
if not os.path.exists(file_name):
    # მონაცემები
    data = [
        [1, "string", 0, "string", "string", 0],
        [2, "string", 0, "string", "string", 0]
    ]

    # CSV ფაილის შექმნა
    with open(file_name, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        # ჰედერი
        writer.writerow(["id", "name", "age", "grade", "subject_name", "mark"])

        # მონაცემების ჩაწერა
        for row in data:
            writer.writerow(row)

    print(f"CSV file '{file_name}' created successfully.")



# 1. დაწერეთ პითონის ფუნქცია, სადაც მომხმარებელი შეიყვანს ინფორმაციას (id,name,age,grade,subject_name,mark) და თქვენ სტუდენტს დაამატებს csv ფაილში. დაასორტირეთ მონაცემები id-ის მიხედვით.

def add_student_to_csv(file_name):
    try:
        # მომხმარებლის შეყვანა
        student_id = int(input("Enter student id: "))
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        grade = input("Enter grade: ")
        subject_name = input("Enter subject name: ")
        mark = int(input("Enter mark: "))

        # ახალი სტუდენტის მონაცემი
        new_student = [student_id, name, age, grade, subject_name, mark]

        # არსებული მონაცემების წაკითხვა, თუ ფაილი არსებობს
        if os.path.exists(file_name):
            with open(file_name, "r", newline="", encoding="utf-8") as csvfile:
                reader = csv.reader(csvfile)
                data = list(reader)
                header = data[0]  # ჰედერი
                rows = data[1:]
        else:
            header = ["id", "name", "age", "grade", "subject_name", "mark"]
            rows = []

        # ახალი სტუდენტის დამატება
        rows.append(new_student)

        # სორტირება id-ის მიხედვით (პირველი ელემენტი)
        rows.sort(key=lambda x: int(x[0]))

        # CSV-ში ჩაწერა
        with open(file_name, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)
            writer.writerows(rows)

        print(f"Student added and data sorted by id in '{file_name}'.")

    except ValueError:
        print("Error: Please enter valid numerical values for id, age, and mark.")
    except Exception as e:
        print(f"Error: {e}")


# ფუნქციის გამოძახება
add_student_to_csv(file_name)



# 2. დაწერეთ პითონის ფუნქცია, რომლის საშუალებით მომხმარებელს შეეძლება, როგორც ყველა, ასევე კონკრეტული სტუდენტის ინფორმაციის წაკითხვა ფაილიდან.

def read_student_csv(file_name):
    try:
        if not os.path.exists(file_name):
            print(f"Error: File '{file_name}' does not exist.")
            return

        with open(file_name, "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)

        if not data:
            print("The file is empty.")
            return

        choice = input("Enter 'all' to see all students or enter student id to search: ").strip()

        if choice == "" or choice.lower() == "all":
            print("\nAll students:")
            for student in data:
                print(student)
        else:
            try:
                student_id = choice
                found = False
                for student in data:
                    if student["id"] == student_id:
                        print("\nStudent information:")
                        print(student)
                        found = True
                        break
                if not found:
                    print(f"No student found with id: {student_id}")
            except Exception as e:
                print(f"Error: {e}")

    except Exception as e:
        print(f"Error: {e}")

# ფუნქციის გამოძახება
read_student_csv(file_name)



# 3. დაწერეთ პითონის ფუნქცია, რომელიც დაითვლის საშუალო ქულას (mark) საგნების მიხედვით.

def average_marks_by_subject(file_name):
    if not os.path.exists(file_name):
        print(f"Error: File '{file_name}' does not exist.")
        return

    subject_totals = {}
    subject_counts = {}

    try:
        with open(file_name, "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                subject = row["subject_name"]
                try:
                    mark = float(row["mark"])
                except ValueError:
                    continue # თუ mark რიცხვი არ არის, გამოტოვებს

                if subject in subject_totals:
                    subject_totals[subject] += mark
                    subject_counts[subject] += 1
                else:
                    subject_totals[subject] = mark
                    subject_counts[subject] = 1

        print("Average marks by subject:")
        for subject in subject_totals:
            avg = subject_totals[subject] / subject_counts[subject]
            print(f"{subject}: {avg:.2f}")

    except Exception as e:
        print(f"Error: {e}")

# მაგალითი გამოძახება
average_marks_by_subject(file_name)



# 4. დაწერეთ პითონის ფუნქცია, რომლის საშუალებით შესაძლებელი იქნება სტუდენტის ქულის განახლება/ცვლილება. მომხმარებელი შეიყვანს სტუდენტის id, საგანს და განახლებულ ქულას.

def update_student_mark(file_name):
    if not os.path.exists(file_name):
        print(f"Error: File '{file_name}' does not exist.")
        return

    try:
        student_id = input("Enter student id: ").strip()
        subject = input("Enter subject name: ").strip()
        new_mark = input("Enter new mark: ").strip()

        # ქულის კონვერტირება რიცხვში
        try:
            new_mark = int(new_mark)
        except ValueError:
            print("Error: Mark must be a number.")
            return

        # CSV-ს წაკითხვა
        with open(file_name, "r", newline="", encoding="utf-8") as csvfile:
            reader = list(csv.DictReader(csvfile))
            fieldnames = reader[0].keys() if reader else ["id", "name", "age", "grade", "subject_name", "mark"]

        # სიაში ცვლილება
        updated = False
        for row in reader:
            if row["id"] == student_id and row["subject_name"].lower() == subject.lower():
                row["mark"] = str(new_mark)
                updated = True
                break

        if not updated:
            print(f"No matching student with id={student_id} and subject={subject} found.")
            return

        # CSV-ში ჩაწერა
        with open(file_name, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(reader)

        print(f"Student id={student_id} mark for '{subject}' updated to {new_mark}.")

    except Exception as e:
        print(f"Error: {e}")


# ფუნქციის გამოძახება
update_student_mark(file_name)
