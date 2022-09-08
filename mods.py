from string import *
from pyrogram.errors import *
from helpers import *

async def _start(_, m):
    await m.reply(_TEXT_1, reply_markup=_MARKUP_1)
    
    
