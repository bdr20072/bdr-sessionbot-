from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""هلو {msg.from_user.mention}🍷,

ɪ ᴀᴍ {me2},
ᴛʀᴜsᴛᴇᴅ 𝗦𝗧𝗥𝗜𝗡𝗚 𝗚𝗥𝗡𝗘𝗥𝗔𝗧𝗢𝗥 ʙᴏᴛ.
ғᴜʟʟʏ sᴀғᴇ & sᴇᴄᴜʀᴇ.
ɴᴏ ᴀɴʏ ᴇʀʀᴏʀ

𝐌𝐚𝐝𝐞 𝐁𝐲  : [Badr](tg://user?id={OWNER_ID}) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="⚡بدء الجلسه⚡", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("❣️ مساعده ❣️", url="https://t.me/Neiman_X_Support"),
                    InlineKeyboardButton("🥀 𝐎𝐟𝐟𝐢𝐜𝐞 🥀", url="https://t.me/DETECTED_09")
                ]
            ]
        ),
        disable_web_page_preview=True,
)
