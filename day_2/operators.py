age=28
height=172.52
complex_num=5+3j

#Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base=float(input("Enter the base of the triangle:"))
height=float(input("Enter the height of the triangle:"))
area_of_triangle=0.5*base*height
print("The area of the triangle is",area_of_triangle)

#Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length=float(input("Enter the length of the rectangle:"))
width=float(input("Enter the width of the rectangle:"))
area_of_rectangle=length*width
print("The area of the rectangle is",area_of_rectangle)

perimeter_of_rectangle=2*(length+width)
print("The perimeter of the rectangle is", perimeter_of_rectangle)