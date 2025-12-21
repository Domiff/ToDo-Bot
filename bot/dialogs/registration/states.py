from aiogram.filters.state import StatesGroup, State


class RegistrationState(StatesGroup):
    confirm = State()
