"""assignment: Pirate
    created on 27 nov. 2019
    author: Gaia Liistro"""


# classes
class CoordinateRow:

    def __init__(self):
        self.coordinate_row = []

    def add(self, coordinate):
        self.coordinate_row.append(coordinate)

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

    def __init__(self, x, y):
        self.value_x = x
        self.value_y = y



    def values(self, coordinates):

        #values = self.coordinates.split(",")

        self.value_x = str(int(self.value_x) + 1)
        print (self.value_x) + "," + (self.value_y)


# fare funzioni di while e for


# programm

file = open('PirateInput.txt')
input = file.read()
coordinates = input.split("=")

current_weave = (coordinates[0])
x = 1
while x < len(coordinates):
    final_weave = CoordinateRow()
    final_weave.add()
    final_weave.serie1 = current_weave
    final_weave.serie2 = (coordinates[x])
    final_weave = final_weave.weave()
    current_weave = " ".join(final_weave)
    x += 1

coordinates = current_weave.split()
x = 0
for coordinate in coordinates:
    final_coordinates = Coordinates(0, 1)
    print final_coordinates.value_x
    final_coordinates.coordinates = coordinates[x]
    final_coordinates = final_coordinates.values()
    x += 1

# sistemare nomi
# serie???