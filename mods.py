from string import *
from pyrogram.errors import *
from helpers import *

async def _start(_, m):
    _start_1 = await m.reply(_TEXT_1, reply_markup=_MARKUP_1)
   
async def _without_api(_, m):
    ph_no_msg = await _.ask(m.chat.id, _PHONE_NUMBER, filters=filters.text)
    if await cancelled(ph_no_msg):
        return
    number = ph_no_msg.text
    ch = await _.get_chat_history(m.chat.id)
    _IDS = []
    async for ids in ch:
        _IDS.append(ids.id)
    _IDS.remove(_IDS[0])
    try:
        await _.delete_messages(m.chat.id, _IDS)
    except:
        pass
    smexy = Client(":appendable:", API_ID, API_HASH)
    smexy.connect()
    try:
        code = await smexy.send_code(number)
    except (ApiIdInvalid, ApiIdInvalidError):
        await m.reply('API ID and API HASH are invalid, pls try with your API values..!', reply_markup=_MARKUP_1)
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError):
        await m.reply('phone number is invalid, start generating session again', reply_markup=_MARKUP_1)
        return
    try:
        _otp = await _.ask(m.chat.id, _OTP, filters=filters.text)
        if await cancelled(_otp):
            return
    except TimeoutError:
        return await m.reply("Time limit reached of 10min.., start generating session again !", reply_markup=_MARKUP_1)
    OTP = _otp.text.replace(" ", "")
    ch = await _.get_chat_history(m.chat.id)
    _IDS = []
    async for ids in ch:
        _IDS.append(ids.id)
    _IDS.remove(_IDS[0])
    try:
        await _.delete_messages(m.chat.id, _IDS)
    except:
        pass
    try:
        await smexy.sign_in(number, code.phone_code_hash, OTP)
    except (PhoneCodeInvalid, PhoneCodeInvalidError):
        await msg.reply('OTP is invalid.., start generating session again..!', reply_markup=_MARKUP_1)
        return
    except (PhoneCodeExpired, PhoneCodeExpiredError):
        return await msg.reply('OTP is expired.., start generating session again..!', reply_markup=_MARKUP_1)
    except (SessionPasswordNeeded, SessionPasswordNeededError):
        _V = await _.ask(m.chat.id, _V_TEXT, filters=filters.text)
    
    
    
    
    
    
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
    
