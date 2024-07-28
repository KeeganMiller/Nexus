from pyray import *
from core.object import Object

init_window(800, 450, "Nexus")

test_object: Object = Object(name='test_object')

while not window_should_close():
    # Update here
    test_object.update(get_frame_time())
    # Draw Here
    begin_drawing()
    clear_background(WHITE)
    draw_text('Nexus OS', 100, 100, 32, BLACK)
    end_drawing()


close_window()