"""
Write a Python function that takes an angle in radians as input and returns the corresponding angle in degrees. Recall that there are pi radians in 180 degrees.

Here are some hints to help you get started:

 You can use the formula: degrees = radians * 180 / pi
 Define a function that takes an angle in radians as input
 Use the above formula to convert the angle from radians to degrees
 Return the resulting value
"""
def rad_to_degree(radian):
    pi = 3.1415
    degree = radian * (180/pi)
    return degree


deg1 = round(rad_to_degree(2),3)
print(deg1)