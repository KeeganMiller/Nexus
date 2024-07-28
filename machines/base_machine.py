from pyray import *

class BaseMachine:
    def __init__(self, users: list):
        if(len(users) == 0):
            # TODO: Generate random user accounts
            pass
        else:
            self.users: list = users

    

class UserAccount:
    def __init__(self, username: str, password: str, super_user: bool):
        self.username: str = username
        self.password: str = password
        self.super_user: bool = super_user
