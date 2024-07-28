from pyray import *
from enum import Enum
from applications.terminal import Terminal

class BaseMachine:
    def __init__(self, users: list, apps: list):
        self.users: list = users if len(users) > 0 else BaseMachine.generate_users()
        self.machine_state: MachineState = MachineState.LOCKED
        self.connection_type: ConnectionType = ConnectionType.MINE
        self.machine_logs: list = []
        self.logged_in_user: UserAccount = None
        self.installed_apps: list = apps if len(apps) > 0 else BaseMachine.get_default_apps()

    # Logs a user acount in
    def login(self, uname: str, pword: str):
        for user in self.users:         # Loop through each user on the machine
            if uname == user.username:              # Check if username matches
                if pword == user.password:          # Check if password matches
                    self.machine_state = MachineState.ACTIVE            # Update the machine state
                    # Add log
                    self.machine_logs.append(MachineLog(ip='TODO', user=uname, date='TODO', time='TODO', note='User has logged in'))
                    self.logged_in_user = user          # Set the logged in user
                    return 'Success'                
                else:           # Password doesn't match username
                    # Added machine log
                    self.machine_logs.append(MachineLog(ip='TODO', user=uname, date='TODO', time='TODO', note='Incorrect password'))
                    return 'Incorrect password'   

        # User doesn't exist
        # Add the machine log  
        self.machine_logs.append(MachineLog(
            ip='TODO', user=uname, date='TODO', time='TODO', note=f'Login attempt failed with username:{uname}'))
        return 'User does not exist'
            
    # Logs the user out
    def logout(self, shutdown: bool = False):
        self.machine_logs.append(MachineLog(
            ip='TODO', user=self.logged_in_user.username, date='TODO', time='TODO', note=f'User logged out'))
        self.logged_in_user = None
        self.machine_state = MachineState.POWERED_OFF if shutdown else MachineState.LOCKED
        
        

    @staticmethod
    def generate_users():
        return [UserAccount(username='Test', password='Test', super_user=True)]

    @staticmethod
    def get_default_apps():
        return [Terminal()]
    

class MachineState(Enum):
    POWERED_OFF = 1
    LOCKED = 2
    ACTIVE = 3

class ConnectionType(Enum):
    TERMINAL = 1
    RAT = 2
    MINE = 3

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

