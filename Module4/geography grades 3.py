""" assignment: Geography Grades 3
    created on 18 nov. 2019
    author: Gaia Liistro """


def round_grade(grade):
    multiple = 0.5
    final_grade = grade + multiple / 2
    final_grade -= final_grade % 0.5
    return final_grade


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
    final_grade = round_grade(average_grade)
    if final_grade == 5.5:
        final_grade = 6.0

    print "%s has a final grade of %.1f" % (name, final_grade)


input_groups = open('grades3.in.txt').read()

groups = input_groups.split('\n=\n')
y = 0
for i in groups:
    input_grades = groups[y].split("\n")
    group_name = input_grades[0]
    y += 1
    print "Report for group %s" % group_name
    x = 1
    for i in input_grades:
        while x < len(input_grades):
            report_geography(input_grades[x])
            x += 1
    print "End of report\n" \
          " "
