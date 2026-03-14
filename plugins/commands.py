import os
from config import Config
from .fonts import Fonts
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(filters.command('start'))
async def start(c, m):
    owner = await c.get_users(int(Config.OWNER_ID))
    owner_username = owner.username if owner.username else 'riz4d'

    # Welcome text
    text = f"""<b>🙋 ʜᴇʟʟᴏ {m.from_user.mention(style='md')},</b>  
<b>🧑🏻‍💻 ɪ’ᴍ ʏᴏᴜʀ ᴘᴇʀsᴏηᴀʟ sᴛʏʟɪsʜ ᴛᴇxᴛ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ.</b>  

<blockquote expandable>
<b>- ✨ ᴛᴜʀη ʏᴏᴜʀ ᴘʟᴀɪη ᴛᴇxᴛ ɪɴᴛᴏ ᴄᴏᴏʟ sᴛʏʟɪsʜ ꜰᴏɴᴛs</b>  
<b>- 💫 ɢᴇɴᴇʀᴀᴛᴇ ꜰᴀɴᴄʏ sʏᴍʙᴏʟs ᴧηᴅ ᴅᴇcᴏʀᴀᴛɪᴏηs</b>  
<b>- 🎨 ᴍᴀᴋᴇ ʏᴏᴜʀ ᴍᴇssᴀɢᴇs ʟᴏᴏᴋ ᴜɴɪqᴜᴇ & ᴇʏᴇ-cᴀᴛᴄʜɪηɢ</b>
</blockquote>  
<blockquote expandable>
<b>ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ:</b>  
<b>1. ᴊᴜsᴛ ᴛʏᴘᴇ ᴀηʏ ᴛᴇxᴛ ʏᴏᴜ ᴡᴀηᴛ ᴛᴏ sᴛʏʟᴇ.</b>  
<b>2. ᴄʜᴏᴏsᴇ ʏᴏᴜʀ ꜰᴀᴠᴏʀɪᴛᴇ sᴛʏʟᴇ ꜰʀᴏᴍ ᴛʜᴇ ʟɪsᴛ.</b>  
<b>3. ᴄᴏᴘʏ & sᴇηᴅ ɪᴛ ᴀɴʏᴡʜᴇʀᴇ — ᴛᴇʟᴇɢʀᴀᴍ, ɪɴsᴛᴀɢʀᴀᴍ, ᴡʜᴀᴛsᴀᴘᴘ, ʏᴏᴜ ɴᴀᴍᴇ ɪᴛ!</b>  

<b>sᴘᴇᴄɪᴀʟ ꜰᴇᴀᴛᴜʀᴇs:</b>  
<b>- ᴍᴜʟᴛɪᴘʟᴇ sᴛʏʟɪsʜ ꜰᴏɴᴛ ᴏᴘᴛɪᴏηs 🅐🅑🅒</b>  
<b>- ꜰᴀɴᴄʏ ᴇᴍᴏᴊɪs ᴧηᴅ sʏᴍʙᴏʟs 🎀🎉</b>  
<b>- 100% ꜰʀᴇᴇ ᴧηᴅ ᴇᴀsʏ ᴛᴏ ᴜsᴇ ✅</b>
</blockquote>
<blockquote>
<b>💬 ɪꜰ ʏᴏᴜ ʜᴀᴠᴇ ᴀηʏ qᴜᴇsᴛɪᴏηs, ꜰᴇᴇʟ ᴄʀᴇᴇ ᴛᴏ ᴄᴏηᴛᴀᴄᴛ ᴛʜᴇ ʙᴏᴛ ᴏᴡɴᴇʀ.</b>
</blockquote>
"""

    # Buttons
    buttons = [
        [InlineKeyboardButton('⌯ ᴍʏ ᴍᴧsᴛєʀ ⌯', url=f"https://t.me/CarelessxOwner")],
        [
            InlineKeyboardButton('⌯ sᴜᴘᴘσʀᴛ ⌯', url='https://t.me/CarelessxWorld'),
            InlineKeyboardButton('⌯ ᴜᴘᴅᴧᴛє ⌯', url='https://t.me/ll_CarelessxCoder_ll')
        ]
    ]

    # Send photo as spoiler first
    await m.reply_photo(
        photo='https://files.catbox.moe/q712gx.jpg',
        spoiler=True
    )

    # Send welcome text with buttons
    await m.reply_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(buttons),
        parse_mode='html'
    )



@Client.on_message(filters.private & filters.incoming & filters.text)
async def style_buttons(c, m, cb=False):
    buttons = [[
        InlineKeyboardButton('𝚃𝚢𝚙𝚎𝚠𝚛𝚒𝚝𝚎𝚛', callback_data='style+typewriter'),
        InlineKeyboardButton('𝕆𝕦𝕥𝕝𝕚𝕟𝕖', callback_data='style+outline'),
        InlineKeyboardButton('𝐒𝐞𝐫𝐢𝐟', callback_data='style+serif'),
        ],[
        InlineKeyboardButton('𝑺𝒆𝒓𝒊𝒇', callback_data='style+bold_cool'),
        InlineKeyboardButton('𝑆𝑒𝑟𝑖𝑓', callback_data='style+cool'),
        InlineKeyboardButton('Sᴍᴀʟʟ Cᴀᴘs', callback_data='style+small_cap'),
        ],[
        InlineKeyboardButton('𝓈𝒸𝓇𝒾𝓅𝓉', callback_data='style+script'),
        InlineKeyboardButton('𝓼𝓬𝓻𝓲𝓹𝓽', callback_data='style+script_bolt'),
        InlineKeyboardButton('ᵗⁱⁿʸ', callback_data='style+tiny'),
        ],[
        InlineKeyboardButton('ᑕOᗰIᑕ', callback_data='style+comic'),
        InlineKeyboardButton('𝗦𝗮𝗻𝘀', callback_data='style+sans'),
        InlineKeyboardButton('𝙎𝙖𝙣𝙨', callback_data='style+slant_sans'),
        ],[
        InlineKeyboardButton('𝘚𝘢𝘯𝘴', callback_data='style+slant'),
        InlineKeyboardButton('𝖲𝖺𝗇𝗌', callback_data='style+sim'),
         InlineKeyboardButton('Ⓒ︎Ⓘ︎Ⓡ︎Ⓒ︎Ⓛ︎Ⓔ︎Ⓢ︎', callback_data='style+circles'),
        ],[
        InlineKeyboardButton('🅒︎🅘︎🅡︎🅒︎🅛︎🅔︎🅢︎', callback_data='style+circle_dark'),
        InlineKeyboardButton('𝔊𝔬𝔱𝔥𝔦𝔠', callback_data='style+gothic'),
        InlineKeyboardButton('𝕲𝖔𝖙𝖍𝖎𝖈', callback_data='style+gothic_bolt'),
        ],[
        InlineKeyboardButton('C͜͡l͜͡o͜͡u͜͡d͜͡s͜͡', callback_data='style+cloud'),
        InlineKeyboardButton('H̆̈ă̈p̆̈p̆̈y̆̈', callback_data='style+happy'),
        InlineKeyboardButton('S̑̈ȃ̈d̑̈', callback_data='style+sad'),
        ],[
        InlineKeyboardButton('Next ➡️', callback_data="nxt")
    ]]
    if not cb:
        await m.reply_text(m.text, reply_markup=InlineKeyboardMarkup(buttons), quote=True)
    else:
        await m.answer()
        await m.message.edit_reply_markup(InlineKeyboardMarkup(buttons))


@Client.on_callback_query(filters.regex('^nxt'))
async def nxt(c, m):
    if m.data == "nxt":
        buttons = [[
            InlineKeyboardButton('🇸 🇵 🇪 🇨 🇮 🇦 🇱 ', callback_data='style+special'),
            InlineKeyboardButton('🅂🅀🅄🄰🅁🄴🅂', callback_data='style+squares'),
            InlineKeyboardButton('🆂︎🆀︎🆄︎🅰︎🆁︎🅴︎🆂︎', callback_data='style+squares_bold'),
            ],[
            InlineKeyboardButton('ꪖꪀᦔꪖꪶꪊᥴ𝓲ꪖ', callback_data='style+andalucia'),
            InlineKeyboardButton('爪卂几ᘜ卂', callback_data='style+manga'),
            InlineKeyboardButton('S̾t̾i̾n̾k̾y̾', callback_data='style+stinky'),
            ],[
            InlineKeyboardButton('B̥ͦu̥ͦb̥ͦb̥ͦl̥ͦe̥ͦs̥ͦ', callback_data='style+bubbles'),
            InlineKeyboardButton('U͟n͟d͟e͟r͟l͟i͟n͟e͟', callback_data='style+underline'),
            InlineKeyboardButton('꒒ꍏꀷꌩꌃꀎꁅ', callback_data='style+ladybug'),
            ],[
            InlineKeyboardButton('R҉a҉y҉s҉', callback_data='style+rays'),
            InlineKeyboardButton('B҈i҈r҈d҈s҈', callback_data='style+birds'),
            InlineKeyboardButton('S̸l̸a̸s̸h̸', callback_data='style+slash'),
            ],[
            InlineKeyboardButton('s⃠t⃠o⃠p⃠', callback_data='style+stop'),
            InlineKeyboardButton('S̺͆k̺͆y̺͆l̺͆i̺͆n̺͆e̺͆', callback_data='style+skyline'),
            InlineKeyboardButton('A͎r͎r͎o͎w͎s͎', callback_data='style+arrows'),
            ],[
            InlineKeyboardButton('ዪሀክቿነ', callback_data='style+qvnes'),
            InlineKeyboardButton('S̶t̶r̶i̶k̶e̶', callback_data='style+strike'),
            InlineKeyboardButton('F༙r༙o༙z༙e༙n༙', callback_data='style+frozen')
            ],[
            InlineKeyboardButton('⬅️ Back', callback_data='nxt+0')
        ]]
        await m.answer()
        await m.message.edit_reply_markup(InlineKeyboardMarkup(buttons))
    else:
        await style_buttons(c, m, cb=True)


@Client.on_callback_query(filters.regex('^style'))
async def style(c, m):
    await m.answer()
    cmd, style = m.data.split('+')

    if style == 'typewriter':
        cls = Fonts.typewriter
    if style == 'outline':
        cls = Fonts.outline
    if style == 'serif':
        cls = Fonts.serief
    if style == 'bold_cool':
        cls = Fonts.bold_cool
    if style == 'cool':
        cls = Fonts.cool
    if style == 'small_cap':
        cls = Fonts.smallcap
    if style == 'script':
        cls = Fonts.script
    if style == 'script_bolt':
        cls = Fonts.bold_script
    if style == 'tiny':
        cls = Fonts.tiny
    if style == 'comic':
        cls = Fonts.comic
    if style == 'sans':
        cls = Fonts.san
    if style == 'slant_sans':
        cls = Fonts.slant_san
    if style == 'slant':
        cls = Fonts.slant
    if style == 'sim':
        cls = Fonts.sim
    if style == 'circles':
        cls = Fonts.circles
    if style == 'circle_dark':
        cls = Fonts.dark_circle
    if style == 'gothic':
        cls = Fonts.gothic
    if style == 'gothic_bolt':
        cls = Fonts.bold_gothic
    if style == 'cloud':
        cls = Fonts.cloud
    if style == 'happy':
        cls = Fonts.happy
    if style == 'sad':
        cls = Fonts.sad
    if style == 'special':
        cls = Fonts.special
    if style == 'squares':
        cls = Fonts.square
    if style == 'squares_bold':
        cls = Fonts.dark_square
    if style == 'andalucia':
        cls = Fonts.andalucia
    if style == 'manga':
        cls = Fonts.manga
    if style == 'stinky':
        cls = Fonts.stinky
    if style == 'bubbles':
        cls = Fonts.bubbles
    if style == 'underline':
        cls = Fonts.underline
    if style == 'ladybug':
        cls = Fonts.ladybug
    if style == 'rays':
        cls = Fonts.rays
    if style == 'birds':
        cls = Fonts.birds
    if style == 'slash':
        cls = Fonts.slash
    if style == 'stop':
        cls = Fonts.stop
    if style == 'skyline':
        cls = Fonts.skyline
    if style == 'arrows':
        cls = Fonts.arrows
    if style == 'qvnes':
        cls = Fonts.rvnes
    if style == 'strike':
        cls = Fonts.strike
    if style == 'frozen':
        cls = Fonts.frozen
    new_text = cls(m.message.reply_to_message.text)
    try:
        await m.message.edit_text(new_text, reply_markup=m.message.reply_markup)
    except:
        pass
