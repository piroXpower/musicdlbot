import os
import asyncio
from pyrogram import Client, filters, idle
from pyrogram.types import Message

SESSION = ""
api_id='21364355'
api_hash="72f11aec1dd3e5764554d477341a3d0b"

app = Client(SESSION, api_id, api_hash)


ALPHABET = {'𝓐', '𝓑', '𝓒', '𝓓', '𝓔', '𝓕', '𝓖', '𝓗', '𝓘', '𝓚', '𝓛', '𝓜', '𝓝',  '𝓟', '𝓠', '𝓡', '𝓢', '𝓣', '𝓤',  '𝓦', '𝓧', '𝓨', '𝓩', '𝙰', '𝙱', '𝙲', '𝙳', '𝙴', '𝙵', '𝙶', '𝙷', '𝙸', '𝙹', '𝙺', '𝙻', '𝙼', '𝙽', '𝙿', '𝚁', '𝚂', '𝚃', '𝚄', '𝚅', '𝚆', '𝚇', '𝚈', '𝚉', 'ꋬ', 'ꃳ', 'ꉔ', '꒯', 'ꏂ', 'ꊰ', 'ꍌ', 'ꁝ', '꒐', '꒻', 'ꀘ', '꒒', 'ꂵ', 'ꋊ', 'ꄲ', 'ꉣ', 'ꆰ', 'ꋪ', 'ꇙ', '꓄', '꒤', '꒦', 'ꅐ', 'ꉧ', 'ꌦ', 'ꁴ​', '𝘼', '𝘽', '𝘾', '𝘿', '𝙀', '𝙁', '𝙂', '𝙃', '𝙄', '𝙅', '𝙆', '𝙇', '𝙈', '𝙉', '𝙊', '𝙋', '𝙌', '𝙍', '𝙎', '𝙏', '𝙐', '𝙑', '𝙒', '𝙓', '𝙔', '𝙕', '₳', '฿', '₵', 'Đ', 'Ɇ', '₣', '₲', 'Ⱨ', '₭', 'Ⱡ', '₥', '₦', 'Ø', '₱', '₴', '₮', 'Ʉ', '₩', 'Ӿ', 'Ɏ', 'Ⱬ', '𝔸', '𝔹', 'ℂ', '𝔻', '𝔼', '𝔽', '𝔾', 'ℍ', '𝕀',  '𝕂', '𝕃', '𝕄', 'ℕ', '𝕆', 'ℙ', 'ℝ', '𝕊', '𝕋', '𝕌', '𝕎', '𝕏', '𝕐', 'ℤ', 'ል', 'ጌ', 'ር', 'ዕ', 'ቿ', 'ቻ', 'ኗ', 'ዘ', 'ጎ', 'ጋ', 'ጕ', 'ረ', 'ጠ', 'ክ', 'ዐ', 'የ', 'ዒ', 'ዪ', 'ነ', 'ፕ', 'ሁ', 'ሀ', 'ሠ', 'ሸ', 'ሃ', 'ጊ', 'ɐ', 'ɔ', 'ǝ', 'ɟ', 'ƃ', 'ɥ', 'ı', 'ɾ', 'ʞ', 'ן', 'ɯ', 'ɹ', 'ʇ', 'ʌ', 'ʍ', 'ʎ', '🄰', '🄱', '🄲', '🄳', '🄴', '🄵', '🄶', '🄷', '🄸', '🄺', '🄻', '🄼', '🄽', '🄾', '🄿', '🅁', '🅂', '🅃', '🅄', '🅆', '🅇', '🅈', '🅉', 'ᴀ', 'ʙ', 'ᴄ', 'ᴅ', 'ᴇ', 'ғ', 'ɢ', 'ʜ', 'ɪ', 'ᴊ', 'ᴋ', 'ʟ', 'ᴍ', 'ɴ', '𝕬', '𝕭', '𝕮', '𝕯', '𝕰', '𝕱', '𝕲', '𝕳', '𝕴', '𝕵', '𝕶', '𝕷', '𝕸', '𝕹', '𝕺', '𝕻', '𝕼', '𝕽', '𝕾', '𝕿', '𝖀', '𝖁', '𝖂', '𝖃', '𝖄', '𝖅','ᴘ', 'ǫ','𝘈', '𝘉', '𝘊', '𝘋', '𝘌', '𝘍', '𝘎', '𝘏', '𝘐', '𝘒', '𝘓', '𝘔', '𝘕', '𝘖', '𝘗', '𝘙', '𝘚', '𝘛', '𝘜', '𝘞', '𝘟', '𝘠', '𝘡', '₳', '฿', '₵', 'Đ', 'Ɇ', '₣', '₲', 'Ⱨ',  'Ⱡ', '₥', '₦', 'Ø', '₱', 'Ɽ', '₴', '₮',  '₩', 'Ӿ', 'Ɏ', 'Ⱬ', 'Ⓐ', 'Ⓑ', 'Ⓒ', 'Ⓓ', 'Ⓔ', 'Ⓕ', 'Ⓖ', 'Ⓗ', 'Ⓘ', 'Ⓚ', 'Ⓛ', 'Ⓜ', 'Ⓝ', 'Ⓞ', 'Ⓟ', 'Ⓡ', 'Ⓢ', 'Ⓣ', 'Ⓤ',  'Ⓦ', 'Ⓧ', 'Ⓨ', 'Ⓩ', '𝔄', '𝔅', 'ℭ', '𝔇', '𝔈', '𝔉', '𝔊', 'ℌ', 'ℑ', '𝔍', '𝔎', '𝔏', '𝔐', '𝔑', '𝔒', '𝔓', '𝔔', 'ℜ', '𝔖', '𝔗', '𝔘', '𝔙', '𝔚', '𝔛', '𝔜', 'ℨ', 'Ａ', 'Ｂ', 'Ｃ', 'Ｄ', 'Ｅ', 'Ｆ', 'Ｇ', 'Ｈ', 'Ｉ', 'Ｋ', 'Ｌ', 'Ｍ', 'Ｎ', 'Ｏ', 'Ｐ', 'Ｒ', 'Ｓ', 'Ｔ', 'Ｕ',  'Ｗ', 'Ｘ', 'Ｙ', 'Ｚ', '🅐', '🅑', '🅒', '🅓', '🅔', '🅕', '🅖', '🅗', '🅘', '🅙', '🅚', '🅛', '🅜', '🅝', '🅞', '🅟', '🅠', '🅡', '🅢', '🅣', '🅤', '🅥', '🅦', '🅧', '🅨', '🅩', '🅰', '🅱', '🅲', '🅳', '🅴', '🅵', '🅶', '🅷', '🅸', '🅹', '🅺', '🅻', '🅼', '🅽', '🅾', '🅿', '🆀', '🆁', '🆂', '🆃', '🆄', '🆅', '🆆', '🆇', '🆈', '🆉', '𝗔', '𝗕', '𝗖', '𝗗', '𝗘', '𝗙', '𝗚', '𝗛', '𝗜', '𝗝', '𝗞', '𝗟', '𝗠', '𝗡', '𝗢', '𝗣', '𝗤', '𝗥', '𝗦', '𝗧', '𝗨', '𝗩', '𝗪', '𝗫', '𝗬', '𝗭', 'Ꭿ', 'Ᏸ', 'Ꮸ', 'Ꭰ', 'Ꭼ', 'Ꮀ', 'Ꮆ', 'Ꮋ', 'Ꭸ', 'Ꮰ', 'Ꮶ', 'Ꮭ', 'Ꮇ', 'Ꮑ', 'Ꮎ', 'Ꮲ', 'Ꮕ', 'Ꮢ', 'Ꮥ', 'Ꮏ', 'Ꮼ', 'Ꮙ', 'Ꮿ', 'Ꮂ', 'Ꮍ', 'Ꮓ', '𝐀', '𝐁', '𝐂', '𝐃', '𝐄', '𝐅', '𝐆', '𝐇', '𝐈', '𝐉', '𝐊', '𝐋', '𝐌', '𝐍', '𝐎', '𝐏', '𝐐', '𝐑', '𝐒', '𝐓', '𝐔', '𝐕', '𝐖', '𝐗', '𝐘', '𝐙', '🇦‌', '🇪‌','🇮','🇦‌🇱‌🇱‌🇪‌🇳‌ 🇨‌🇱‌🇦‌🇸‌🇸‌🇷‌🇴‌🇴‌🇲‌🇪‌🇨‌🇹‌🇮‌🇴‌🇳‌-🇦‌','🇸‌🇮‌🇴‌', '𝙖', '𝙗', '𝙘', '𝙙', '𝙚', '𝙛', '𝙜', '𝙝', '𝙞', '𝙟', '𝙠', '𝙡', '𝙢', '𝙣', '𝙤', '𝙥', '𝙦', '𝙧', '𝙨', '𝙩', '𝙪', '𝙫', '𝙬', '𝙭', '𝙮', '𝙯', '𝗮', '𝗯', '𝗰', '𝗱', '𝗲', '𝗳', '𝗴', '𝗵', '𝗶', '𝗷', '𝗸', '𝗹', '𝗺', '𝗻', '𝗼', '𝗽', '𝗾', '𝗿', '𝘀', '𝘁', '𝘂', '𝘃', '𝘄', '𝘅', '𝘆', '𝘇'}

def contains_font(text):
    # Check if the message contains non-ASCII characters (indicating it's a font)
    return any(char in ALPHABET for char in text)

@app.on_message(filters.text & filters.group & ~filters.bot)
def fonts(_, message:Message):
    if contains_font(message.text):
        sendee = message.from_user.id
        chatname = message.chat.title
        message.reply(f'{sendee} sending font in ` {chatname} ')
        message.delete()

app.start()
print('App Started') 
idle()
