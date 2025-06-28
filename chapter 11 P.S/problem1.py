#  1. Create a class (2-D vector) and use it to create another class representing a 3-D
# vector.
class vector2d :
    a=1
    print("running vector2d")
    pass

class vector3d(vector2d):
    b=5
    print("running vector3d")
    pass

print("vector2d.a   ",vector2d.a)
print("vector3d.a   ",vector3d.a)
print("vector3d.b   ",vector3d.b)
