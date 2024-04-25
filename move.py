from adafruit_servokit import ServoKit
from math import *
import math
import threading
from adafruit_servokit import ServoKit

pca = ServoKit(channels=16)

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


def set_servo(pin, angle):
    pca.servo[pin].angle = angle


def inverse_kinematics(pin: list):
    th = []
    theta = [135, 90, 90]

    for i in pin:
        thread = threading.Thread(target=set_servo, args=(i, theta[i]))
        th.append(thread)
        thread.start()

    for i in th:
        i.join()



