#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math


def average(a: float, b: float, c: float) -> float:
    return (a + c + b) / 3



def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    angle_min
    return 0.0


def to_degrees(angle_rads: float) -> tuple:
   degree = (angle_rads * 180) / math.pi
   portion_dec = degree % 1
   minutes = portion_dec * 60
   portion_dec2 = minutes % 1
   secondes = portion_dec2 * 60
   degree = int(degree)
   minutes = int (minutes)
   return degree, minutes, secondes


def to_celsius(temperature: float) -> float:
    return (temperature - 32) / 1.8


def to_farenheit(temperature: float) -> float:
    return (temperature * 1.8) + 32



def main() -> None:
    print(f"Moyenne des nombres 2, 4, 6: {average(2.1, 4.3, 6.5)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
