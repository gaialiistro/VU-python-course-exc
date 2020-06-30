input = open('BMIInput-2.txt').readlines()


class HatzelklatzerSydrome(object):
    def __init__(self, input):
        self.input = input

    BMI_row = []

    def BMI(self):
        input = self.input.split()
        self.lenght = input[3]
        self.weight = input[4]
        BMI_MIN = 18.5
        BMI_MAX = 25
        self.BMI = float(self.weight) / (float(self.lenght) ** 2)
        return self.BMI

    def add(self):
        self.BMI_row.append(self.BMI)
        return self.BMI_row

    def health(self):
        input = self.input.split()
        self.health = input[-1]
        return self.health


def average_bmi(list):
    return sum(list) / len(list)


def result(index):
    data = HatzelklatzerSydrome(input[int(index)])
    data.BMI()
    return data.add()


x = 0
for patient in input:
    list = result(x)
    x += 1
AVERAGE = average_bmi(list)
print "The average BMI of the test subjects is %.1f" % (AVERAGE)

x = 0
y = 0
z = 0
for patient in input:
    patient = HatzelklatzerSydrome(input[z])
    bmi = patient.BMI()
    health = patient.health()
    if bmi < AVERAGE and health == "Yes":
        x += 1
    elif bmi > AVERAGE and health == "Yes":
        y += 1
    z += 1

print "There are %d cases of the syndrome amongst people with a BMI >= %.1f." % (y, AVERAGE)
print "There are %d cases of the syndrome amongst people with a BMI < %.1f." % (x, AVERAGE)


#da sistemare