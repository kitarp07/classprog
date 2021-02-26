#find the area of rectangle

length = float(input ("enter the length:"))
breadth = float(input ("enter the breadth: "))

area = length*breadth
print (f'The area of rectangle is {area}')

#area of triangle
base = float(input ("enter the base: "))
height = float(input ("enter the height: "))
area = (base*height)//2
print(f'The area of triangle is {area}')

#area of circle
radius= float(input ("enter the radius of circle: "))
area = (radius**2)*(22/7)
print(f'The area of circle is {area}')
