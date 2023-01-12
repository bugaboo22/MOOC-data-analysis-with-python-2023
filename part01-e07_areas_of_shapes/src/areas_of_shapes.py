#!/usr/bin/env python3

import math


def main():

    while True:

        x = input('Choose a shape (triangle, rectangle, circle): ')

        if x == 'triangle':
            base = float(input('Give base of the triangle: '))
            height = float(input('Give height of the triangle: '))
            area = (height * base) * 0.5
            print(f'The area is {area}')

        elif x == 'rectangle':
            width = float(input('Give width of the rectangle: '))
            height = float(input('Give height of the rectangle: '))
            area = width * height
            print(f'The area is {area}')

        elif x == 'circle':
            radius = float(input('Give radius of the circle: '))
            area = str(math.pi * radius**2)
            print(f'The area is {area}')
        
        elif len(x) == 0:
            break

        else:
            print('Unknown shape!')
        
if __name__ == "__main__":
    main()
