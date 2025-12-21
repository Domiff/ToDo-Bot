from aiogram import Router

from .read import read_router
from .create import create_router
from .update import update_router
from .delete import delete_router


router = Router()
router.include_routers(read_router, create_router, update_router, delete_router)
