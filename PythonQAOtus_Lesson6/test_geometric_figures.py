import pytest
from geometric_figures import GeometricFigure, Triangle, Rectangle, Square, Circle


class Test_Geometric_Figures(GeometricFigure):

    @pytest.mark.parametrize("side_a, side_b, side_c, expected_info", [
        (3, 4, 5,
         "Название фигуры => Triangle\nКоличество углов => 3\nПериметр фигуры => 12\nПлощадь фигуры => 6.0\n"),
        (13, 12, 5,
         "Название фигуры => Triangle\nКоличество углов => 3\nПериметр фигуры => 30\nПлощадь фигуры => 30.0\n"),
        (3, 4, 2,
         "Название фигуры => Triangle\nКоличество углов => 3\nПериметр фигуры => 9\nПлощадь фигуры => 2.9047375096555625\n"),
        (7, 8, 6,
         "Название фигуры => Triangle\nКоличество углов => 3\nПериметр фигуры => 21\nПлощадь фигуры => 20.33316256758894\n"),
        (7, 5, 3,
         "Название фигуры => Triangle\nКоличество углов => 3\nПериметр фигуры => 15\nПлощадь фигуры => 6.49519052838329\n")]
                             )
    def test_init_class_Triangle(self, side_a, side_b, side_c, expected_info):
        self.GF = Triangle(side_a, side_b, side_c)
        assert self.GF.show_info() == expected_info

    @pytest.mark.parametrize("side_a, side_b, expected_info", [
        (3, 4,
         "Название фигуры => Rectangle\nКоличество углов => 4\nПериметр фигуры => 14\nПлощадь фигуры => 12\n"),
        (13, 12,
         "Название фигуры => Rectangle\nКоличество углов => 4\nПериметр фигуры => 50\nПлощадь фигуры => 156\n"),
        (3, 4,
         "Название фигуры => Rectangle\nКоличество углов => 4\nПериметр фигуры => 14\nПлощадь фигуры => 12\n"),
        (7, 8,
         "Название фигуры => Rectangle\nКоличество углов => 4\nПериметр фигуры => 30\nПлощадь фигуры => 56\n"),
        (7, 5,
         "Название фигуры => Rectangle\nКоличество углов => 4\nПериметр фигуры => 24\nПлощадь фигуры => 35\n")]
                             )
    def test_init_class_Rectangle(self, side_a, side_b, expected_info):
        self.GF = Rectangle(side_a, side_b)
        assert self.GF.show_info() == expected_info

    @pytest.mark.parametrize("side_a, expected_info", [
        (3,
         "Название фигуры => Square\nКоличество углов => 4\nПериметр фигуры => 12\nПлощадь фигуры => 9\n"),
        (13,
         "Название фигуры => Square\nКоличество углов => 4\nПериметр фигуры => 52\nПлощадь фигуры => 169\n"),
        (8,
         "Название фигуры => Square\nКоличество углов => 4\nПериметр фигуры => 32\nПлощадь фигуры => 64\n"),
        (7,
         "Название фигуры => Square\nКоличество углов => 4\nПериметр фигуры => 28\nПлощадь фигуры => 49\n"),
        (4,
         "Название фигуры => Square\nКоличество углов => 4\nПериметр фигуры => 16\nПлощадь фигуры => 16\n")]
                             )
    def test_init_class_Square(self, side_a, expected_info):
        self.GF = Square(side_a)
        assert self.GF.show_info() == expected_info

    @pytest.mark.parametrize("side_a, expected_info", [
        (3,
         "Название фигуры => Circle\nКоличество углов => 0\nПериметр фигуры => 18.84955592153876\nПлощадь фигуры => 29.608813203268074\n"),
        (13,
         "Название фигуры => Circle\nКоличество углов => 0\nПериметр фигуры => 81.68140899333463\nПлощадь фигуры => 128.30485721416164\n"),
        (8,
         "Название фигуры => Circle\nКоличество углов => 0\nПериметр фигуры => 50.26548245743669\nПлощадь фигуры => 78.95683520871486\n"),
        (7,
         "Название фигуры => Circle\nКоличество углов => 0\nПериметр фигуры => 43.982297150257104\nПлощадь фигуры => 69.0872308076255\n"),
        (4,
         "Название фигуры => Circle\nКоличество углов => 0\nПериметр фигуры => 25.132741228718345\nПлощадь фигуры => 39.47841760435743\n")]
                             )
    def test_init_class_Circle(self, side_a, expected_info):
        self.GF = Circle(side_a)
        assert self.GF.show_info() == expected_info

    def test_put_name(self, fixture_names):
        self._put_name(fixture_names)
        assert self.name == fixture_names

    def test_put_angles(self, fixture_angles):
        self._put_angles(fixture_angles)
        assert self.angles == fixture_angles

    def test_put_perimeter(self, fixture_perimeter):
        self._put_perimeter(fixture_perimeter)
        assert self.perimeter == fixture_perimeter

    def test_put_area(self, fixture_area):
        self._put_area(fixture_area)
        assert self.area == fixture_area

    def test__get_name(self, fixture_names):
        self._put_name(fixture_names)
        assert self._GeometricFigure__get_name() == fixture_names

    def test__get_angles(self, fixture_angles):
        self._put_angles(fixture_angles)
        assert self._GeometricFigure__get_angles() == fixture_angles

    def test__get_perimeter(self, fixture_perimeter):
        self._put_perimeter(fixture_perimeter)
        assert self._GeometricFigure__get_perimeter() == fixture_perimeter

    def test__get_area(self, fixture_area):
        self._put_area(fixture_area)
        assert self._GeometricFigure__get_area() == fixture_area

    def test_right_add_square(self):
        self.Tr1 = Triangle(3, 4, 5)
        self.Tr2 = Triangle(13, 12, 5)
        self.Tr1.add_square(self.Tr2)
        assert self.Tr1.area == 36

    def test_not_right_add_square(self, capsys):
        self.Tr1 = Triangle(3, 4, 5)
        self.Tr1.add_square(10)
        captured = capsys.readouterr()
        assert captured.out == "Передан неправильный класс\n"
