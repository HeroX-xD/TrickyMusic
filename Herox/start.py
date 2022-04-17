from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from SJM.decorators import sudo_users_only
from SJM.filters import command
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_private(client: Client, message: Message):
 await message.reply_photo(
        photo=f"https://telegra.ph/file/a82f511eb98f58a685e32.jpg",
        caption=f"""ʜᴇʟʟᴏ✨ **ᴡᴇʟᴄᴏᴍᴇ {message.from_user.mention()} !**\n
 **ɪ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜsɪᴄ ɪɴ ɢʀᴏᴜᴘ ᴠɪᴅᴇᴏ ᴄᴀʟʟ !!**
 **ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴘʀᴏᴍᴏᴛᴇ 💫**
 **ғᴏʀ ᴀɴʏ ʜᴇʟᴘ ᴊᴏɪɴ @Techno_Trickop**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ 𝘼𝙙𝙙 𝙢𝙚 𝙞𝙣 𝙮𝙤𝙪𝙧 𝙂𝙧𝙥 ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton(
                    "• Cᴏᴍᴍᴀɴᴅs", callback_data="cb_cmd"),],
                [
                    InlineKeyboardButton("• Oᴡɴᴇʀ", url=f"https://t.me/{OWNER_NAME}"),
                    InlineKeyboardButton("• Dᴇᴠᴇʟᴏᴘᴇʀ ", url=f"https://t.me/herox_xd"),
                ],
                [
                    InlineKeyboardButton(
                        "• Sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "• Uᴘᴅᴀᴛᴇs", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "• Sᴏᴜʀᴄᴇ Cᴏᴅᴇ •", url="https://github.com/SJMxADITI/TrickyMusic"
                    )
                ],
            ]
        ),
    )


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def start_group(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("• Sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "• Uᴘᴅᴀᴛᴇs", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    alive = f"**Hello {message.from_user.mention()}, i'm {BOT_NAME}**\n\n✨ Bot is working normally\n🍀 My Master: [{ALIVE_NAME}](https://t.me/{OWNER_NAME})\n🍀 Pyrogram Version: `{pyrover}`\n✨ Python Version: `{__python_version__}`\n🍀 Uptime Status: `{uptime}`\n\n**𝗧𝗵𝗮𝗻𝗸𝘀 𝗳𝗼𝗿 𝗔𝗱𝗱𝗶𝗻𝗴 𝗺𝗲 𝗵𝗲𝗿𝗲, 𝗳𝗼𝗿 𝗽𝗹𝗮𝘆𝗶𝗻𝗴 𝗺𝘂𝘀𝗶𝗰 𝗼𝗻 𝘆𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽 𝘃𝗼𝗶𝗰𝗲 𝗰𝗵𝗮𝘁** ❤"

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(
    command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""✨ **Hello** {message.from_user.mention()} !
» **press the button below to read the explanation and see the list of available commands !**
⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="❓ Basic Guide", callback_data="cb_cmd")]]
        ),
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 Bot Alive #𝙃𝙚𝙧𝙤𝙭_𝙈𝙪𝙨𝙞𝙘 `PONG!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 bot status:\n"
        f"• **uptime:** `{uptime}`\n"
        f"• **start time:** `{START_TIME_ISO}`"
    )
