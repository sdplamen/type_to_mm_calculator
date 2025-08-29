#  1 = 0.352778

# Convert mm to type size
def mm_to_points(mm):
    # There are 25.4 mm in an inch
    # There are 72 points in an inch
    points_per_mm = 72 / 25.4
    points = mm * points_per_mm
    return points

type_size_mm = 9 # Replace with your type size in millimeters
type_size_points = mm_to_points(type_size_mm)

print(f"{type_size_mm} mm is approximately {type_size_points:.2f} points")

# Convert type size to mm
def points_to_mm(points):
    # There are 25.4 mm in an inch
    # There are 72 points in an inch
    inches = points / 72.0
    mm = inches * 25.4
    return mm

type_size_points = 1  # Replace with your type size in points
type_size_mm = points_to_mm(type_size_points)

print(f"{type_size_points} points is approximately {type_size_mm:.2f} mm")