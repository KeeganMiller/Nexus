from pyray import *
from applications.base_application import BaseApplication

class Terminal(BaseApplication):
    def _init__(self, icon: Texture2D, name: str):
        super().__init__(icon, name)

    def open(self, **kwargs):
        super().open(kwargs)

    def run(self, **kwargs):
        super().open(kwargs)