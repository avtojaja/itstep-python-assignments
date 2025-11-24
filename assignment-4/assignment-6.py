# დაწერეთ პროგრამა, რომელიც ტერმინალში მომხმარებელს გამოუტანს სტუდენტების აიდის (id) სიას, მომხმარებელი აირჩევს სტუდენტის აიდის, მიღებული აიდისთვის დაბეჭდავს სტუდენტის მონაცემებს. მონაცემებში უნდა დაიბეჭდოს (სახელი, გვარი, ასაკი და ქულა თითოეული საგნის მიხედვით)

# მაგალითად: მომხმარებელმა თუ აირჩია სტუდენტი აიდით 20, უნდა დაბეჭდოთ ამ სტუდენტის ინფორმაცია.

# terminal ouput:
# studentebis ID: 20, 25, 56, 100, 1232, 846723
# airchiet studentis ID:
# შემდეგ მომხმარებელს შეყავს აიდი, მაგალითად - 20

# პროგრამა ბეჭდავს ტერმინალში შემდეგ ინფორმაციას (output):

# student information:
# ID: 20, Name: Giorgi, Age: 25
# subject: Math, grade: B
# subject: Physics, grade: A
# subject: English, grade: A
# subject: Chemistry, grade: B
# subject: History, grade: c

# my_dict = {
#   "students": [
#     {"id": 20, "name": "Giorgi", "age": 25},
#     {"id": 25, "name": "Giorgi", "age": 23},
#     {"id": 56, "name": "Nika", "age": 25},
#     {"id": 100, "name": "Nika", "age": 22},
#     {"id": 1232, "name": "Dato", "age": 22},
#     {"id": 846723, "name": "Archili", "age": 32}
#   ],
#   "subjects": [
#     {"id": 1, "name": "Math", "grades": {"20": "B", "25": "A", "56": "B", "100": "A", "1232": "C", "846723": "A"}},
#     {"id": 2, "name": "Physics", "grades": {"20": "A", "25": "B", "56": "B", "100": "A", "1232": "C", "846723": "B"}},
#     {"id": 3, "name": "English", "grades": {"20": "A", "25": "A", "56": "A", "100": "A", "1232": "B", "846723": "A"}},
#     {"id": 4, "name": "Chemistry", "grades": {"20": "B", "25": "B", "56": "B", "100": "A", "1232": "A", "846723": "A"}},
#     {"id": 5, "name": "History", "grades": {"20": "C", "25": "B", "56": "B", "100": "A", "1232": "A", "846723": "A"}},
#   ]
# }


# სტუდენტებისა და საგნების მონაცემები
my_dict = {
  "students": [
    {"id": 20, "name": "Giorgi", "age": 25},
    {"id": 25, "name": "Giorgi", "age": 23},
    {"id": 56, "name": "Nika", "age": 25},
    {"id": 100, "name": "Nika", "age": 22},
    {"id": 1232, "name": "Dato", "age": 22},
    {"id": 846723, "name": "Archili", "age": 32}
  ],
  "subjects": [
    {"id": 1, "name": "Math", "grades": {"20": "B", "25": "A", "56": "B", "100": "A", "1232": "C", "846723": "A"}},
    {"id": 2, "name": "Physics", "grades": {"20": "A", "25": "B", "56": "B", "100": "A", "1232": "C", "846723": "B"}},
    {"id": 3, "name": "English", "grades": {"20": "A", "25": "A", "56": "A", "100": "A", "1232": "B", "846723": "A"}},
    {"id": 4, "name": "Chemistry", "grades": {"20": "B", "25": "B", "56": "B", "100": "A", "1232": "A", "846723": "A"}},
    {"id": 5, "name": "History", "grades": {"20": "C", "25": "B", "56": "B", "100": "A", "1232": "A", "846723": "A"}},
  ]
}

# ყველა სტუდენტის ID-ების სია
student_ids = [str(student["id"]) for student in my_dict["students"]]
print("studentebis ID:", ", ".join(student_ids))

# ID-ის არჩევა
selected_id = input("airchiet studentis ID: ").strip()

# სტუდენტის ძიება
student = None
for s in my_dict["students"]:
    if str(s["id"]) == selected_id:
        student = s
        break

# სტუდენტის ინფორმაციის დაბეჭდვა
if student:
    print("\nstudent information:")
    print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}")

    # საგნების ქულების დაბეჭდვა
    for subject in my_dict["subjects"]:
        grade = subject["grades"].get(selected_id, "N/A")
        print(f"subject: {subject['name']}, grade: {grade}")
else:
    print("ასეთი ID-ის მქონე სტუდენტი ვერ მოიძებნა.")
