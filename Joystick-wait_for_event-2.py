# Joystick
# InputEvent
# A tuple describing a joystick event. Contains three named parameters:
# 
# timestamp - The time at which the event occurred, as a fractional number of seconds (the same format as the built-in time function)
# 
# direction - The direction the joystick was moved, as a string ("up", "down", "left", "right", "middle")
# 
# action - The action that occurred, as a string ("pressed", "released", "held")
# 
# This tuple type is used by several joystick methods either as the return type or the type of a parameter.

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
event = sense.stick.wait_for_event()
print("The joystick was {} {}".format(event.action, event.direction))
sleep(0.1)
event = sense.stick.wait_for_event(emptybuffer=True)
print("The joystick was {} {}".format(event.action, event.direction))