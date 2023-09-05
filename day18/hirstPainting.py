# import colorgram
#
# rgb_colors = []
#
# colors = colorgram.extract("testing.jpg", 5)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors) #gets colors in listed tuple form from image

import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.penup()
tim.hideturtle()
color_list = [(10, 40, 55), (150, 62, 95), (226, 70, 115), (57, 72, 96), (127, 39, 72), (46, 19, 36), (25, 75, 95), (14, 7, 6), (249, 112, 129), (251, 121, 108), (4, 27, 25), (24, 128, 111), (15, 95, 87), (48, 54, 92), (26, 185, 154), (30, 166, 199), (49, 182, 226), (254, 130, 134), (107, 104, 177), (46, 220, 178), (137, 101, 89), (252, 137, 134), (254, 1, 97), (181, 104, 96), (159, 179, 240), (31, 246, 198), (142, 137, 88), (199, 196, 166), (248, 185, 158), (164, 196, 255)]
tim.speed("fastest")
tim.setheading(225)
tim.forward(100)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



t.Screen().exitonclick()