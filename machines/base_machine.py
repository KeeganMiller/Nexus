from pyray import *
from enum import Enum

class BaseMachine:
    def __init__(self, users: list):
        self.users: list = users if len(users) > 0 else BaseMachine.generate_users()
        self.machine_state: MachineState = MachineState.LOCKED
        self.machine_logs: list = []
        

    # Logs a user acount in
    def login(self, uname: str, pword: str):
        for user in self.users:
            if uname == user.username:
                if pword == user.password:
                    self.machine_state = MachineState.ACTIVE
                    self.machine_logs.append(MachineLog(ip='TODO', user=uname, date='TODO', time='TODO', note='User has logged in'))
                    return 'Success'
                else:
                    self.machine_logs.append(MachineLog(ip='TODO', user=uname, date='TODO', time='TODO', note='Incorrect password'))
                    return 'Incorrect password'
            else:
                self.machine_logs.append(MachineLog(
                    ip='TODO', user=uname, date='TODO', time='TODO', note=f'Login attempt failed with username:{uname}'))
                return 'User does not exist'
            
    def logout(self, shutdown: bool = False):
        
        
        

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

class MachineLog:
    def __init__(self, ip: str, user: str, date: str, time: str, note: str):
        self._ip = ip
        self._date = date
        self._time = time
        self._note = note

    def get_detailed_note(self):
        return f'{self._ip}#{self._user}: - {self._note}\n {self._date}#{self._time}'
    
    def get_note(self):
        return f'{self._ip} - {self._note}'

