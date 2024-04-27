from math import *

# from adafruit_servokit import ServoKit
#
# pca = ServoKit(channels=16)

# pca = ServoKit(channels=16)
# pin = 0

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


def inverse_kinematics(x, y, z, arm: str):
    d = sqrt(x ** 2 + z ** 2) - coxa
    theta1 = degrees(atan(x / z))
    y_offset = gc - y
    R = sqrt(d ** 2 + y_offset ** 2)
    a1 = degrees(acos(y_offset / R))
    p1 = (femur ** 2) + (R ** 2) - (tibia ** 2)
    x1 = p1 / (2 * femur * R)
    a2 = degrees(acos(x1))
    theta2 = a1 + a2
    theta3 = degrees(acos((p1) / (2 * femur * tibia)))

    conversion = {
        'arm1': [
            (150 + theta1) * dtb,
            (150 + theta2) * dtb,
            (150 + theta3) * dtb,
        ],
        'arm2': [
            (150 - theta1) * dtb,
            (150 - theta2) * dtb,
            (150 - theta3) * dtb,
        ],
        'arm3': [
            (150 - theta1) * dtb,
            (150 - theta2) * dtb,
            (150 - theta3) * dtb,
        ],
        'arm4': [
            (150 + theta1) * dtb,
            (150 + theta2) * dtb,
            (150 + theta3) * dtb,
        ],
    }
    theta1, theta2, theta3 = conversion.get(arm)
    return theta1, theta2, theta3


# def set_servo(pin, angle):
#     pca.servo[pin].angle = angle

def unpack_t(arr):
    # Extracting columns
    columns = [list(col) for col in zip(*arr)]
    return columns[0], columns[1], columns[2], columns[3]


def movement(pin, x, y, z, arm):
    """
    :param pin: must be array with maximum length is 6 | the pin is attached pin to the PCA9685 board for cross feet
    :param x: must be array with maxium length is 2 | x1 for the front and x2 for rear (cross)
    :param y: must be same like x
    :param z: must be same like y
    :param arm: must be array with 1 dimension and length is dependent on if length(x == y == z)
    :return: function return None but it moves the servo
    """
    th = []
    theta = []

    for a, b, c, arm in zip(x, y, z, arm):
        t1, t2, t3 = inverse_kinematics(a, b, c, arm)
        theta.append(t1)
        theta.append(t2)
        theta.append(t3)

    print(theta)

    # for i in pin:
    #     thread = threading.Thread(target=set_servo, args=(i, theta[i]))
    #     th.append(thread)
    #     thread.start()
    #
    # for i in th:
    #     i.join()
