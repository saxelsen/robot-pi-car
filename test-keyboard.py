from enum import Enum
from sshkeyboard import listen_keyboard
import time


class Action(Enum):
	FORWARD = 'w'
	LEFT = 'a'
	RIGHT = 'd'
	BACK = 's'


action = None
start = 0
end = 0


def on_press(key):
	print(f'pressed {key}')

	global action
	global start
	try:
		if key == 'w':
			action = Action.FORWARD
		elif key == 'a':
			action = Action.LEFT
		elif key == 'd':
			action = Action.RIGHT
		elif key == 's':
			action = Action.BACK
		else:
			action = None

	except Exception:
		action = None

	start = time.time()


def on_release(key):
	global action
	global start
	global end

	action = None
	end = time.time()
	elapsed = end - start
	print(f'released {key} after {elapsed:.2f}s')


listen_keyboard(
	on_press=on_press,
	on_release=on_release,
	delay_second_char=0.05
)
