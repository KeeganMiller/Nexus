from pyray import *

class Object:
    def __init__(self, name: str):
        self.name: str = name
        self.local_position: Vector2 = Vector2(0, 0)
        self.position: Vector2 = Vector2(0, 0)
        self.local_scale: Vector2 = Vector2(1, 1)
        self.scale: Vector2 = Vector2(1, 1)
        self.local_rotation: float = 0.0
        self.rotation: float = 0.0
        self.parent: Object = None
        self.children: list = []
        

    def start(self):
        pass

    def update(self, dt: float):
       self._update_transform()

    def draw(self):
        pass

    def destroy(self):
        pass

    # Updates all the transform properties
    def _update_transform(self):
        if self.parent != None:
            self.position = vector2_add(self.parent.position, self.local_position)
            self.scale = vector2_add(self.parent.scale, self.local_scale)
            self.rotation = self.parent.rotation + self.local_rotation
        else:
            self.position = self.local_position
            self.scale = self.local_scale
            self.rotation = self.local_rotation
