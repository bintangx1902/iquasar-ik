from adafruit_servokit import ServoKit
from math import *
import math
# pca = ServoKit(channels=16)
# pin = 0
# pca.servo[pin].angle = 135
coxa = 21.15


x=48
y=0
z=2

femur = 19.6535
tibia = 40.025
gc = 39.538
D= sqrt(x**2+z**2)
d = D-coxa
teta1=degrees(atan(x/z))
yoffset=gc-y
R=sqrt(d**2+yoffset**2)
a1=degrees(acos(yoffset/R))
p1=(femur**2) + (R**2) - (tibia**2)
x1=p1/(2 * femur * R)
a2 = degrees(acos(x1))
teta2=a1+a2
teta3=degrees(acos((p1)/(2*femur*tibia)))





