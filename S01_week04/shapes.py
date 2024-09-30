class Rectangle:
    valid_colours = ["red", "blue", "yellow", "purple", "transparent"]
    count = 0

    def __init__(self, length, width, colour="transparent"):
        self.length = length
        self.width = width
        self._colour = "transparent"

        self.set_colour(colour)

        Rectangle.count += 1
        self.id = Rectangle.count

    def display(self):
        print(f"Rectangle[id={self.id}, length={self.length}, width={self.width}, colour={self._colour}")

    def calc_area(self):
        area = self.length * self.width
        return area

    def get_colour(self):
        return self._colour

    def set_colour(self, colour):
        if colour.lower() in Rectangle.valid_colours:
            self._colour = colour
