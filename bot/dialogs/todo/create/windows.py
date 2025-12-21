from aiogram_dialog import Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Button, Column
from aiogram_dialog.widgets.text import Const

from .states import CreateStates
from .handlers import title_handler, body_handler, deadline_handler, primary_handler, secondary_handler, confirm_create_handler

title_window = Window(
    Const("Enter title: "),
    TextInput(id="title", on_success=title_handler),
    state=CreateStates.title,
)

body_window = Window(
    Const("Enter body: "),
    TextInput(id="body", on_success=body_handler),
    state=CreateStates.body,
)

deadline_window = Window(
    Const("Enter deadline: "),
    TextInput(id="deadline", on_success=deadline_handler),
    state=CreateStates.deadline,
)

category_window = Window(
    Const("Enter category: "),
        Button(Const("Primary"), id="primary", on_click=primary_handler),
        Button(Const("Secondary"), id="secondary", on_click=secondary_handler),
    state=CreateStates.category,
)

confirm_window = Window(
    Const("Confirm create task"),
    Button(Const("Confirm"), id="confirm_tasks", on_click=confirm_create_handler),
    state=CreateStates.confirm,
)
