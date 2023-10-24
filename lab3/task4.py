def calculate_ring_area(outer_radius, inner_radius):
    if outer_radius <= 0 or inner_radius <= 0 or inner_radius >= outer_radius:
        return "Некорректные значения радиусов"

    ring_area = 3.14159 * (outer_radius ** 2 - inner_radius ** 2)
    return ring_area


outer_radius = 10
inner_radius = 5
result = calculate_ring_area(outer_radius, inner_radius)
print(f"Площадь кольца = {result}")
