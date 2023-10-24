import math

def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def is_triangle(vertices):
    if len(vertices) != 3:
        return False

    side1 = distance(vertices[0], vertices[1])
    side2 = distance(vertices[1], vertices[2])
    side3 = distance(vertices[2], vertices[0])

    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        return True
    else:
        return False

def triangle_info(vertices):
    if not is_triangle(vertices):
        return "Это не треугольник."

    side1 = distance(vertices[0], vertices[1])
    side2 = distance(vertices[1], vertices[2])
    side3 = distance(vertices[2], vertices[0])

    perimeter = side1 + side2 + side3

    # Используем формулу Герона для вычисления площади треугольника
    s = perimeter / 2
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

    return f"Стороны треугольника: {side1}, {side2}, {side3}\nПериметр: {perimeter}\nПлощадь: {area}"

# Пример использования
vertices = [(0, 0), (3, 0), (0, 4)]
print(triangle_info(vertices))