"""assignment: Administration
    created on 18 nov. 2019
    author: Gaia Liistro"""


def round_grade(grade):
    multiple = 0.5
    final_grade = grade + multiple / 2
    final_grade -= final_grade % 0.5
    if final_grade % 1 == 0:
        final_grade = int(final_grade)
    if 5.5 <= grade < 6:
        final_grade = "6-"
    return final_grade



def results(input):
    students_info = input.split("_")
    name = students_info[0]
    grades = students_info[len(students_info) - 1].split()
    sum_grades = sum(map(float, grades))
    average_grade = sum_grades / len(grades)
    final_grade = round_grade(average_grade)
    print "%s has a final grade of %s" % (name, final_grade)


def graph(similarity_scores):
    graph = "     "
    x = 0
    for number in similarity_scores:
        if int(similarity_scores[x]) == 0:
            graph = graph + "_"
        elif int(similarity_scores[x]) < 20:
            graph = graph + "-"
        else:
            graph = graph + "^"
        x += 1
    print graph


def matches(students):
    matches = students.split(',')
    x = 0
    for student in matches:
        print "     " + matches[x]
        x += 1


def graph_matches(input):
    line = input.split(';')
    similarity_scores = line[0].split('=')
    graph(similarity_scores)
    if line[1] != "\n":
        matches(line[1])
    else:
        print "     No matches found\n"\


# start
text_input = open('administration.in.txt').readlines()

x = 0
for person in text_input:
    if x % 2 == 0:
        results(text_input[x])
    else:
        graph_matches(text_input[x])
    x += 1