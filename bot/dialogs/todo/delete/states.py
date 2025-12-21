from aiogram.fsm.state import StatesGroup, State


class DeleteStates(StatesGroup):
    choose_task = State()
    confirm = State()
