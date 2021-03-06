# Copyright (C) 2021 By VeezMusicProject

from driver.core import me_bot
from driver.decorators import check_blacklist
from driver.queues import QUEUE
from driver.database.dbpunish import is_gbanned_user
from pyrogram import Client, filters
from program.utils.inline import menu_markup, stream_markup
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from config import (
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_USERNAME,
    UPDATES_CHANNEL,
    SUDO_USERS,
    OWNER_ID,
)


@Client.on_callback_query(filters.regex("home_start"))
@check_blacklist()
async def start_set(_, query: CallbackQuery):
    BOT_NAME = me_bot.first_name
    await query.answer("home start")
    await query.edit_message_text(
        f"""β¨ **Welcome [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
π­ [{BOT_NAME}](https://t.me/{BOT_USERNAME}) **Is a bot to play music and video in groups, through the Telegram Group video chat!**

π‘ **Find out all the Bot's commands and how they work by clicking on the Β» π Commands button!**

π **To know how to use this bot, please click on the Β» β Basic Guide button!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(

                        "β APNE GROUP ME ADD KRE  β",

                        url=f"https://t.me/katil_vc_player_bot?startgroup=true",

                    )

                ],

                [InlineKeyboardButton("β Basic Guide", callback_data="user_guide")],

                [

                    InlineKeyboardButton("π Commands", callback_data="command_list"),

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

                        "π Source Code", url="https://t.me/heartbrokenperson1"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("quick_use"))
@check_blacklist()
async def quick_set(_, query: CallbackQuery):
    await query.answer("quick bot usage")
    await query.edit_message_text(
        f"""βΉοΈ Quick use Guide bot, please read fully !

π©π»βπΌ Β» /play - Type this with give the song title or youtube link or audio file to play Music. (Remember to don't play YouTube live stream by using this command!, because it will cause unforeseen problems.)

π©π»βπΌ Β» /vplay - Type this with give the song title or youtube link or video file to play Video. (Remember to don't play YouTube live video by using this command!, because it will cause unforeseen problems.)

π©π»βπΌ Β» /vstream - Type this with give the YouTube live stream video link or m3u8 link to play live Video. (Remember to don't play local audio/video files or non-live YouTube video by using this command!, because it will cause unforeseen problems.)

β Have questions? Contact us in [Support Group](https://t.me/{GROUP_SUPPORT}).""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="user_guide")]]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("user_guide"))
@check_blacklist()
async def guide_set(_, query: CallbackQuery):
    ass_uname = me_bot.first_name
    await query.answer("user guide")
    await query.edit_message_text(
        f"""β How to use this Bot ?, read the Guide below !

1.) First, add this bot to your Group.
2.) Then, promote this bot as administrator on the Group also give all permissions except Anonymous admin.
3.) After promoting this bot, type /reload in Group to update the admin data.
3.) Invite @{ass_uname} to your group or type /userbotjoin to invite her, unfortunately the userbot will joined by itself when you type `/play (song name)` or `/vplay (song name)`.
4.) Turn on/Start the video chat first before start to play video/music.

`- END, EVERYTHING HAS BEEN SETUP -`

π If the userbot not joined to video chat, make sure if the video chat already turned on and the userbot in the chat.

π‘ If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Β» Quick use Guide Β«", callback_data="quick_use")
                ],[
                    InlineKeyboardButton("π Go Back", callback_data="home_start")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("command_list"))
@check_blacklist()
async def commands_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    await query.answer("commands menu")
    await query.edit_message_text(
        f"""β¨ **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

Β» Check out the menu below to read the module information & see the list of available Commands !

All commands can be used with (`! / .`) handler""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("π?π»ββοΈ Admins Commands", callback_data="admin_command"),
                ],[
                    InlineKeyboardButton("π©π»βπΌ Users Commands", callback_data="user_command"),
                ],[
                    InlineKeyboardButton("Sudo Commands", callback_data="sudo_command"),
                    InlineKeyboardButton("Owner Commands", callback_data="owner_command"),
                ],[
                    InlineKeyboardButton("π Go Back", callback_data="home_start")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("user_command"))
@check_blacklist()
async def user_set(_, query: CallbackQuery):
    BOT_NAME = me_bot.first_name
    await query.answer("basic commands")
    await query.edit_message_text(
        f"""βοΈ Command list for all user.

Β» /play (song name/link) - play music on video chat
Β» /vplay (video name/link) - play video on video chat
Β» /vstream (m3u8/yt live link) - play live stream video
Β» /playlist - see the current playing song
Β» /lyric (query) - scrap the song lyric
Β» /video (query) - download video from youtube
Β» /song (query) - download song from youtube
Β» /search (query) - search a youtube video link
Β» /ping - show the bot ping status
Β» /uptime - show the bot uptime status
Β» /alive - show the bot alive info (in Group only)

β‘οΈ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("admin_command"))
@check_blacklist()
async def admin_set(_, query: CallbackQuery):
    BOT_NAME = me_bot.first_name
    await query.answer("admin commands")
    await query.edit_message_text(
        f"""βοΈ Command list for group admin.

Β» /pause - pause the current track being played
Β» /resume - play the previously paused track
Β» /skip - goes to the next track
Β» /stop - stop playback of the track and clears the queue
Β» /vmute - mute the streamer userbot on group call
Β» /vunmute - unmute the streamer userbot on group call
Β» /volume `1-200` - adjust the volume of music (userbot must be admin)
Β» /reload - reload bot and refresh the admin data
Β» /userbotjoin - invite the userbot to join group
Β» /userbotleave - order userbot to leave from group

β‘οΈ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("sudo_command"))
@check_blacklist()
async def sudo_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    BOT_NAME = me_bot.first_name
    if user_id not in SUDO_USERS:
        await query.answer("β οΈ You don't have permissions to click this button\n\nΒ» This button is reserved for sudo members of this bot.", show_alert=True)
        return
    await query.answer("sudo commands")
    await query.edit_message_text(
        f"""βοΈ Command list for sudo user.

Β» /stats - get the bot current statistic
Β» /calls - show you the list of all active group call in database
Β» /block (`chat_id`) - use this to blacklist any group from using your bot
Β» /unblock (`chat_id`) - use this to whitelist any group from using your bot
Β» /blocklist - show you the list of all blacklisted chat
Β» /speedtest - run the bot server speedtest
Β» /sysinfo - show the system information
Β» /eval - execute any code (`developer stuff`)
Β» /sh - run any command (`developer stuff`)

β‘ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("owner_command"))
@check_blacklist()
async def owner_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    BOT_NAME = me_bot.first_name
    if user_id not in OWNER_ID:
        await query.answer("β οΈ You don't have permissions to click this button\n\nΒ» This button is reserved for owner of this bot.", show_alert=True)
        return
    await query.answer("owner commands")
    await query.edit_message_text(
        f"""βοΈ Command list for bot owner.

Β» /gban (`username` or `user_id`) - for global banned people, can be used only in group
Β» /ungban (`username` or `user_id`) - for un-global banned people, can be used only in group
Β» /update - update your bot to latest version
Β» /restart - restart your bot directly
Β» /leaveall - order userbot to leave from all group
Β» /leavebot (`chat id`) - order bot to leave from the group you specify
Β» /broadcast (`message`) - send a broadcast message to all groups in bot database
Β» /broadcast_pin (`message`) - send a broadcast message to all groups in bot database with the chat pin

β‘ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("stream_menu_panel"))
@check_blacklist()
async def at_set_markup_menu(_, query: CallbackQuery):
    user_id = query.from_user.id
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("π‘ Only admin with manage video chat permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    user_id = query.message.from_user.id
    buttons = menu_markup(user_id)
    if chat_id in QUEUE:
        await query.answer("control panel opened")
        await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
    else:
        await query.answer("β nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("stream_home_panel"))
@check_blacklist()
async def is_set_home_menu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("π‘ Only admin with manage video chat permission that can tap this button !", show_alert=True)
    await query.answer("control panel closed")
    user_id = query.message.from_user.id
    buttons = stream_markup(user_id)
    await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))


@Client.on_callback_query(filters.regex("set_close"))
@check_blacklist()
async def on_close_menu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("π‘ Only admin with manage video chat permission that can tap this button !", show_alert=True)
    await query.message.delete()


@Client.on_callback_query(filters.regex("close_panel"))
@check_blacklist()
async def in_close_panel(_, query: CallbackQuery):
    await query.message.delete()
