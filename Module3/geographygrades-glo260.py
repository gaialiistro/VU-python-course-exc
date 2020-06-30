""" assignment: Geography Grades 1
    created on 9 nov. 2019
    author: Gaia Liistro """


def report_geography(input_student):
    students_info = input_student.split("_")
    name = students_info[0]
    grades = students_info[len(students_info) - 1].split()
    if len(grades) == 3:
        a = float(grades[0])
        b = float(grades[1])
        c = float(grades[2])
        average_grade = (a + b + c) / 3
    else:
        average_grade = 1
    print "%s has an average grade of %.1f" % (name, average_grade)


input_grades = open('grades1.in.txt').readlines()

print "Report for group 2b"
x = 0
for i in input_grades:
    report_geography(input_grades[x])
    x += 1
print "End of report."
