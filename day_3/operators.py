# age=28
# height=172.52
# complex_num=5+3j

# #Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
# base=float(input("Enter the base of the triangle:"))
# height=float(input("Enter the height of the triangle:"))
# area_of_triangle=0.5*base*height
# print("The area of the triangle is",area_of_triangle)

# #Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
# length=float(input("Enter the length of the rectangle:"))
# width=float(input("Enter the width of the rectangle:"))
# area_of_rectangle=length*width
# print("The area of the rectangle is",area_of_rectangle)

# perimeter_of_rectangle=2*(length+width)
# print("The perimeter of the rectangle is", perimeter_of_rectangle)

# #Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
# radius=float(input("Enter the radius of the circle:"))
# area_of_circle=3.14*radius*radius
# print("the area of the circle is",area_of_circle)

# circumference_of_circle=2*3.14*radius
# print("The circumference of the circle is",circumference_of_circle)

#Calculate the slope, x-intercept and y-intercept of y = 2x -2
x=input("Enter the value of x:")
y=2*float(x)-2
print("the value of y is",y)

#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1=2
y1=2
x2=6
y2=10
slope=(y2-y1)/(x2-x1)
print(slope)

#Compare the slopes in tasks 8 and 9.
slope1=2
slope2=slope

print(slope1==slope2)
print(slope1>slope2)
print(slope1<slope2)
print(slope1<=slope2)
print(slope1>=slope2)
print(slope1!=slope2)
