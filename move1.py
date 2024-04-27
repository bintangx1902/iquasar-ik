import threading
from math import *

from adafruit_servokit import ServoKit

pca = ServoKit(channels=16)

# leg parameter
coxa = 21.15
femur = 19.6535
tibia = 40.025

# ground clearance
gc = 39.538

# final coordinate
x = 48
y = 0
z = 2

dtb = 1023 // 300


def inverse_kinematics(x, y, z, arm):
    D = sqrt(x ** 2 + z ** 2)
    d = D - coxa
    teta1 = degrees(atan(z / x))
    y_offset = gc - y
    R = sqrt(d ** 2 + y_offset ** 2)
    a1 = degrees(acos(y_offset / R))
    p1 = (femur ** 2) + (R ** 2) - (tibia ** 2)
    x1 = p1 / (2 * femur * R)
    a2 = degrees(acos(x1))
    teta2 = a1 + a2
    teta3 = degrees(acos((p1) / (2 * femur * tibia)))

    arm_cases = {
        # servo arm default angle = 150 degree
        'arm1': lambda:
        (
            (150 + teta1) * dtb,
            (150 + teta2) * dtb,
            (150 + teta3) * dtb
        ),

        'arm2': lambda:
        (
            (150 - teta1) * dtb,
            (150 - teta2) * dtb,
            (150 - teta3) * dtb
        ),

        'arm3': lambda:
        (
            (150 - teta1) * dtb,
            (150 - teta2) * dtb,
            (150 - teta3) * dtb
        ),

        'arm4': lambda:
        (
            (150 + teta1) * dtb,
            (150 + teta2) * dtb,
            (150 + teta3) * dtb
        )

    }
    ateta1, ateta2, ateta3 = arm_cases.get(arm, lambda: (None, None, None))()
    return ateta1, ateta2, ateta3


def move_1cm():


def set_servo(pin, angle):
    pca.servo[pin].angle = angle


def movement(pin: list, x, y, z):
    """
    :param pin: must be array with maximum length is 6 | the pin is attached pin to the PCA9685 board for cross feet
    :param x: must be array with maxium length is 2 | x1 for the front and x2 for rear (cross)
    :param y: must be same like x
    :param z: must be same like y
    :return: function return nothing but it moves the servo
    """
    th = []
    teta = []

    for a, b, c in zip(x, y, z):
        t1, t2, t3 = inverse_kinematics(a, b, c)
        teta.append(t1)
        teta.append(t2)
        teta.append(t3)

    for i in pin:
        thread = threading.Thread(target=set_servo, args=(i, teta[i]))
        th.append(thread)
        thread.start()

    for i in th:
        i.join()
