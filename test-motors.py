from gpiozero import CamJamKitRobot
import time

robot = CamJamKitRobot()

# turn motors on
robot.forward()

time.sleep(1)

# turn motors off
robot.stop()