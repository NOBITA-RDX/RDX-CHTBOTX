from pyrogram.types import InlineKeyboardButton

from config import SUPPORT_GRP, UPDATE_CHNL
from Mickey import OWNER
from Mickey import MickeyBot

DEV_OP = [
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ ᴜʜʜ ʙᴀʙʏ",
            url=f"https://t.me/{MickeyBot.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴍᴅs", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="💜", url="https://t.me/+GEooO-YpKXlhNjA1"),
        InlineKeyboardButton(text="💙", callback_data="ABOUT"),
        InlineKeyboardButton(text="𓆩🖤𓆪", user_id="1777270311"),
        InlineKeyboardButton(text="💚", url="https://t.me/+xWcg-WBN1oBjMjk1"),
        InlineKeyboardButton(text="💛", url="https://youtube.com/@LofiBoyraj"),
    ],
]

PNG_BTN = [
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ ᴜʜʜ ʙᴀʙʏ",
            url=f"https://t.me/{MickeyBot.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(
            text="✯ 𝐂ʟᴏsᴇ ✯",
            callback_data="CLOSE",
        ),
    ],
]


BACK = [
    [
        InlineKeyboardButton(text="✯ 𝐁ᴀᴄᴋ ✯", callback_data="BACK"),
    ],
]


HELP_BTN = [
    [
        InlineKeyboardButton(text="✯ 𝐂ʜᴀᴛʙᴏᴛ ✯", callback_data="CHATBOT_CMD"),
        InlineKeyboardButton(text="✯ 𝐓ᴏᴏʟs ✯", callback_data="TOOLS_DATA"),
    ],
    [
        InlineKeyboardButton(text="✯ 𝐁ᴀᴄᴋ ✯", callback_data="BACK"),
        InlineKeyboardButton(text="✯ 𝐂ʟᴏsᴇ ✯", callback_data="CLOSE"),
    ],
]


CLOSE_BTN = [
    [
        InlineKeyboardButton(text="✯ 𝐂ʟᴏsᴇ ✯", callback_data="CLOSE"),
    ],
]


CHATBOT_ON = [
    [
        InlineKeyboardButton(text="𝐄ɴᴀʙʟᴇ", callback_data=f"addchat"),
        InlineKeyboardButton(text="𝐃ɪsᴀʙʟᴇ", callback_data=f"rmchat"),
    ],
]


MUSIC_BACK_BTN = [
    [
        InlineKeyboardButton(text="✯𝐒ᴏᴏᴍ✯", callback_data=f"soom"),
    ],
]

S_BACK = [
    [
        InlineKeyboardButton(text="✯ 𝐁ᴀᴄᴋ ✯", callback_data="SBACK"),
        InlineKeyboardButton(text="✯ 𝐂ʟᴏsᴇ ✯", callback_data="CLOSE"),
    ],
]


CHATBOT_BACK = [
    [
        InlineKeyboardButton(text="✯ 𝐁ᴀᴄᴋ ✯", callback_data="CHATBOT_BACK"),
        InlineKeyboardButton(text="✯ 𝐂ʟᴏsᴇ ✯", callback_data="CLOSE"),
    ],
]


HELP_START = [
    [
        InlineKeyboardButton(text="✯ 𝐇ᴇʟᴘ ✯", callback_data="HELP"),
        InlineKeyboardButton(text="✯ 𝐂ʟᴏsᴇ ✯", callback_data="CLOSE"),
    ],
]


HELP_BUTN = [
    [
        InlineKeyboardButton(
            text="✯ 𝐇ᴇʟᴘ ✯", url=f"https://t.me/{MickeyBot.username}?start=help"
        ),
        InlineKeyboardButton(text="✯ 𝐂ʟᴏsᴇ ✯", callback_data="CLOSE"),
    ],
]


ABOUT_BTN = [
    [
        InlineKeyboardButton(text="💙", url="https://t.me/+xWcg-WBN1oBjMjk1"),
        InlineKeyboardButton(text="💜", callback_data="HELP"),
        InlineKeyboardButton(text="𓆩🖤𓆪", user_id="1777270311"),
        InlineKeyboardButton(text="💚", url="https://t.me/+FTpq6AVRnqMwZDRl"),
        InlineKeyboardButton(text="🧡", url="https://t.me/+GEooO-YpKXlhNjA1",
        ),
    ],
    [
        InlineKeyboardButton(text="✯ 𝐁ᴀᴄᴋ ✯", callback_data="BACK"),
    ],
]
