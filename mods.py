from string import *
from pyrogram.errors import *
from helpers import *

async def _start(_, m):
    _start_1 = await m.reply(_TEXT_1, reply_markup=_MARKUP_1)
   
async def _without_api(_, m):
    ph_no_msg = await _.ask(_PHONE_NUMBER, filters=filters.text)
    if await cancelled(ph_no_msg):
        return
    number = ph_no_msg.text
    _otp = await m.reply(_OTP)
    
  async def cancelled(m):
    if "/cancel" in m.text:
        await m.reply("Cancelled the Process!", quote=True, reply_markup=_MARKUP_1)
        return True
    elif "/restart" in m.text:
        await m.reply("Restarted the Bot!", quote=True, reply_markup=_MARKUP_1)
        return True
    elif msg.text.startswith("/"): 
        await m.reply("Cancelled the generation process!", quote=True)
        return True
    else:
        return False
    
