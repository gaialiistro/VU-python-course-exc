"""assignment: Pirate
    created on 27 nov. 2019
    author: Gaia Liistro"""

#classes

class CoordinateRow:

    def __init__(self):
        self.coordinate_row = []
        self.serie1 = []
        self.serie2 = []

    def add(self, number):
        self.coordinate_row.append(number)
        return self.coordinate_row

    def weave(self):
        serie1 = self.serie1.split()
        serie2 = self.serie2.split()
        x = 0
        weave = " "
        while len(serie1) > x or len(serie2) > x:
            while len(serie1) > x and len(serie2) > x:
                weave = self.add(serie1[x])
                weave = self.add(serie2[x])
                x += 1
            if len(serie1) < len(serie2):
                weave = self.add(serie2[x])
                x += 1
            else:
                weave = self.add(serie1[x])
                x += 1
        return (weave)


class Coordinates:

    def __init__(self):
        self.coordinates = []

    def values(self):
        values = self.coordinates.split(",")
        self.value_x = values[0]
        self.value_y = values[1]
        self.value_x = str(int(self.value_x) + 1)
        print (self.value_x) + "," + (self.value_y)




#functions

def final_weave(current_weave, coordinates_row):
    final_weave = CoordinateRow()
    final_weave.serie1 = current_weave
    final_weave.serie2 = (coordinates_row)
    final_weave = final_weave.weave()
    current_weave = " ".join(final_weave)
    return current_weave

def final_coordinates(coordinates):
    final_coordinates = Coordinates()
    final_coordinates.coordinates = coordinates
    final_coordinates = final_coordinates.values()




#program

file = open('PirateInput.txt')
input = file.read()
coordinates = input.split("=")


current_weave = (coordinates[0])
x = 1
while x < len(coordinates):
    current_weave = final_weave(current_weave, coordinates[x])
    x += 1

coordinates = current_weave.split()
x = 0
for coordinate in coordinates:
    final_coordinates(coordinates[x])
    x += 1
