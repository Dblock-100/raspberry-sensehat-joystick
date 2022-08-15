#get_events
#Returns a list of InputEvent tuples representing all events that have occurred since the last call to get_events or wait_for_event

from sense_hat import SenseHat

sense = SenseHat()
while True:
    for event in sense.stick.get_events():
        print("The joystick was {} {}".format(event.action, event.direction))
