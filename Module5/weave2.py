class NumberRow(object):

    def __init__(self):
        self.number_row = []
        self.serie1 = []
        self.serie2 = []

    def add(self, number):
        self.number_row.append(number)
        return self.number_row

    def weave(self):
        x = 0
        final_serie = " "
        for numbers in self.serie1:
            final_serie = self.add(self.serie1[x])
            final_serie = self.add(self.serie2[x])
            x += 1
        return (final_serie)



input = open('weave2input.txt').readlines()

first_row = NumberRow()
first_row.serie1 = (input[0].split())
first_row.serie2 = (input[1].split())
first_weave = first_row.weave()
print " ".join(first_weave)
second_row = NumberRow()
second_row.serie1 = first_weave
second_row.serie2 = (input[2].split())
print " ".join(second_row.weave())