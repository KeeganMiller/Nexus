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
        self._parent: Object = None
        self._children: list = []
        

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
        if self._parent != None:
            self.position = vector2_add(self.parent.position, self.local_position)
            self.scale = vector2_add(self.parent.scale, self.local_scale)
            self.rotation = self.parent.rotation + self.local_rotation
        else:
            self.position = self.local_position
            self.scale = self.local_scale
            self.rotation = self.local_rotation

    def set_parent(self, parent: 'Object'):
        # Remove this object as a child from the current parent
        if self._parent != None:
            self._parent.remove_child(child=self)

        self._parent = parent               # Set the new parent object
        if(self._parent != None):
            self._parent.add_child(child=self)

    def add_child(self, child: 'Object'):
        if not child in self._children:
            self._children.append(child)

    def remove_child(self, child: 'Object'):
        if child in self._children:
            self._children.remove(child)
        
    
class TextureObject(Object):
    def __init__(self, name: str, texture: Texture2D, tint: Color = WHITE):
        super().__init__(name)
        self.texture = texture
        self.tint = tint

    def draw(self):
        super().draw()
        if not self.texture == None and self.texture.id > 0:
            draw_texture_ex(self.texture, self.position, self.rotation, self.scale)