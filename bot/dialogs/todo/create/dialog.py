from aiogram_dialog import Dialog

from .windows import title_window, body_window, deadline_window, category_window, confirm_window

create_dialog = Dialog(title_window, body_window, category_window, deadline_window, confirm_window)
