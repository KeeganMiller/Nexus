from pyray import *

init_window(800, 450, "Nexus")
while not window_should_close():
    # Update here

    # Draw Here
    begin_drawing()
    clear_background(WHITE)
    draw_text('Nexus OS', 100, 100, 32, BLACK)
    end_drawing()