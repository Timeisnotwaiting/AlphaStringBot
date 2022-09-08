from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

_TEXT_1 = """Welcome to Alpha Pyrogram String Session Generator.


You can procees with bot's api values if you want , else you can proceed with your api values

Bot has over 100+ API ID and HASH Saved , You can use them. 


Press Button to start generating session!"""

_MARKUP_1 = [
            [InlineKeyboardButton("🔗 Generate String with your API", callback_data="WITH_API")
            ],
            [InlineKeyboardButton("🔗 Generate String with Bot's API", callback_data="WITHOUT_API")
            ]
            ]
