from aiogram_dialog import Dialog

from .windows import choose_task_window, choose_field_window, title_window, body_window, deadline_window, confirm_window


update_dialog = Dialog(choose_task_window, choose_field_window, title_window, body_window, deadline_window, confirm_window)
