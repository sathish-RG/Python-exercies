#Day 2: 30 Days of python programming

First_name="sathish"
Last_name="R"
Full_name=First_name+Last_name
Contry="India"
City="Chennai"
Age=28
year=2026
is_married=False
is_True=True
is_light_on=False

# Age, Year, Height=28, 2026, 172

print(type(First_name))
print(type(Last_name))
print(type(Age))
print(type(is_married))


a=len(First_name)
b=len(Last_name)

#Compare the length of your first name and your last name
print(a<b)
print(a>b)
print(a==b)
print(a!=b)

num_one=5
num_two=4

total=num_one+num_two
print (total)

diff=num_two-num_one
print(diff)

product=num_one*num_two
print(product)

division=num_one/num_two
print(division)

reminder=num_one%num_two
print(reminder)

exp=num_one**num_two
print(exp)

floor_division=num_one//num_two
print(floor_division)

# The radius of a circle is 30 meters.
#Calculate the area of a circle and assign the value to a variable name of area_of_circle
#Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
#Take radius as user input and calculate the area
r=input('Enter the radius of the circle:')
radius=int(r)
area_of_circle=3.14*radius**2
print(area_of_circle)
circum_of_circle=2*3.14*radius
print(circum_of_circle)


#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
First_name=input("Enter your first name:")
Last_name=input("Enter your last name:")
Country=input("Enter your country:")
Age=input("Enter your age:")

print(First_name)
print(Last_name)
print(Country)
print(Age)

#Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help("keywords")