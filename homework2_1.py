class Triangle():
    current_instance_count: int = 0

    def __new__(cls, *args, **kwargs):
        cls.current_instance_count += 1
        return super().__new__(cls)

    def __init__(self, side_a: int, side_b: int, side_c: int):
        self.side_a = self.int_validation(side_a)
        self.side_b = self.int_validation(side_b)
        self.side_c = self.int_validation(side_c)

    @staticmethod
    def int_validation(value):
        if isinstance(value, (int, float)):
            if value <= 0:
                raise ValueError("Can't be negative or Zero")
        else:
            raise ValueError("Must be an instance of int or float")

        return value

    @classmethod
    def get_current_instance_count(cls):
        return f"Current instance count is {cls.current_instance_count}"

    def __repr__(self):
        return f'Sides of a Trianle - {self.side_a}, {self.side_b}, {self.side_c}'

    def to_tuple(self):
        return self.side_a, self.side_b, self.side_c

    def perimeter(self):
        p = self.side_a + self.side_b + self.side_c
        return f'Perimeter of triangle - {p}'

    def area(self):
        s = (self.side_a + self.side_b + self.side_c) / 2
        area_ = (s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c)) ** 0.5
        return f'Area of triangle - {area_}'

    def __eq__(self, other):
        if not isinstance(other, Triangle):
            raise ValueError("not comparable")

        comparison = sorted(self.to_tuple()) == sorted(other.to_tuple())

        return comparison



triangle_1 = Triangle(5, 6, 7)
triangle_2 = Triangle(7, 5, 6)
print(triangle_1.get_current_instance_count())
print(triangle_1 == triangle_2)
print(triangle_1.area())
print(triangle_1.perimeter())

class Rectangular:

    def __init__(self, side_1, side_2, side_3):
        self.side_1 = self.number_validation(side_1)
        self.side_2 = self.number_validation(side_2)
        self.side_3 = self.number_validation(side_3)

    @staticmethod
    def number_validation(value):
        if type(value) == str:
            raise ValueError("Wrong Value")
        else:
            return value

    def __repr__(self):
        return f'Sides of a Cube - {self.side_1}, {self.side_2}, {self.side_3} '

    def to_tuple(self):
        return self.side_1, self.side_2, self.side_3

    def __eq__(self, other):
        if not isinstance(other, Rectangular):
            raise ValueError("cant compare not Rectangular objects")

        comparison = sorted(self.to_tuple()) == sorted(other.to_tuple())

        return comparison

    def __lt__(self, other):
        self_sorted = sorted(self.to_tuple())
        other_sorted = sorted(other.to_tuple())
        comparison = True
        for i in range(3):
            check = self_sorted[i] >= other_sorted[i]
            if check:
                comparison = False
                break

        return comparison


rect_1 = Rectangular(6, 5, 8)
rect_2 = Rectangular(15, 11, 18)

print(rect_1 == rect_2)
print(rect_1 < rect_2)