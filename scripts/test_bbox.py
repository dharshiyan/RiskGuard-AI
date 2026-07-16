from src.common import BoundingBox


bbox = BoundingBox(
    x1=100,
    y1=200,
    x2=300,
    y2=500,
)

print(f"Width  : {bbox.width}")
print(f"Height : {bbox.height}")
print(f"Area   : {bbox.area}")
print(f"Center : {bbox.center}")