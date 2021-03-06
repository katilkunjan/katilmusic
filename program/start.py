import asyncio

from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_USERNAME,
    UPDATES_CHANNEL,
)
from driver.decorators import check_blacklist
from program import __version__
from driver.core import bot, me_bot, me_user
from driver.filters import command, other_filters
from driver.database.dbchat import add_served_chat, is_served_chat
from driver.database.dbpunish import is_gbanned_user
from driver.database.dbusers import add_served_user
from driver.database.dblockchat import blacklisted_chats
from pyrogram import Client, filters, __version__ as pyrover
from pyrogram.errors import FloodWait, MessageNotModified
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ChatJoinRequest

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
@check_blacklist()
async def start_(c: Client, message: Message):
    BOT_NAME = me_bot.first_name
    await message.reply_text(
        f"""β¨ **Welcome {message.from_user.mention()} !**\n
π­ [β° δΊγπππππγδΊ MUSIC β±](https://t.me/katil_vc_player_bot) **ALLOWS YOU TO PLAY MUSIC AND VIDEO ON GROUPS THROUGH THE NEW TELEGRAM's VOICE CHATS!**

π‘ **Find out all the Bot's commands and how they work by clicking on the Β» π Commands button!**

π **To know how to use this bot, please click on the Β» β Basic Guide button!**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "β APNE GROUP ME ADD KRE β",
                        url=f"https://t.me/katil_vc_player_bot?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("β Basic Guide", callback_data="user_guide")],
                [
                    InlineKeyboardButton("π COMMANDS", callback_data="command_list"),
                    InlineKeyboardButton("ΰΌβ[β’δΊγπππππγδΊβ’]β", url=f"https://t.me/TERA_BAAP_KATIL"),
                ],
                [
                    InlineKeyboardButton(
                        "βΖ¬Κα΄οΈ»β¦β€βπ»πΎοΈππ΄ππ πΏοΈπΎοΈπΈπ½πββ€β¦οΈ»γ", url=f"https://t.me/FULL_MASTI_CLUBS"
                    ),
                    InlineKeyboardButton(
                        "π£HEART BROKEN π PERSON", url=f"https://t.me/heartbrokenperson1"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "π€ ASSISTANT", url=f"https://t.me/KATIL_ASSISTANT"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(
    command(["alive", f"alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
@check_blacklist()
async def alive(c: Client, message: Message):
    chat_id = message.chat.id
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    BOT_NAME = me_bot.first_name
    
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("βΖ¬Κα΄οΈ»β¦β€βπ»πΎοΈππ΄ππ πΏοΈπΎοΈπΈπ½πββ€β¦οΈ»γ", url=f"https://t.me/FULL_MASTI_CLUBS"),
                InlineKeyboardButton(
                    "HEART BROKEN π PERSON", url=f"https://t.me/heartbrokenperson1"
                ),
            ]
        ]
    )

    alive = f"**Hello {message.from_user.mention()}, i'm {BOT_NAME}**\n\nπ§πΌβπ» My Master: [{ALIVE_NAME}](https://t.me/{OWNER_USERNAME})\nπΎ Bot Version: `v{__version__}`\nπ₯ Pyrogram Version: `{pyrover}`\nπ Python Version: `{__python_version__}`\nβ¨ PyTgCalls Version: `{pytover.__version__}`\nπ Uptime Status: `{uptime}`\n\nβ€ **Thanks for Adding me here, for playing video & music on your Group's video chat**"

    await c.send_photo(
        chat_id,
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
@check_blacklist()
async def ping_pong(c: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("π `PONG!!`\n" f"β‘οΈ `{delta_ping * 1000:.3f} ms`")


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@check_blacklist()
async def get_uptime(c: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "π€ bot status:\n"
        f"β’ **uptime:** `{uptime}`\n"
        f"β’ **start time:** `{START_TIME_ISO}`"
    )


@Client.on_chat_join_request()
async def approve_join_chat(c: Client, m: ChatJoinRequest):
    if not m.from_user:
        return
    try:
        await c.approve_chat_join_request(m.chat.id, m.from_user.id)
    except FloodWait as e:
        await asyncio.sleep(e.x + 2)
        await c.approve_chat_join_request(m.chat.id, m.from_user.id)


@Client.on_message(filters.new_chat_members)
async def new_chat(c: Client, m: Message):
    chat_id = m.chat.id
    if await is_served_chat(chat_id):
        pass
    else:
        await add_served_chat(chat_id)
    ass_uname = me_user.username
    bot_id = me_bot.id
    for member in m.new_chat_members:
        if chat_id in await blacklisted_chats():
            await m.reply(
                "βοΈ This chat has blacklisted by sudo user and You're not allowed to use me in this chat."
            )
            return await bot.leave_chat(chat_id)
        if member.id == bot_id:
            return await m.reply(
                "β€οΈ Thanks for adding me to the **Group** !\n\n"
                "Appoint me as administrator in the **Group**, otherwise I will not be able to work properly, and don't forget to type `/userbotjoin` for invite the assistant.\n\n"
                "Once done, then type `/reload`",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("HEART BROKEN π PERSON", url=f"https://t.me/heartbrokenperson1"),
                            InlineKeyboardButton("βΖ¬Κα΄οΈ»β¦β€βπ»πΎοΈππ΄ππ πΏοΈπΎοΈπΈπ½πββ€β¦οΈ»γ", url=f"https://t.me/FULL_MASTI_CLUBS")
                        ],
                        [
                            InlineKeyboardButton("π€ ASSISTANT", url="https://t.me/KATIL_ASSISTANT")
                        ]
                    ]
                )
            )


chat_watcher_group = 10

@Client.on_message(group=chat_watcher_group)
async def chat_watcher_func(_, message: Message):
    if message.from_user:
        user_id = message.from_user.id
        await add_served_user(user_id)
        return
    try:
        userid = message.from_user.id
    except Exception:
        return
    suspect = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    if await is_gbanned_user(userid):
        try:
            await message.chat.ban_member(userid)
        except Exception:
            return
        await message.reply_text(
            f"π?πΌ (> {suspect} <)\n\n**Gbanned** user detected, that user has been gbanned by sudo user and was blocked from this Chat !\n\nπ« **Reason:** potential spammer and abuser."
        )
