import pytest

from S01_week03.shapes import Rectangle


# @pytest.fixture(autouse=True)
# def reset_rectangle_count():
#     Rectangle.count = 0
#     yield


def test___init__():
    # Rectangle.count = 0
    r1 = Rectangle(10, 10)
    expected_id = 1
    actual_id = r1.id

    assert actual_id == expected_id


def test___init___multiple_rectangles():
    # Rectangle.count = 0
    r1 = Rectangle(10, 10)
    r2 = Rectangle(4, 6)
    r3 = Rectangle(10, 11)
    expected_id = 3
    actual_id = r3.id

    assert actual_id == expected_id


def test_calc_area_int():
    # Rectangle.count = 0
    r1 = Rectangle(3, 4)
    expected_area = 3*4

    actual_area = r1.calc_area()

    assert actual_area == expected_area


def test_calc_area_int_one_negative():
    # Rectangle.count = 0
    r1 = Rectangle(-2, 4)
    expected_area = -2 * 4

    actual_area = r1.calc_area()

    assert actual_area == expected_area


def test_calc_area_int_two_negatives():
    # Rectangle.count = 0
    r1 = Rectangle(-2, -6)
    expected_area = -2 * -6

    actual_area = r1.calc_area()

    assert actual_area == expected_area


def test_calc_area_float():
    # Rectangle.count = 0
    r1 = Rectangle(3.5, 4.7)
    expected_area = 3.5*4.7

    actual_area = r1.calc_area()

    assert actual_area == expected_area


def test_calc_area_float_one_negative():
    # Rectangle.count = 0
    r1 = Rectangle(-3.5, 4.7)
    expected_area = -3.5*4.7

    actual_area = r1.calc_area()

    assert actual_area == expected_area


def test_calc_area_float_two_negatives():
    # Rectangle.count = 0
    r1 = Rectangle(-3.5, -7.2)
    expected_area = -3.5*-7.2

    actual_area = r1.calc_area()

    assert actual_area == expected_area


def test_calc_area_mixed_params():
    # Rectangle.count = 0
    r1 = Rectangle(5, -7.2)
    expected_area = 5*-7.2

    actual_area = r1.calc_area()

    assert actual_area == expected_area


# todo: Run __init__ tests and try to work out why they fail
# todo: Uncomment line changing Rectangle count and rerun tests - why do they work now?
# todo: Write tests for set_colour
