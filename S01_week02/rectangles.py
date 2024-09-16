from shapes import Rectangle


def create_rectangle():
    length = int(input("Please enter the length: "))
    width = int(input("Please enter the width: "))
    colour = input("Please enter the colour: ")

    rect = Rectangle(length, width, colour)

    return rect

def find_biggest(rectangles):
    if len(rectangles) > 0:
        max_rect = rectangles[0]

        for r in rectangles:
            if r.calc_area() > max_rect.calc_area():
                max_rect = r

        return max_rect
    else:
        return None


rectangles = []

for i in range(5):
    r = create_rectangle()
    rectangles.append(r)

biggest = find_biggest(rectangles)
if biggest is not None:
    biggest.display()
else:
    print("No max rectangle found")