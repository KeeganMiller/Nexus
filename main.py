from pyray import *
from core.object import Object
from core.resources import Resources
from machines.base_machine import BaseMachine, UserAccount, ConnectionType

class Main:
    home_machine = BaseMachine(users=[UserAccount(username='H4ck3r', password='Hacker', super_user=True)])
    home_machine.connection_type = ConnectionType.MINE

    def run():
        init_window(800, 450, "Nexus")

        while not window_should_close():
            # Update here
            Resources.update(get_frame_time)
            # Draw Here
            begin_drawing()
            clear_background(WHITE)
            Resources.draw()
            end_drawing()


        close_window()


Main.run()