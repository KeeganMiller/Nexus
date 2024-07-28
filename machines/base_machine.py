from pyray import *
from enum import Enum

class BaseMachine:
    def __init__(self, users: list):
        self.users: list = users if len(users) > 0 else BaseMachine.generate_users()
        self.machine_state: MachineState = MachineState.LOCKED

    # Logs a user acount in
    def login(self, uname: str, pword: str):
        for user in self.users:
            if uname == user.username:
                if pword == user.password:
                    self.machine_state = MachineState.ACTIVE
                    return 'Success'
                else:
                    return 'Incorrect password'
            else:
                return 'User does not exist'
            

        

    @staticmethod
    def generate_users():
        return [UserAccount(username='Test', password='Test', super_user=True)]
    

class MachineState(Enum):
    POWERED_OFF = 1
    LOCKED = 2
    ACTIVE = 3

class UserAccount:
    def __init__(self, username: str, password: str, super_user: bool):
        self.username: str = username
        self.password: str = password
        self.super_user: bool = super_user
