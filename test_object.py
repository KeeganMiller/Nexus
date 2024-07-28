from pyray import *
from core.object import Object

class TestObject(Object):
    def __init__(self, name: str):
        super().__init__(name)

    def update(self, dt: float):
        super().update(dt)
        print(f'Hello, World!')
    
    def draw(self):
        super().draw()
        draw_text('Hello, World!', 100, 100, 32, BLACK)