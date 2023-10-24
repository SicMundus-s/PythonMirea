import volume
import area
import perimeter

length = 10
width = 20
height = 30

volume_result = volume.calculate_volume(length, width, height)
surface_area_result = area.calculate_surface_area(length, width, height)
perimeter_result = perimeter.calculate_perimeter(length, width, height)

print(f"Объем = {volume_result}")
print(f"Площадь = {surface_area_result}")
print(f"Периметр = {perimeter_result}")