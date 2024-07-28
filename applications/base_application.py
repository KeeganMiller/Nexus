from pyray import *
from core.object import Object

class BaseApplication(Object):
    def __init__(self, icon: Texture2D, name: str): 
        self.icon: Texture2D = None
        self.name = name
        
    def open(self, **kwargs):
        pass

    def run(self, **kwargs):
        pass
