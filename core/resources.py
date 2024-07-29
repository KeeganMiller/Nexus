from pyray import *
from core.object import Object

class Resources:

    _objects: list = []
    _textures: list = []
    
    @staticmethod
    def update(dt: float):
        for obj in Resources._objects:
            obj.update(dt=dt)
    
    @staticmethod
    def draw():
        for obj in Resources._objects:
            obj.draw()

    @staticmethod
    def add_object(obj: Object):
        if not obj in Resources._objects:
            Resources._objects.append(obj)
            obj.start()
            
    @staticmethod
    def remove_object(obj: Object):
        if obj in Resources._objects:
            Resources._objects.remove(obj)
            obj.destroy()

    @staticmethod
    def get_texture(name: str, path: str = ''):
        if not path == '':
            for t in Resources._textures:
                if t.path == path:
                    return t.texture
            else:
                texture = load_texture(path)
                if texture.id > 0:
                    textureObj = TextureStorage(name=name, path=path, texture=texture)
                    Resources._textures.append(textureObj)
        else:
            for t in Resources._texture:
                if t.name == name:
                    return t.texture
        print(f'Failed to find or load texture')



class TextureStorage:
    def __init__(self, name: str, path: str, texture: str):
        self.name = name
        self.path: str = path
        self.texture: Texture2D = texture