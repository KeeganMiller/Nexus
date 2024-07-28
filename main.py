from pyray import *
from core.object import Object
from core.resources import Resources
from test_object import TestObject

init_window(800, 450, "Nexus")

Resources.add_object(obj=TestObject('Test'))

while not window_should_close():
    # Update here
    Resources.update(get_frame_time)
    # Draw Here
    begin_drawing()
    clear_background(WHITE)
    Resources.draw()
    end_drawing()


close_window()