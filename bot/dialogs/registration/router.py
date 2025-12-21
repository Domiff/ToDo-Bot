from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from .states import RegistrationState
from .dialog import register_dialog


router = Router()
router.include_router(register_dialog)


@router.message(CommandStart())
async def start(message: Message, dialog_manager: DialogManager, state: FSMContext):
    await dialog_manager.start(state=RegistrationState.confirm, mode=StartMode.RESET_STACK)
