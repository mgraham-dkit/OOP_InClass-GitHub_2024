from shapes import Rectangle


def create_rectangle():
    length = int(input("Please enter the length: "))
    width = int(input("Please enter the width: "))
    choice = input("Do you want a colour? Y to add, any other key for transparent.")
    if choice.upper() is "Y":
        colour = input("Please enter the colour: ")
        rect = Rectangle(length, width, colour)
    else:
        rect = Rectangle(length, width)

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

def find_smallest(rectangles):
    if len(rectangles) > 0:
        pos = 0
        min_rect = rectangles[0]

        for i, r in enumerate(rectangles):
            if r.calc_area() < min_rect.calc_area():
                min_rect = r
                pos = i

        return i
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
    print("No rectangles found")

smallest_pos = find_smallest(rectangles)
if smallest_pos is not None:
    print(f"The smallest rectangle was found at position {smallest_pos}")
else:
    print("No rectangles found")
