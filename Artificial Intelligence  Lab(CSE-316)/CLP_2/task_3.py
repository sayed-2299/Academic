students=(
    ("sanjida",23,3.5),
    ("bably",24,3.7),
    ("tanveer",25,3.25),
    ("israt",24,3.35),
    ("anik",25,3.67)
    )

sorted_students = sorted(students, key=lambda student:student[2])
print('sorted by grade:\n',sorted_students)
