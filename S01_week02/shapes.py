class Rectangle:
    valid_colours = ["red", "blue", "yellow", "purple", "transparent"]

    def __init__(self, length, width, colour="Transparent"):
        self.length = length
        self.width = width
        if colour in Rectangle.valid_colours:
            self._colour = colour

    def display(self):
        print(f"Rectangle[length={self.length}, width={self.width}, colour={self._colour}")

    def calc_area(self):
        area = self.length * self.width
        return area

    def get_colour(self):
        return self._colour

    def set_colour(self, colour):
        if colour in Rectangle.valid_colours:
            self._colour = colour
