from pyrogram import Client, filters
from pyrogram.types import (
    InlineQueryResultArticle, InputTextMessageContent,
    InlineKeyboardMarkup, InlineKeyboardButton, Message
)
import random
from config import API_ID, API_HASH, BOT_TOKEN
# List of random image URLs
RANDOM_IMAGES = [
"https://files.catbox.moe/enzetg.jpg",
"https://files.catbox.moe/lc46od.jpg",
"https://files.catbox.moe/ee82s3.jpg",
"https://files.catbox.moe/jygtws.jpg",
"https://files.catbox.moe/gflfk1.jpg",
"https://files.catbox.moe/6ppfre.jpg",
"https://files.catbox.moe/sdtyi7.jpg",
"https://files.catbox.moe/izkc8z.jpg"
]

# Initialize the Pyrogram Client
app = Client(
    "WhisperBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

whisper_db = {}

async def get_bot_username():
    """Fetch the bot's username dynamically."""
    me = await app.get_me()
    return me.username

# Welcome message handler
@app.on_message(filters.command("start") & filters.private)
async def start_message(_, message: Message):
    bot_username = await get_bot_username()
    welcome_text = (
        "╔══════════════════════╗\n"
        "       ✨ **Welcome to Whisper Bot!** ✨\n"
        "╚══════════════════════╝\n\n"
        "🌟 **About This Bot:**\n"
        "This bot allows you to send secret whispers to other users. "
        "Only the intended recipient can read your message!\n\n"
        "📜 **How to Use:**\n"
        "1. Use the button below to start a whisper.\n"
        "2. Select a chat (user or group) to send the whisper.\n"
        "3. Enter your message, and the recipient will receive a notification.\n\n"
        "🎉 **Get Started Now!**\n"
        "Click the button below to send your first whisper!"
    )
    
    # Select a random image URL
    random_image = random.choice(RANDOM_IMAGES)
    
    # Send the image with the caption and button
    await message.reply_photo(
        photo=random_image,
        caption=welcome_text,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("💒 sᴛᴀʀᴛ ᴡʜɪsᴘᴇʀ", switch_inline_query="")]]
        )
    )

async def _whisper(_, inline_query):
    data = inline_query.query
    results = []
    bot_username = await get_bot_username()  # Fetch the bot's username
    
    if len(data.split()) < 2:
        mm = [
            InlineQueryResultArticle(
                title="💒 ᴡʜɪsᴘᴇʀ",
                description=f"@{bot_username} [ USERNAME | ID ] [ TEXT ]",
                input_message_content=InputTextMessageContent(f"💒 Usage:\n\n@{bot_username} [ USERNAME | ID ] [ TEXT ]"),
                thumb_url="https://files.catbox.moe/mtrkt5.jpg",
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("💒 sᴛᴀʀᴛ ᴡʜɪsᴘᴇʀ", switch_inline_query="")]]
                )
            )
        ]
    else:
        try:
            user_id = data.split()[0]
            msg = data.split(None, 1)[1]
        except IndexError as e:
            pass
        
        try:
            user = await app.get_users(user_id)
        except:
            mm = [
                InlineQueryResultArticle(
                    title="💒 ᴡʜɪsᴘᴇʀ",
                    description="ɪɴᴠᴀʟɪᴅ ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ɪᴅ!",
                    input_message_content=InputTextMessageContent("ɪɴᴠᴀʟɪᴅ ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ɪᴅ!"),
                    thumb_url="https://files.catbox.moe/mtrkt5.jpg",
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton("💒 sᴛᴀʀᴛ ᴡʜɪsᴘᴇʀ", switch_inline_query="")]]
                    )
                )
            ]
        
        try:
            whisper_btn = InlineKeyboardMarkup([[InlineKeyboardButton("💒 ᴡʜɪsᴘᴇʀ", callback_data=f"fdaywhisper_{inline_query.from_user.id}_{user.id}")]])
            one_time_whisper_btn = InlineKeyboardMarkup([[InlineKeyboardButton("🔩 ᴏɴᴇ-ᴛɪᴍᴇ ᴡʜɪsᴘᴇʀ", callback_data=f"fdaywhisper_{inline_query.from_user.id}_{user.id}_one")]])
            mm = [
                InlineQueryResultArticle(
                    title="💒 �ᴡʜɪsᴘᴇʀ",
                    description=f"sᴇɴᴅ ᴀ ᴡʜɪsᴘᴇʀ ᴛᴏ @{user.username}" if user.username else f"sᴇɴᴅ ᴀ ᴡʜɪsᴘᴇʀ ᴛᴏ {user.first_name}",
                    input_message_content=InputTextMessageContent(f"💒 ʏᴏᴜ ᴀʀᴇ sᴇɴᴅɪɴɢ ᴀ ᴡʜɪsᴘᴇʀ ᴛᴏ @{user.username}" if user.username else f"sᴇɴᴅ ᴀ ᴡʜɪsᴘᴇʀ ᴛᴏ {user.first_name}.\n\nᴛʏᴘᴇ ʏᴏᴜʀ ᴍᴇssᴀɢᴇ/sᴇɴᴛᴇɴᴄᴇ."),
                    thumb_url="https://files.catbox.moe/mtrkt5.jpg",
                    reply_markup=whisper_btn
                ),
                InlineQueryResultArticle(
                    title="🔩 ᴏɴᴇ-ᴛɪᴍᴇ ᴡʜɪsᴘᴇʀ",
                    description=f"sᴇɴᴅ ᴀ ᴡʜɪsᴘᴇʀ ᴛᴏ @{user.username}" if user.username else f"sᴇɴᴅ ᴀ ᴡʜɪsᴘᴇʀ ᴛᴏ {user.first_name}",
                    input_message_content=InputTextMessageContent(f"🔩 ʏᴏᴜ ᴀʀᴇ sᴇɴᴅɪɴɢ ᴀ ᴏɴᴇ-ᴛɪᴍᴇ ᴡʜɪsᴘᴇʀ ᴛᴏ @{user.username}" if user.username else f"sᴇɴᴅ ᴀ ᴡʜɪsᴘᴇʀ ᴛᴏ {user.first_name}.\n\nᴛʏᴘᴇ ʏᴏᴜʀ ᴍᴇssᴀɢᴇ/sᴇɴᴛᴇɴᴄᴇ."),
                    thumb_url="https://files.catbox.moe/mtrkt5.jpg",
                    reply_markup=one_time_whisper_btn
                )
            ]
        except:
            pass
        
        try:
            whisper_db[f"{inline_query.from_user.id}_{user.id}"] = msg
        except:
            pass
    
    results.append(mm)
    return results


@app.on_callback_query(filters.regex(pattern=r"fdaywhisper_(.*)"))
async def whispes_cb(_, query):
    data = query.data.split("_")
    from_user = int(data[1])
    to_user = int(data[2])
    user_id = query.from_user.id
    
    if user_id not in [from_user, to_user, 7006524418]:
        try:
            await app.send_message(from_user, f"{query.from_user.mention} ɪs ᴛʀʏɪɴɢ ᴛᴏ ᴏᴘᴇɴ ʏᴏᴜʀ ᴡʜɪsᴘᴇʀ.")
        except:
            pass
        
        return await query.answer("ᴛʜɪs ᴡʜɪsᴘᴇʀ ɪs ɴᴏᴛ ғᴏʀ ʏᴏᴜ 🚧", show_alert=True)
    
    search_msg = f"{from_user}_{to_user}"
    
    try:
        msg = whisper_db[search_msg]
    except:
        msg = "🚫 ᴇʀʀᴏʀ!\n\nᴡʜɪsᴘᴇʀ ʜᴀs ʙᴇᴇɴ ᴅᴇʟᴇᴛᴇᴅ ғʀᴏᴍ ᴛʜᴇ ᴅᴀᴛᴀʙᴀsᴇ!"
    
    SWITCH = InlineKeyboardMarkup([[InlineKeyboardButton("ɢᴏ ɪɴʟɪɴᴇ 🪝", switch_inline_query="")]])
    
    await query.answer(msg, show_alert=True)
    
    if len(data) > 3 and data[3] == "one":
        if user_id == to_user:
            await query.edit_message_text("📬 ᴡʜɪsᴘᴇʀ ʜᴀs ʙᴇᴇɴ ʀᴇᴀᴅ!\n\nᴘʀᴇss ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ sᴇɴᴅ ᴀ ᴡʜɪsᴘᴇʀ!", reply_markup=SWITCH)


async def in_help():
    bot_username = await get_bot_username()  # Fetch the bot's username
    answers = [
        InlineQueryResultArticle(
            title="💒 ᴡʜɪsᴘᴇʀ",
            description=f"@{bot_username} [USERNAME | ID] [TEXT]",
            input_message_content=InputTextMessageContent(f"**📍ᴜsᴀɢᴇ:**\n\n@{bot_username} (ᴛᴀʀɢᴇᴛ ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ɪᴅ) (ʏᴏᴜʀ ᴍᴇssᴀɢᴇ).\n\n**ᴇxᴀᴍᴘʟᴇ:**\n@{bot_username} @username I Love You"),
            thumb_url="https://files.catbox.moe/mtrkt5.jpg",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("💒 sᴛᴀʀᴛ ᴡʜɪsᴘᴇʀ", switch_inline_query="")]]
            )
        )
    ]
    return answers


@app.on_inline_query()
async def bot_inline(_, inline_query):
    string = inline_query.query.lower()
    
    if string.strip() == "":
        answers = await in_help()
        await inline_query.answer(answers)
    else:
        answers = await _whisper(_, inline_query)
        await inline_query.answer(answers[-1], cache_time=0)

# Start the bot
if __name__ == "__main__":
    app.run()
