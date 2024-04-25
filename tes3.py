import time
from adafruit_servokit import ServoKit

# Initialize the servo kit with the default address (0x40) for PCA9685
kit = ServoKit(channels=16)

# Function to set angle for a servo
def set_angle(channel, angle):
    pulse = int(500 + (angle / 180) * 2000)
    kit.servo[channel].throttle = pulse

# Set angles for all servos simultaneously
def set_angles(angles):
    for channel, angle in enumerate(angles):
        set_angle(channel, angle)

# Example of setting angles simultaneously for three servos attached to channels 0, 1, and 2
def control_servos(angles):
    for angle, servo_channel in zip(angles, [0, 1, 2]):  # Channels 0, 1, and 2
        set_angle(servo_channel, angle)

# Example angles for three servos
angles = [135, 90, 140]  # Example angles, adjust as needed
print (angles)
control_servos(angles)


# Delay to hold the position for some time
time.sleep(1)