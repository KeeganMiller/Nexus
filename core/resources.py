from pyray import *
from core.object import Object

class Resources:

    _objects: list = []
    
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