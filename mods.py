from string import *
from pyrogram.errors import *
from helpers import *

async def _start(_, m):
    _start_1 = await m.reply(_TEXT_1, reply_markup=_MARKUP_1)
   
async def _without_api(_, m):
    ph_no_msg = await _.ask(_PHONE_NUMBER, filters=filters.text)
    
