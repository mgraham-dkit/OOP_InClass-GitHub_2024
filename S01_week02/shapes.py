class Rectangle:
    def __init__(self, length, width, colour):
        self.length = length
        self.width = width
        self.colour = colour

    def display(self):
        print(f"Rectangle[length={self.length}, width={self.width}, colour={self.colour}")

    def calc_area(self):
        area = self.length * self.width
        return area
