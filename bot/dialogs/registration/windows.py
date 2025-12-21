from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Button

from .states import RegistrationState
from .handlers import confirm


confirm_window = Window(
    Const("Hello! Register in system?"),
    Button(Const("Confirm"), id="confirm", on_click=confirm),
    state=RegistrationState.confirm,
)
