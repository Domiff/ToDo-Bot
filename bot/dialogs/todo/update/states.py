from aiogram.fsm.state import StatesGroup, State


class UpdateState(StatesGroup):
    choose_task = State()
    choose_field = State()
    title = State()
    body = State()
    deadline = State()
    category = State()
    confirm = State()
