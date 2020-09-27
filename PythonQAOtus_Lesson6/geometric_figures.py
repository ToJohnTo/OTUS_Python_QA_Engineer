import math


class GeometricFigure(object):

    name = ""
    angles = -1
    perimeter = -1
    area = -1

    def _put_name(self, name):
        self.name = name

    def _put_angles(self, angles):
        self.angles = angles

    def _put_perimeter(self, perimeter):
        self.perimeter = perimeter

    def _put_area(self, area):
        self.area = area

    def __get_name(self):
        return self.name

    def __get_angles(self):
        return self.angles

    def __get_perimeter(self):
        return self.perimeter

    def __get_area(self):
        return self.area

    def add_square(self, other):
        if isinstance(other, GeometricFigure):
            self.area += other.area
            return 1
        else:
            print(f"Передан неправильный класс")
            return 0

    def show_info(self):
        info = "Название фигуры => %s" % self.__get_name() + "\n" +\
               "Количество углов => %s" % self.__get_angles() + "\n" +\
               "Периметр фигуры => %s" % self.__get_perimeter() + "\n" +\
               "Площадь фигуры => %s" % self.__get_area() + "\n"
        return info


class Triangle(GeometricFigure):

    def __init__(self, side_a, side_b, side_c):
        """Class constructor"""
        self._put_name("Triangle")
        self._put_angles(3)
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

        perimeter = side_a + side_b + side_c
        self._put_perimeter(perimeter)

        area = math.sqrt((perimeter/2) * ((perimeter/2) - side_a) * ((perimeter/2) - side_b) * ((perimeter/2) - side_c))
        self._put_area(area)


class Rectangle(GeometricFigure):

    def __init__(self, side_a, side_b):
        """Class constructor"""
        self._put_name("Rectangle")
        self._put_angles(4)
        self.side_a = side_a
        self.side_b = side_b

        perimeter = 2 * (side_a + side_b)
        self._put_perimeter(perimeter)

        area = side_a * side_b
        self._put_area(area)


class Square(GeometricFigure):

    def __init__(self, side_a):
        """Class constructor"""
        self._put_name("Square")
        self._put_angles(4)
        self.side_a = side_a

        perimeter = 4 * side_a
        self._put_perimeter(perimeter)

        area = side_a * side_a
        self._put_area(area)


class Circle(GeometricFigure):

    def __init__(self, radius):
        """Class constructor"""
        self._put_name("Circle")
        self._put_angles(0)
        self.radius = radius

        perimeter = 2 * math.pi * radius
        self._put_perimeter(perimeter)

        area = math.pi * math.pi * radius
        self._put_area(area)
