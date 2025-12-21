from aiogram import Router

from .read import read_router
from .create import create_router
from .update import update_router


router = Router()
router.include_routers(read_router, create_router, update_router)
