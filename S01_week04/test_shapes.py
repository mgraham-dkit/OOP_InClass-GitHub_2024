import pytest

from S01_week04.shapes import Rectangle


@pytest.fixture(autouse=True)
def reset_rectangle_count():
    Rectangle.count = 0
    yield


def test___init__default_colour():
    expected_colour = "transparent"
    r1 = Rectangle(10, 10)
    expected_id = 1
    actual_id = r1.id

    assert actual_id == expected_id

    actual_colour = r1.get_colour()
    assert actual_colour == expected_colour


def test___init___multiple_rectangles_default_colour():
    expected_colour = "transparent"
    r1 = Rectangle(10, 10)
    r2 = Rectangle(4, 6)
    r3 = Rectangle(10, 11)
    expected_id = 3
    actual_id = r3.id

    assert actual_id == expected_id
    actual_colour = r3.get_colour()
    assert actual_colour == expected_colour


def test___init__valid_colour():
    expected_colour = "red"
    r1 = Rectangle(10, 10, expected_colour)
    expected_id = 1
    actual_id = r1.id

    assert actual_id == expected_id

    actual_colour = r1.get_colour()
    assert actual_colour == expected_colour


def test___init___multiple_rectangles_valid_colour():
    expected_colour = "red"

    r1 = Rectangle(10, 10)
    r2 = Rectangle(4, 6)
    r3 = Rectangle(10, 11, expected_colour)
    expected_id = 3
    actual_id = r3.id

    assert actual_id == expected_id

    actual_colour = r3.get_colour()
    assert actual_colour == expected_colour


def test_calc_area_int():
    r1 = Rectangle(3, 4)
    expected_area = 3*4

    actual_area = r1.calc_area()

    assert actual_area == expected_area


def test_calc_area_int_one_negative():
    r1 = Rectangle(-2, 4)
    expected_area = -2 * 4

    actual_area = r1.calc_area()

    assert actual_area == expected_area


def test_calc_area_int_two_negatives():
    r1 = Rectangle(-2, -6)
    expected_area = -2 * -6

    actual_area = r1.calc_area()

    assert actual_area == expected_area


def test_calc_area_float():
    r1 = Rectangle(3.5, 4.7)
    expected_area = 3.5*4.7

    actual_area = r1.calc_area()

    assert actual_area == expected_area


def test_calc_area_float_one_negative():
    r1 = Rectangle(-3.5, 4.7)
    expected_area = -3.5*4.7

    actual_area = r1.calc_area()

    assert actual_area == expected_area


def test_calc_area_float_two_negatives():
    r1 = Rectangle(-3.5, -7.2)
    expected_area = -3.5*-7.2

    actual_area = r1.calc_area()

    assert actual_area == expected_area


def test_calc_area_mixed_params():
    r1 = Rectangle(5, -7.2)
    expected_area = 5*-7.2

    actual_area = r1.calc_area()

    assert actual_area == expected_area


def test_set_colour_valid_colour():
    r1 = Rectangle(10, 10)

    expected_colour = "blue"
    r1.set_colour(expected_colour)
    actual_colour = r1.get_colour()

    assert actual_colour == expected_colour


def test_set_colour_invalid_colour():
    r1 = Rectangle(10, 10)

    expected_colour = "transparent"
    r1.set_colour("pink")
    actual_colour = r1.get_colour()

    assert actual_colour == expected_colour
