from enum import Enum
from sshkeyboard import listen_keyboard
from gpiozero import CamJamKitRobot


class Action(Enum):
	FORWARD = 'w'
	LEFT = 'a'
	RIGHT = 'd'
	BACK = 's'


action = None


robot = CamJamKitRobot()


def on_press(key):
	global action
	global robot
	try:
		if key == 'w':
			action = Action.FORWARD
			robot.forward()
		elif key == 'a':
			action = Action.LEFT
			robot.left()
		elif key == 'd':
			action = Action.RIGHT
			robot.right()
		elif key == 's':
			action = Action.BACK
			robot.backward()
		else:
			action = None

	except Exception:
		action = None


def on_release(key):
	global action
	global robot

	robot.stop()
	action = None


listen_keyboard(
	on_press=on_press,
	on_release=on_release,
	delay_second_char=0.05
)
