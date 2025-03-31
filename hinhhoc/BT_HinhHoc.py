'Xây dựng các lớp đối tượng'
import math

# Câu 1: Xây dựng các Class
class Shape:
    #hàm khởi tạo (Constructor)
    def __init__(self, name):
        self.name = name
    #phương thức tính diện tích
    def GetArea(self):
        return
#lớp kế thừa hình chữ nhật
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def GetArea(self):
        return self.width * self.height
    #phương thức in ra kết quả
    def __str__(self):
        return f"Rectangle - Width: {self.width} - Height: {self.height} - Area: {self.GetArea()}"

#lớp kế thừa hình vuông
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side,side)

    def __str__(self):
        return f"Square - Side: {self.width}, Area: {self.GetArea()}"

#lớp kế thừa hình tròn
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def GetArea(self):
        return math.pi *  self.radius ** 2

    def __str__(self):
        return f"Circle - Radius: {self.radius} - Area: {self.GetArea():.2f}"

#lớp kế thừa hình tam giác
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def GetArea(self):
        #công thức heron
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def __str__(self):
        return f"Triangle - Sides: {self.a}, {self.b}, {self.c} - Area: {self.GetArea():.2f}"

# Câu 2: Tạo 1 danh sách n hình vẽ thuộc các loại khác nhau (n > 5)
shapes = [
    Rectangle(5,10),
    Rectangle(8,13),
    Square(5),
    Circle(10),
    Triangle(6, 8, 10),  # Tam giác vuông
    Triangle(7, 7, 7)  # Tam giác đều
]

# Câu 3. In thông tin từng hình vẽ theo: loại, diện tích
print("\nDanh sách các hình vẽ:")
for shape in shapes:
    print(shape)

# Câu 4. Đếm số lượng mỗi loại
shape_counts = {"Rectangle": 0, "Square": 0, "Circle": 0, "Triangle": 0}
for shape in shapes:
    shape_counts[type(shape).__name__] += 1

print("\nSố lượng từng loại hình vẽ:")
for shape, count in shape_counts.items():
    print(f"{shape}: {count}")

# Câu 5. Tính diện tích hình vẽ lớn nhất
max_area = max(shape.GetArea() for shape in shapes)
print(f"\nDiện tích lớn nhất trong danh sách: {max_area:.2f}")

# Câu 6. Tìm hình có diện tích lớn nhất theo từng loại
largest_shapes = {}

for shape in shapes:
    shape_type = type(shape).__name__
    if shape_type not in largest_shapes or shape.GetArea() > largest_shapes[shape_type].GetArea():
        largest_shapes[shape_type] = shape

print("\nHình vẽ có diện tích lớn nhất theo từng loại:")
for shape_type, shape in largest_shapes.items():
    print(shape)