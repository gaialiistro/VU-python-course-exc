
input = open('BMIInput-1.txt').readlines()

class HatzelklatzerSydrome (object):
    def __init__(self, input):
        self.input = input

    def read_input(self):
        input = self.input.split()
        self.name = input[0]
        self.surname = input[1]
        self.sex = input[2]
        self.lenght = input[3]
        self.weight = input[4]

    def BMI(self):
        BMI_MIN = 18.5
        BMI_MAX = 25
        self.BMI = float(self.weight) / (float(self.lenght) ** 2)
        if BMI_MIN < self.BMI < BMI_MAX:
            self.state = "healty"
        else: self.state = "unhealty"
        return self.state

    def address(self):
        if self.sex == "M":
            self.address = "Mr."
        else: self.address = "Mrs."



def result(index):
    data = HatzelklatzerSydrome(input[int(index)])
    data.read_input()
    data.address()
    data.BMI()
    print "%s %s's BMI is %.1f and is %s" %(data.address, data.surname, data.BMI, data.state)


x = 0
for person in input:
    result(x)
    x += 1
