from aiogram.fsm.state import StatesGroup, State


class CreateStates(StatesGroup):
    title = State()
    body = State()
    deadline = State()
    category = State()
    confirm = State()
