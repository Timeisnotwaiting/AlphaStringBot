from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

_TEXT_1 = """Welcome to Alpha Pyrogram String Session Generator.


You can procees with bot's api values if you want , else you can proceed with your api values

Bot has over 100+ API ID and HASH Saved , You can use them. 


Press Button to start generating session!"""

_MARKUP_1_ = [
            [InlineKeyboardButton("🔗 Generate String with your API", callback_data="WITH_API")
            ],
            [InlineKeyboardButton("🔗 Generate String with Bot's API", callback_data="WITHOUT_API")
            ]
            ]

_MARKUP_1 = InlineKeyboardMarkup(_MARKUP_1_)

_PHONE_NUMBER = """Send me the phone number for which you want to generate string.

Remember to include country code.
Eg: +91 8854923453

Use /cancel to stop process anytime."""

_OTP = """I had sent an OTP to the number +91 9392983853 through Telegram App within 5 mins.

Please enter the OTP in the format 1 2 3 4 5 (use space between numbers)

If Bot not sending OTP then try /genstring the Bot.
Press /cancel to stop process anytime."""

_V_TEXT = """🔐 This account have two-step verification code.
Please enter your second factor authentication code within 5 mins.
Press /cancel to stop process anytime."""

_SS = """✅ Successfully Generated Session for {}.

Username : @{}


Here's a copy of string session:

{}

Thanks For using {}"""
