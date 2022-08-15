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

##Joystick wait for event##
#Blocks execution until a joystick event occurs, then returns an InputEvent representing the event that occurred.

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
event = sense.stick.wait_for_event()
print("The joystick was {} {}".format(event.action, event.direction))
sleep(0.1)
event = sense.stick.wait_for_event()
print("The joystick was {} {}".format(event.action, event.direction))

#In the above example, if you briefly push the joystick in a single direction you should see two events
#output: a pressed action and a released action. The optional emptybuffer can be used to flush any pending events before waiting for new events.
#Try the following script to see the difference: