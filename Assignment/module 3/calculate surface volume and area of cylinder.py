import math

radius=float(input("enter radius of cylinder:"))
height=float(input("enter height of  cylinder:"))

surface_area = 2*math.pi *radius*(radius+height)
volume=math.pi*radius**2*height

print(f"the surface area of thr cylinder is:{surface_area}")
print(f"the volume of thr cylinder is:{volume}")
