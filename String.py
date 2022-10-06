from email import utils
from Database import Library
from State import State, StateManager

library = Library()
state_manager = StateManager()

class command:
    def __init__(self, action, description):
        self.action = action;
        self.description = description;

    def __str__(self):
        return f'Введите {self.__action} для {self.__description}'

library_commands = [
    {
        'command':utils.Actions.Exit,
        'description':''

    }
]

dict1 = (
    
)

start_state = State()