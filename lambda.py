square=lambda a:a**2
rect=lambda l,b:l*b
triangle=lambda b,h:1/2*(b*h)
sq=int(input("Enter the side of the square:"))
print("Area of the square is",square(sq))
sq=str(input("Enter the length and width of rectangle")).split(',')
print("Area of rectangle is",rect(int(sq[0]),int(sq[1])))
sq=str(input("Enter the breadth and height of triangle")).split(',')
print("Area of triangle is",triangle(int(sq[0]),int(sq[1])))