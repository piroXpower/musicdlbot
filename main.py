import asyncio
from pyrogram import Client, filters, idle
from pyrogram.types import Message

SESSION = ""
api_id='21364355'
api_hash="72f11aec1dd3e5764554d477341a3d0b"

app = Client(SESSION, api_id, api_hash)

#ALPHABET = {'𝕬', '𝕰', '𝕴', '𝕺', '𝖀','𝙰', '𝙴', '𝙸', '𝚄', 'ꋬ', 'ꏂ', '꒐', 'ꄲ', '꒤', '𝘼', '𝙀', '𝙄', '𝙊', '𝙐', '₳', 'Ɇ', 'Ł', 'Ø', 'Ʉ', '𝔸', '𝔼', '𝕀', '𝕆', '𝕌', 'ᗩ', 'ᘿ', 'ᓰ', 'ᓍ', 'ᑘ','ɐ', 'ǝ', 'ı', '🄰', '🄴', '🄸', '🄾', '🅄', 'ᴀ', 'ᴇ', 'ɪ', 'ᴏ', 'ᴜ', '𝕬', '𝕰', '𝕴', '𝕺', '𝖀', '𝘈', '𝘌', '𝘐', '𝘖', '𝘜', '₳', 'Ɇ', 'ł', 'Ø', 'Ʉ', 'Ⓐ', 'Ⓔ', 'Ⓘ', 'Ⓞ', 'Ⓤ', '𝔄', '𝔈', 'ℑ', '𝔒', '𝔘', 'Ａ', 'Ｅ', 'Ｉ', 'Ｏ', 'Ｕ', '🅐', '🅔', '🅘', '🅞', '🅤', '🅰', '🅴', '🅸', '🅾', '🆄', 'Α', 'Ҽ', 'Ι', 'Σ', 'Υ', '𝗔', '𝗘', '𝗜', '𝗢', '𝗨', 'α', 'є', 'ι', 'σ', 'υ', 'Ꭿ', 'Ꭼ', 'Ꭸ', 'Ꮎ', 'Ꮼ', '𝐀', '𝐄', '𝐈', '𝐎', '𝐔', 'α', 'є', 'ι', 'σ', 'υ', 'Ä', 
#ALPHABET = {'𝓐', '𝓑', '𝓒', '𝓓', '𝓔', '𝓕', '𝓖', '𝓗', '𝓘', '𝓙', '𝓚', '𝓛', '𝓜', '𝓝', '𝓞', '𝓟', '𝓠', '𝓡', '𝓢', '𝓣', '𝓤', '𝓥', '𝓦', '𝓧', '𝓨', '𝓩', '𝙰', '𝙱', '𝙲', '𝙳', '𝙴', '𝙵', '𝙶', '𝙷', '𝙸', '𝙹', '𝙺', '𝙻', '𝙼', '𝙽', '𝙿', '𝚁', '𝚂', '𝚃', '𝚄', '𝚅', '𝚆', '𝚇', '𝚈', '𝚉', 'ꋬ', 'ꃳ', 'ꉔ', '꒯', 'ꏂ', 'ꊰ', 'ꍌ', 'ꁝ', '꒐', '꒻', 'ꀘ', '꒒', 'ꂵ', 'ꋊ', 'ꄲ', 'ꉣ', 'ꆰ', 'ꋪ', 'ꇙ', '꓄', '꒤', '꒦', 'ꅐ', 'ꉧ', 'ꌦ', 'ꁴ​', '𝘼', '𝘽', '𝘾', '𝘿', '𝙀', '𝙁', '𝙂', '𝙃', '𝙄', '𝙅', '𝙆', '𝙇', '𝙈', '𝙉', '𝙊', '𝙋', '𝙌', '𝙍', '𝙎', '𝙏', '𝙐', '𝙑', '𝙒', '𝙓', '𝙔', '𝙕', '₳', '฿', '₵', 'Đ', 'Ɇ', '₣', '₲', 'Ⱨ', 'Ł', 'J', '₭', 'Ⱡ', '₥', '₦', 'Ø', '₱', 'Q', 'Ɽ', '₴', '₮', 'Ʉ', 'V', '₩', 'Ӿ', 'Ɏ', 'Ⱬ', '𝔸', '𝔹', 'ℂ', '𝔻', '𝔼', '𝔽', '𝔾', 'ℍ', '𝕀', '𝕁', '𝕂', '𝕃', '𝕄', 'ℕ', '𝕆', 'ℙ', 'ℚ', 'ℝ', '𝕊', '𝕋', '𝕌', '𝕍', '𝕎', '𝕏', '𝕐', 'ℤ', 'ል', 'ጌ', 'ር', 'ዕ', 'ቿ', 'ቻ', 'ኗ', 'ዘ', 'ጎ', 'ጋ', 'ጕ', 'ረ', 'ጠ', 'ክ', 'ዐ', 'የ', 'ዒ', 'ዪ', 'ነ', 'ፕ', 'ሁ', 'ሀ', 'ሠ', 'ሸ', 'ሃ', 'ጊ', 'ɐ', 'ɔ', 'ǝ', 'ɟ', 'ƃ', 'ɥ', 'ı', 'ɾ', 'ʞ', 'ן', 'ɯ', 'u', 'ɹ', 's', 'ʇ', 'ʌ', 'ʍ', 'x', 'ʎ', 'z','🄰', '🄱', '🄲', '🄳', '🄴', '🄵', '🄶', '🄷', '🄸', '🄹', '🄺', '🄻', '🄼', '🄽', '🄾', '🄿', '🅀', '🅁', '🅂', '🅃', '🅄', '🅅', '🅆', '🅇', '🅈', '🅉', 'ᴀ', 'ʙ', 'ᴄ', 'ᴅ', 'ᴇ', 'ғ', 'ɢ', 'ʜ', 'ɪ', 'ᴊ', 'ᴋ', 'ʟ', 'ᴍ', 'ɴ', '𝕬', '𝕭', '𝕮', '𝕯', '𝕰', '𝕱', '𝕲', '𝕳', '𝕴', '𝕵', '𝕶', '𝕷', '𝕸', '𝕹', '𝕺', '𝕻', '𝕼', '𝕽', '𝕾', '𝕿', '𝖀', '𝖁', '𝖂', '𝖃', '𝖄', '𝖅','ᴘ', 'ǫ', 'ʀ', 's', 'ᴛ', 'ᴜ', 'ᴠ', 'ᴡ', 'x', 'ʏ', 'ᴢ','𝘈', '𝘉', '𝘊', '𝘋', '𝘌', '𝘍', '𝘎', '𝘏', '𝘐', '𝘑', '𝘒', '𝘓', '𝘔', '𝘕', '𝘖', '𝘗', '𝘘', '𝘙', '𝘚', '𝘛', '𝘜', '𝘝', '𝘞', '𝘟', '𝘠', '𝘡', '₳', '฿', '₵', 'Đ', 'Ɇ', '₣', '₲', 'Ⱨ', 'ł', 'J', '₭', 'Ⱡ', '₥', '₦', 'Ø', '₱', 'Q', 'Ɽ', '₴', '₮', 'Ʉ', 'V', '₩', 'Ӿ', 'Ɏ', 'Ⱬ', 'Ⓐ', 'Ⓑ', 'Ⓒ', 'Ⓓ', 'Ⓔ', 'Ⓕ', 'Ⓖ', 'Ⓗ', 'Ⓘ', 'Ⓙ', 'Ⓚ', 'Ⓛ', 'Ⓜ', 'Ⓝ', 'Ⓞ', 'Ⓟ', 'Ⓠ', 'Ⓡ', 'Ⓢ', 'Ⓣ', 'Ⓤ', 'Ⓥ', 'Ⓦ', 'Ⓧ', 'Ⓨ', 'Ⓩ', '𝔄', '𝔅', 'ℭ', '𝔇', '𝔈', '𝔉', '𝔊', 'ℌ', 'ℑ', '𝔍', '𝔎', '𝔏', '𝔐', '𝔑', '𝔒', '𝔓', '𝔔', 'ℜ', '𝔖', '𝔗', '𝔘', '𝔙', '𝔚', '𝔛', '𝔜', 'ℨ', 'Ａ', 'Ｂ', 'Ｃ', 'Ｄ', 'Ｅ', 'Ｆ', 'Ｇ', 'Ｈ', 'Ｉ', 'Ｊ', 'Ｋ', 'Ｌ', 'Ｍ', 'Ｎ', 'Ｏ', 'Ｐ', 'Ｑ', 'Ｒ', 'Ｓ', 'Ｔ', 'Ｕ', 'Ｖ', 'Ｗ', 'Ｘ', 'Ｙ', 'Ｚ', '🅐', '🅑', '🅒', '🅓', '🅔', '🅕', '🅖', '🅗', '🅘', '🅙', '🅚', '🅛', '🅜', '🅝', '🅞', '🅟', '🅠', '🅡', '🅢', '🅣', '🅤', '🅥', '🅦', '🅧', '🅨', '🅩', '🅰', '🅱', '🅲', '🅳', '🅴', '🅵', '🅶', '🅷', '🅸', '🅹', '🅺', '🅻', '🅼', '🅽', '🅾', '🅿', '🆀', '🆁', '🆂', '🆃', '🆄', '🆅', '🆆', '🆇', '🆈', '🆉', '𝗔', '𝗕', '𝗖', '𝗗', '𝗘', '𝗙', '𝗚', '𝗛', '𝗜', '𝗝', '𝗞', '𝗟', '𝗠', '𝗡', '𝗢', '𝗣', '𝗤', '𝗥', '𝗦', '𝗧', '𝗨', '𝗩', '𝗪', '𝗫', '𝗬', '𝗭', 'Ꭿ', 'Ᏸ', 'Ꮸ', 'Ꭰ', 'Ꭼ', 'Ꮀ', 'Ꮆ', 'Ꮋ', 'Ꭸ', 'Ꮰ', 'Ꮶ', 'Ꮭ', 'Ꮇ', 'Ꮑ', 'Ꮎ', 'Ꮲ', 'Ꮕ', 'Ꮢ', 'Ꮥ', 'Ꮏ', 'Ꮼ', 'Ꮙ', 'Ꮿ', 'Ꮂ', 'Ꮍ', 'Ꮓ', '𝐀', '𝐁', '𝐂', '𝐃', '𝐄', '𝐅', '𝐆', '𝐇', '𝐈', '𝐉', '𝐊', '𝐋', '𝐌', '𝐍', '𝐎', '𝐏', '𝐐', '𝐑', '𝐒', '𝐓', '𝐔', '𝐕', '𝐖', '𝐗', '𝐘', '𝐙', '🇦‌', '🇪‌','🇮','🇦‌🇱‌🇱‌🇪‌🇳‌ 🇨‌🇱‌🇦‌🇸‌🇸‌🇷‌🇴‌🇴‌🇲‌🇪‌🇨‌🇹‌🇮‌🇴‌🇳‌-🇦‌','🇸‌🇮‌🇴‌'}
#ALPHABET = {'𝓐', '𝓑', '𝓒', '𝓓', '𝓔', '𝓕', '𝓖', '𝓗', '𝓘', '𝓙', '𝓚', '𝓛', '𝓜', '𝓝', '𝓞', '𝓟', '𝓠', '𝓡', '𝓢', '𝓣', '𝓤', '𝓥', '𝓦', '𝓧', '𝓨', '𝓩', '𝙰', '𝙱', '𝙲', '𝙳', '𝙴', '𝙵', '𝙶', '𝙷', '𝙸', '𝙹', '𝙺', '𝙻', '𝙼', '𝙽', '𝙿', '𝚁', '𝚂', '𝚃', '𝚄', '𝚅', '𝚆', '𝚇', '𝚈', '𝚉', 'ꋬ', 'ꃳ', 'ꉔ', '꒯', 'ꏂ', 'ꊰ', 'ꍌ', 'ꁝ', '꒐', '꒻', 'ꀘ', '꒒', 'ꂵ', 'ꋊ', 'ꄲ', 'ꉣ', 'ꆰ', 'ꋪ', 'ꇙ', '꓄', '꒤', '꒦', 'ꅐ', 'ꉧ', 'ꌦ', 'ꁴ​', '𝘼', '𝘽', '𝘾', '𝘿', '𝙀', '𝙁', '𝙂', '𝙃', '𝙄', '𝙅', '𝙆', '𝙇', '𝙈', '𝙉', '𝙊', '𝙋', '𝙌', '𝙍', '𝙎', '𝙏', '𝙐', '𝙑', '𝙒', '𝙓', '𝙔', '𝙕', '₳', '฿', '₵', 'Đ', 'Ɇ', '₣', '₲', 'Ⱨ', 'Ł', '₭', 'Ⱡ', '₥', '₦', 'Ø', '₱', 'Ɽ', '₴', '₮', 'Ʉ',  '₩', 'Ӿ', 'Ɏ', 'Ⱬ', '𝔸', '𝔹', 'ℂ', '𝔻', '𝔼', '𝔽', '𝔾', 'ℍ', '𝕀', '𝕁', '𝕂', '𝕃', '𝕄', 'ℕ', '𝕆', 'ℙ', 'ℚ', 'ℝ', '𝕊', '𝕋', '𝕌', '𝕍', '𝕎', '𝕏', '𝕐', 'ℤ', 'ል', 'ጌ', 'ር', 'ዕ', 'ቿ', 'ቻ', 'ኗ', 'ዘ', 'ጎ', 'ጋ', 'ጕ', 'ረ', 'ጠ', 'ክ', 'ዐ', 'የ', 'ዒ', 'ዪ', 'ነ', 'ፕ', 'ሁ', 'ሀ', 'ሠ', 'ሸ', 'ሃ', 'ጊ', 'ɐ', 'ɔ', 'ǝ', 'ɟ', 'ƃ', 'ɥ', 'ı', 'ɾ', 'ʞ', 'ן', 'ɯ', 'u', 'ɹ', 's', 'ʇ', 'ʌ', 'ʍ', 'x', 'ʎ', 'z','🄰', '🄱', '🄲', '🄳', '🄴', '🄵', '🄶', '🄷', '🄸', '🄹', '🄺', '🄻', '🄼', '🄽', '🄾', '🄿', '🅀', '🅁', '🅂', '🅃', '🅄', '🅅', '🅆', '🅇', '🅈', '🅉', 'ᴀ', 'ʙ', 'ᴄ', 'ᴅ', 'ᴇ', 'ғ', 'ɢ', 'ʜ', 'ɪ', 'ᴊ', 'ᴋ', 'ʟ', 'ᴍ', 'ɴ', '𝕬', '𝕭', '𝕮', '𝕯', '𝕰', '𝕱', '𝕲', '𝕳', '𝕴', '𝕵', '𝕶', '𝕷', '𝕸', '𝕹', '𝕺', '𝕻', '𝕼', '𝕽', '𝕾', '𝕿', '𝖀', '𝖁', '𝖂', '𝖃', '𝖄', '𝖅','ᴘ', 'ǫ', 'ʀ', 's', 'ᴛ', 'ᴜ', 'ᴠ', 'ᴡ', 'x', 'ʏ', 'ᴢ','𝘈', '𝘉', '𝘊', '𝘋', '𝘌', '𝘍', '𝘎', '𝘏', '𝘐', '𝘑', '𝘒', '𝘓', '𝘔', '𝘕', '𝘖', '𝘗', '𝘘', '𝘙', '𝘚', '𝘛', '𝘜', '𝘝', '𝘞', '𝘟', '𝘠', '𝘡', '₳', '฿', '₵', 'Đ', 'Ɇ', '₣', '₲', 'Ⱨ', 'ł', '₭', 'Ⱡ', '₥', '₦', 'Ø', '₱', 'Ɽ', '₴', '₮', 'Ʉ', '₩', 'Ӿ', 'Ɏ', 'Ⱬ', 'Ⓐ', 'Ⓑ', 'Ⓒ', 'Ⓓ', 'Ⓔ', 'Ⓕ', 'Ⓖ', 'Ⓗ', 'Ⓘ', 'Ⓙ', 'Ⓚ', 'Ⓛ', 'Ⓜ', 'Ⓝ', 'Ⓞ', 'Ⓟ', 'Ⓠ', 'Ⓡ', 'Ⓢ', 'Ⓣ', 'Ⓤ', 'Ⓥ', 'Ⓦ', 'Ⓧ', 'Ⓨ', 'Ⓩ', '𝔄', '𝔅', 'ℭ', '𝔇', '𝔈', '𝔉', '𝔊', 'ℌ', 'ℑ', '𝔍', '𝔎', '𝔏', '𝔐', '𝔑', '𝔒', '𝔓', '𝔔', 'ℜ', '𝔖', '𝔗', '𝔘', '𝔙', '𝔚', '𝔛', '𝔜', 'ℨ', '🅐', '🅑', '🅒', '🅓', '🅔', '🅕', '🅖', '🅗', '🅘', '🅙', '🅚', '🅛', '🅜', '🅝', '🅞', '🅟', '🅠', '🅡', '🅢', '🅣', '🅤', '🅥', '🅦', '🅧', '🅨', '🅩', '🅰', '🅱', '🅲', '🅳', '🅴', '🅵', '🅶', '🅷', '🅸', '🅹', '🅺', '🅻', '🅼', '🅽', '🅾', '🅿', '🆀', '🆁', '🆂', '🆃', '🆄', '🆅', '🆆', '🆇', '🆈', '🆉', '𝗔', '𝗕', '𝗖', '𝗗', '𝗘', '𝗙', '𝗚', '𝗛', '𝗜', '𝗝', '𝗞', '𝗟', '𝗠', '𝗡', '𝗢', '𝗣', '𝗤', '𝗥', '𝗦', '𝗧', '𝗨', '𝗩', '𝗪', '𝗫', '𝗬', '𝗭', 'Ꭿ', 'Ᏸ', 'Ꮸ', 'Ꭰ', 'Ꭼ', 'Ꮀ', 'Ꮆ', 'Ꮋ', 'Ꭸ', 'Ꮰ', 'Ꮶ', 'Ꮭ', 'Ꮇ', 'Ꮑ', 'Ꮎ', 'Ꮲ', 'Ꮕ', 'Ꮢ', 'Ꮥ', 'Ꮏ', 'Ꮼ', 'Ꮙ', 'Ꮿ', 'Ꮂ', 'Ꮍ', 'Ꮓ', '𝐀', '𝐁', '𝐂', '𝐃', '𝐄', '𝐅', '𝐆', '𝐇', '𝐈', '𝐉', '𝐊', '𝐋', '𝐌', '𝐍', '𝐎', '𝐏', '𝐐', '𝐑', '𝐒', '𝐓', '𝐔', '𝐕', '𝐖', '𝐗', '𝐘', '𝐙', '🇦‌', '🇪‌','🇮','🇦‌🇱‌🇱‌🇪‌🇳‌ 🇨‌🇱‌🇦‌🇸‌🇸‌🇷‌🇴‌🇴‌🇲‌🇪‌🇨‌🇹‌🇮‌🇴‌🇳‌-🇦‌','🇸‌🇮‌🇴‌'}
#ALPHABET = {'𝓐', '𝓑', '𝓒', '𝓓', '𝓔', '𝓕', '𝓖', '𝓗', '𝓘', '𝓙', '𝓚', '𝓛', '𝓜', '𝓝', '𝓞', '𝓟', '𝓠', '𝓡', '𝓢', '𝓣', '𝓤', '𝓥', '𝓦', '𝓧', '𝓨', '𝓩', '𝙰', '𝙱', '𝙲', '𝙳', '𝙴', '𝙵', '𝙶', '𝙷', '𝙸', '𝙹', '𝙺', '𝙻', '𝙼', '𝙽', '𝙿', '𝚁', '𝚂', '𝚃', '𝚄', '𝚅', '𝚆', '𝚇', '𝚈', '𝚉', 'ꋬ', 'ꃳ', 'ꉔ', '꒯', 'ꏂ', 'ꊰ', 'ꍌ', 'ꁝ', '꒐', '꒻', 'ꀘ', '꒒', 'ꂵ', 'ꋊ', 'ꄲ', 'ꉣ', 'ꆰ', 'ꋪ', 'ꇙ', '꓄', '꒤', '꒦', 'ꅐ', 'ꉧ', 'ꌦ', 'ꁴ​', '𝘼', '𝘽', '𝘾', '𝘿', '𝙀', '𝙁', '𝙂', '𝙃', '𝙄', '𝙅', '𝙆', '𝙇', '𝙈', '𝙉', '𝙊', '𝙋', '𝙌', '𝙍', '𝙎', '𝙏', '𝙐', '𝙑', '𝙒', '𝙓', '𝙔', '𝙕', '₳', '฿', '₵', 'Đ', 'Ɇ', '₣', '₲', 'Ⱨ', 'Ł', 'J', '₭', 'Ⱡ', '₥', '₦', 'Ø', '₱', 'Q', 'Ɽ', '₴', '₮', 'Ʉ', 'V', '₩', 'Ӿ', 'Ɏ', 'Ⱬ', '𝔸', '𝔹', 'ℂ', '𝔻', '𝔼', '𝔽', '𝔾', 'ℍ', '𝕀', '𝕁', '𝕂', '𝕃', '𝕄', 'ℕ', '𝕆', 'ℙ', 'ℚ', 'ℝ', '𝕊', '𝕋', '𝕌', '𝕍', '𝕎', '𝕏', '𝕐', 'ℤ', 'ል', 'ጌ', 'ር', 'ዕ', 'ቿ', 'ቻ', 'ኗ', 'ዘ', 'ጎ', 'ጋ', 'ጕ', 'ረ', 'ጠ', 'ክ', 'ዐ', 'የ', 'ዒ', 'ዪ', 'ነ', 'ፕ', 'ሁ', 'ሀ', 'ሠ', 'ሸ', 'ሃ', 'ጊ', 'ɐ', 'ɔ', 'ǝ', 'ɟ', 'ƃ', 'ɥ', 'ı', 'ɾ', 'ʞ', 'ן', 'ɯ', 'ɹ', 's', 'ʇ', 'ʌ', 'ʍ', 'x', 'ʎ', 'z','🄰', '🄱', '🄲', '🄳', '🄴', '🄵', '🄶', '🄷', '🄸', '🄹', '🄺', '🄻', '🄼', '🄽', '🄾', '🄿', '🅀', '🅁', '🅂', '🅃', '🅄', '🅅', '🅆', '🅇', '🅈', '🅉', 'ᴀ', 'ʙ', 'ᴄ', 'ᴅ', 'ᴇ', 'ғ', 'ɢ', 'ʜ', 'ɪ', 'ᴊ', 'ᴋ', 'ʟ', 'ᴍ', 'ɴ', '𝕬', '𝕭', '𝕮', '𝕯', '𝕰', '𝕱', '𝕲', '𝕳', '𝕴', '𝕵', '𝕶', '𝕷', '𝕸', '𝕹', '𝕺', '𝕻', '𝕼', '𝕽', '𝕾', '𝕿', '𝖀', '𝖁', '𝖂', '𝖃', '𝖄', '𝖅','ᴘ', 'ǫ', 'ʀ', 'ᴛ', 'ᴜ', 'ᴡ', 'x', 'ʏ','𝘈', '𝘉', '𝘊', '𝘋', '𝘌', '𝘍', '𝘎', '𝘏', '𝘐', '𝘑', '𝘒', '𝘓', '𝘔', '𝘕', '𝘖', '𝘗', '𝘘', '𝘙', '𝘚', '𝘛', '𝘜', '𝘝', '𝘞', '𝘟', '𝘠', '𝘡', '₳', '฿', '₵', 'Đ', 'Ɇ', '₣', '₲', 'Ⱨ', 'ł', 'J', '₭', 'Ⱡ', '₥', '₦', 'Ø', '₱', 'Q', 'Ɽ', '₴', '₮', 'Ʉ', 'V', '₩', 'Ӿ', 'Ɏ', 'Ⱬ', 'Ⓐ', 'Ⓑ', 'Ⓒ', 'Ⓓ', 'Ⓔ', 'Ⓕ', 'Ⓖ', 'Ⓗ', 'Ⓘ', 'Ⓙ', 'Ⓚ', 'Ⓛ', 'Ⓜ', 'Ⓝ', 'Ⓞ', 'Ⓟ', 'Ⓠ', 'Ⓡ', 'Ⓢ', 'Ⓣ', 'Ⓤ', 'Ⓥ', 'Ⓦ', 'Ⓧ', 'Ⓨ', 'Ⓩ', '𝔄', '𝔅', 'ℭ', '𝔇', '𝔈', '𝔉', '𝔊', 'ℌ', 'ℑ', '𝔍', '𝔎', '𝔏', '𝔐', '𝔑', '𝔒', '𝔓', '𝔔', 'ℜ', '𝔖', '𝔗', '𝔘', '𝔙', '𝔚', '𝔛', '𝔜', 'ℨ', 'Ａ', 'Ｂ', 'Ｃ', 'Ｄ', 'Ｅ', 'Ｆ', 'Ｇ', 'Ｈ', 'Ｉ', 'Ｊ', 'Ｋ', 'Ｌ', 'Ｍ', 'Ｎ', 'Ｏ', 'Ｐ', 'Ｑ', 'Ｒ', 'Ｓ', 'Ｔ', 'Ｕ', 'Ｖ', 'Ｗ', 'Ｘ', 'Ｙ', 'Ｚ', '🅐', '🅑', '🅒', '🅓', '🅔', '🅕', '🅖', '🅗', '🅘', '🅙', '🅚', '🅛', '🅜', '🅝', '🅞', '🅟', '🅠', '🅡', '🅢', '🅣', '🅤', '🅥', '🅦', '🅧', '🅨', '🅩', '🅰', '🅱', '🅲', '🅳', '🅴', '🅵', '🅶', '🅷', '🅸', '🅹', '🅺', '🅻', '🅼', '🅽', '🅾', '🅿', '🆀', '🆁', '🆂', '🆃', '🆄', '🆅', '🆆', '🆇', '🆈', '🆉', '𝗔', '𝗕', '𝗖', '𝗗', '𝗘', '𝗙', '𝗚', '𝗛', '𝗜', '𝗝', '𝗞', '𝗟', '𝗠', '𝗡', '𝗢', '𝗣', '𝗤', '𝗥', '𝗦', '𝗧', '𝗨', '𝗩', '𝗪', '𝗫', '𝗬', '𝗭', 'Ꭿ', 'Ᏸ', 'Ꮸ', 'Ꭰ', 'Ꭼ', 'Ꮀ', 'Ꮆ', 'Ꮋ', 'Ꭸ', 'Ꮰ', 'Ꮶ', 'Ꮭ', 'Ꮇ', 'Ꮑ', 'Ꮎ', 'Ꮲ', 'Ꮕ', 'Ꮢ', 'Ꮥ', 'Ꮏ', 'Ꮼ', 'Ꮙ', 'Ꮿ', 'Ꮂ', 'Ꮍ', 'Ꮓ', '𝐀', '𝐁', '𝐂', '𝐃', '𝐄', '𝐅', '𝐆', '𝐇', '𝐈', '𝐉', '𝐊', '𝐋', '𝐌', '𝐍', '𝐎', '𝐏', '𝐐', '𝐑', '𝐒', '𝐓', '𝐔', '𝐕', '𝐖', '𝐗', '𝐘', '𝐙', '🇦‌', '🇪‌','🇮','🇦‌🇱‌🇱‌🇪‌🇳‌ 🇨‌🇱‌🇦‌🇸‌🇸‌🇷‌🇴‌🇴‌🇲‌🇪‌🇨‌🇹‌🇮‌🇴‌🇳‌-🇦‌','🇸‌🇮‌🇴‌'}
#ALPHABET = {'𝓐', '𝓑', '𝓒', '𝓓', '𝓔', '𝓕', '𝓖', '𝓗', '𝓘', '𝓙', '𝓚', '𝓛', '𝓜', '𝓝', '𝓞', '𝓟', '𝓠', '𝓡', '𝓢', '𝓣', '𝓤', '𝓥', '𝓦', '𝓧', '𝓨', '𝓩', '𝙰', '𝙱', '𝙲', '𝙳', '𝙴', '𝙵', '𝙶', '𝙷', '𝙸', '𝙹', '𝙺', '𝙻', '𝙼', '𝙽', '𝙿', '𝚁', '𝚂', '𝚃', '𝚄', '𝚅', '𝚆', '𝚇', '𝚈', '𝚉', 'ꋬ', 'ꃳ', 'ꉔ', '꒯', 'ꏂ', 'ꊰ', 'ꍌ', 'ꁝ', '꒐', '꒻', 'ꀘ', '꒒', 'ꂵ', 'ꋊ', 'ꄲ', 'ꉣ', 'ꆰ', 'ꋪ', 'ꇙ', '꓄', '꒤', '꒦', 'ꅐ', 'ꉧ', 'ꌦ', 'ꁴ​', '𝘼', '𝘽', '𝘾', '𝘿', '𝙀', '𝙁', '𝙂', '𝙃', '𝙄', '𝙅', '𝙆', '𝙇', '𝙈', '𝙉', '𝙊', '𝙋', '𝙌', '𝙍', '𝙎', '𝙏', '𝙐', '𝙑', '𝙒', '𝙓', '𝙔', '𝙕', '₳', '฿', '₵', 'Đ', 'Ɇ', '₣', '₲', 'Ⱨ', 'Ł',  '₭', 'Ⱡ', '₥', '₦', 'Ø', '₱',  'Ɽ', '₴', '₮', 'Ʉ',, '₩', 'Ӿ', 'Ɏ', 'Ⱬ', '𝔸', '𝔹', 'ℂ', '𝔻', '𝔼', '𝔽', '𝔾', 'ℍ', '𝕀', '𝕁', '𝕂', '𝕃', '𝕄', 'ℕ', '𝕆', 'ℙ', 'ℚ', 'ℝ', '𝕊', '𝕋', '𝕌', '𝕍', '𝕎', '𝕏', '𝕐', 'ℤ', 'ል', 'ጌ', 'ር', 'ዕ', 'ቿ', 'ቻ', 'ኗ', 'ዘ', 'ጎ', 'ጋ', 'ጕ', 'ረ', 'ጠ', 'ክ', 'ዐ', 'የ', 'ዒ', 'ዪ', 'ነ', 'ፕ', 'ሁ', 'ሀ', 'ሠ', 'ሸ', 'ሃ', 'ጊ', 'ɐ', 'ɔ', 'ǝ', 'ɟ', 'ƃ', 'ɥ', 'ı', 'ɾ', 'ʞ', 'ן', 'ɯ', 'ɹ',  'ʇ', 'ʌ', 'ʍ',  'ʎ','🄰', '🄱', '🄲', '🄳', '🄴', '🄵', '🄶', '🄷', '🄸', '🄹', '🄺', '🄻', '🄼', '🄽', '🄾', '🄿', '🅀', '🅁', '🅂', '🅃', '🅄', '🅅', '🅆', '🅇', '🅈', '🅉', 'ᴀ', 'ʙ', 'ᴄ', 'ᴅ', 'ᴇ', 'ғ', 'ɢ', 'ʜ', 'ɪ', 'ᴊ', 'ᴋ', 'ʟ', 'ᴍ', 'ɴ', '𝕬', '𝕭', '𝕮', '𝕯', '𝕰', '𝕱', '𝕲', '𝕳', '𝕴', '𝕵', '𝕶', '𝕷', '𝕸', '𝕹', '𝕺', '𝕻', '𝕼', '𝕽', '𝕾', '𝕿', '𝖀', '𝖁', '𝖂', '𝖃', '𝖄', '𝖅','ᴘ', 'ǫ', 'ʀ', 'ᴛ', 'ᴜ', 'ᴡ', 'ʏ','𝘈', '𝘉', '𝘊', '𝘋', '𝘌', '𝘍', '𝘎', '𝘏', '𝘐', '𝘑', '𝘒', '𝘓', '𝘔', '𝘕', '𝘖', '𝘗', '𝘘', '𝘙', '𝘚', '𝘛', '𝘜', '𝘝', '𝘞', '𝘟', '𝘠', '𝘡', '₳', '฿', '₵', 'Đ', 'Ɇ', '₣', '₲', 'Ⱨ', 'ł', 'J', '₭', 'Ⱡ', '₥', '₦', 'Ø', '₱', 'Q', 'Ɽ', '₴', '₮', 'Ʉ', 'V', '₩', 'Ӿ', 'Ɏ', 'Ⱬ', 'Ⓐ', 'Ⓑ', 'Ⓒ', 'Ⓓ', 'Ⓔ', 'Ⓕ', 'Ⓖ', 'Ⓗ', 'Ⓘ', 'Ⓙ', 'Ⓚ', 'Ⓛ', 'Ⓜ', 'Ⓝ', 'Ⓞ', 'Ⓟ', 'Ⓠ', 'Ⓡ', 'Ⓢ', 'Ⓣ', 'Ⓤ', 'Ⓥ', 'Ⓦ', 'Ⓧ', 'Ⓨ', 'Ⓩ', '𝔄', '𝔅', 'ℭ', '𝔇', '𝔈', '𝔉', '𝔊', 'ℌ', 'ℑ', '𝔍', '𝔎', '𝔏', '𝔐', '𝔑', '𝔒', '𝔓', '𝔔', 'ℜ', '𝔖', '𝔗', '𝔘', '𝔙', '𝔚', '𝔛', '𝔜', 'ℨ', 'Ａ', 'Ｂ', 'Ｃ', 'Ｄ', 'Ｅ', 'Ｆ', 'Ｇ', 'Ｈ', 'Ｉ', 'Ｊ', 'Ｋ', 'Ｌ', 'Ｍ', 'Ｎ', 'Ｏ', 'Ｐ', 'Ｑ', 'Ｒ', 'Ｓ', 'Ｔ', 'Ｕ', 'Ｖ', 'Ｗ', 'Ｘ', 'Ｙ', 'Ｚ', '🅐', '🅑', '🅒', '🅓', '🅔', '🅕', '🅖', '🅗', '🅘', '🅙', '🅚', '🅛', '🅜', '🅝', '🅞', '🅟', '🅠', '🅡', '🅢', '🅣', '🅤', '🅥', '🅦', '🅧', '🅨', '🅩', '🅰', '🅱', '🅲', '🅳', '🅴', '🅵', '🅶', '🅷', '🅸', '🅹', '🅺', '🅻', '🅼', '🅽', '🅾', '🅿', '🆀', '🆁', '🆂', '🆃', '🆄', '🆅', '🆆', '🆇', '🆈', '🆉', '𝗔', '𝗕', '𝗖', '𝗗', '𝗘', '𝗙', '𝗚', '𝗛', '𝗜', '𝗝', '𝗞', '𝗟', '𝗠', '𝗡', '𝗢', '𝗣', '𝗤', '𝗥', '𝗦', '𝗧', '𝗨', '𝗩', '𝗪', '𝗫', '𝗬', '𝗭', 'Ꭿ', 'Ᏸ', 'Ꮸ', 'Ꭰ', 'Ꭼ', 'Ꮀ', 'Ꮆ', 'Ꮋ', 'Ꭸ', 'Ꮰ', 'Ꮶ', 'Ꮭ', 'Ꮇ', 'Ꮑ', 'Ꮎ', 'Ꮲ', 'Ꮕ', 'Ꮢ', 'Ꮥ', 'Ꮏ', 'Ꮼ', 'Ꮙ', 'Ꮿ', 'Ꮂ', 'Ꮍ', 'Ꮓ', '𝐀', '𝐁', '𝐂', '𝐃', '𝐄', '𝐅', '𝐆', '𝐇', '𝐈', '𝐉', '𝐊', '𝐋', '𝐌', '𝐍', '𝐎', '𝐏', '𝐐', '𝐑', '𝐒', '𝐓', '𝐔', '𝐕', '𝐖', '𝐗', '𝐘', '𝐙', '🇦‌', '🇪‌','🇮','🇦‌🇱‌🇱‌🇪‌🇳‌ 🇨‌🇱‌🇦‌🇸‌🇸‌🇷‌🇴‌🇴‌🇲‌🇪‌🇨‌🇹‌🇮‌🇴‌🇳‌-🇦‌','🇸‌🇮‌🇴‌'}
#ALPHABET = {'𝓐', '𝓑', '𝓒', '𝓓', '𝓔', '𝓕', '𝓖', '𝓗', '𝓘', '𝓙', '𝓚', '𝓛', '𝓜', '𝓝', '𝓞', '𝓟', '𝓠', '𝓡', '𝓢', '𝓣', '𝓤', '𝓥', '𝓦', '𝓧', '𝓨', '𝓩', '𝙰', '𝙱', '𝙲', '𝙳', '𝙴', '𝙵', '𝙶', '𝙷', '𝙸', '𝙹', '𝙺', '𝙻', '𝙼', '𝙽', '𝙿', '𝚁', '𝚂', '𝚃', '𝚄', '𝚅', '𝚆', '𝚇', '𝚈', '𝚉', 'ꋬ', 'ꃳ', 'ꉔ', '꒯', 'ꏂ', 'ꊰ', 'ꍌ', 'ꁝ', '꒐', '꒻', 'ꀘ', '꒒', 'ꂵ', 'ꋊ', 'ꄲ', 'ꉣ', 'ꆰ', 'ꋪ', 'ꇙ', '꓄', '꒤', '꒦', 'ꅐ', 'ꉧ', 'ꌦ', 'ꁴ​', '𝘼', '𝘽', '𝘾', '𝘿', '𝙀', '𝙁', '𝙂', '𝙃', '𝙄', '𝙅', '𝙆', '𝙇', '𝙈', '𝙉', '𝙊', '𝙋', '𝙌', '𝙍', '𝙎', '𝙏', '𝙐', '𝙑', '𝙒', '𝙓', '𝙔', '𝙕', '₳', '฿', '₵', 'Đ', 'Ɇ', '₣', '₲', 'Ⱨ', '₭', 'Ⱡ', '₥', '₦', 'Ø', '₱', '₴', '₮', 'Ʉ', 'V', '₩', 'Ӿ', 'Ɏ', 'Ⱬ', '𝔸', '𝔹', 'ℂ', '𝔻', '𝔼', '𝔽', '𝔾', 'ℍ', '𝕀', '𝕁', '𝕂', '𝕃', '𝕄', 'ℕ', '𝕆', 'ℙ', 'ℚ', 'ℝ', '𝕊', '𝕋', '𝕌', '𝕍', '𝕎', '𝕏', '𝕐', 'ℤ', 'ል', 'ጌ', 'ር', 'ዕ', 'ቿ', 'ቻ', 'ኗ', 'ዘ', 'ጎ', 'ጋ', 'ጕ', 'ረ', 'ጠ', 'ክ', 'ዐ', 'የ', 'ዒ', 'ዪ', 'ነ', 'ፕ', 'ሁ', 'ሀ', 'ሠ', 'ሸ', 'ሃ', 'ጊ', 'ɐ', 'ɔ', 'ǝ', 'ɟ', 'ƃ', 'ɥ', 'ı', 'ɾ', 'ʞ', 'ן', 'ɯ', 'ɹ', 'ʇ', 'ʌ', 'ʍ', 'ʎ', '🄰', '🄱', '🄲', '🄳', '🄴', '🄵', '🄶', '🄷', '🄸', '🄹', '🄺', '🄻', '🄼', '🄽', '🄾', '🄿', '🅀', '🅁', '🅂', '🅃', '🅄', '🅅', '🅆', '🅇', '🅈', '🅉', 'ᴀ', 'ʙ', 'ᴄ', 'ᴅ', 'ᴇ', 'ғ', 'ɢ', 'ʜ', 'ɪ', 'ᴊ', 'ᴋ', 'ʟ', 'ᴍ', 'ɴ', '𝕬', '𝕭', '𝕮', '𝕯', '𝕰', '𝕱', '𝕲', '𝕳', '𝕴', '𝕵', '𝕶', '𝕷', '𝕸', '𝕹', '𝕺', '𝕻', '𝕼', '𝕽', '𝕾', '𝕿', '𝖀', '𝖁', '𝖂', '𝖃', '𝖄', '𝖅','ᴘ', 'ǫ','𝘈', '𝘉', '𝘊', '𝘋', '𝘌', '𝘍', '𝘎', '𝘏', '𝘐', '𝘑', '𝘒', '𝘓', '𝘔', '𝘕', '𝘖', '𝘗', '𝘘', '𝘙', '𝘚', '𝘛', '𝘜', '𝘝', '𝘞', '𝘟', '𝘠', '𝘡', '₳', '฿', '₵', 'Đ', 'Ɇ', '₣', '₲', 'Ⱨ', 'ł', 'J', '₭', 'Ⱡ', '₥', '₦', 'Ø', '₱', 'Q', 'Ɽ', '₴', '₮', 'Ʉ', 'V', '₩', 'Ӿ', 'Ɏ', 'Ⱬ', 'Ⓐ', 'Ⓑ', 'Ⓒ', 'Ⓓ', 'Ⓔ', 'Ⓕ', 'Ⓖ', 'Ⓗ', 'Ⓘ', 'Ⓙ', 'Ⓚ', 'Ⓛ', 'Ⓜ', 'Ⓝ', 'Ⓞ', 'Ⓟ', 'Ⓠ', 'Ⓡ', 'Ⓢ', 'Ⓣ', 'Ⓤ', 'Ⓥ', 'Ⓦ', 'Ⓧ', 'Ⓨ', 'Ⓩ', '𝔄', '𝔅', 'ℭ', '𝔇', '𝔈', '𝔉', '𝔊', 'ℌ', 'ℑ', '𝔍', '𝔎', '𝔏', '𝔐', '𝔑', '𝔒', '𝔓', '𝔔', 'ℜ', '𝔖', '𝔗', '𝔘', '𝔙', '𝔚', '𝔛', '𝔜', 'ℨ', 'Ａ', 'Ｂ', 'Ｃ', 'Ｄ', 'Ｅ', 'Ｆ', 'Ｇ', 'Ｈ', 'Ｉ', 'Ｊ', 'Ｋ', 'Ｌ', 'Ｍ', 'Ｎ', 'Ｏ', 'Ｐ', 'Ｑ', 'Ｒ', 'Ｓ', 'Ｔ', 'Ｕ', 'Ｖ', 'Ｗ', 'Ｘ', 'Ｙ', 'Ｚ', '🅐', '🅑', '🅒', '🅓', '🅔', '🅕', '🅖', '🅗', '🅘', '🅙', '🅚', '🅛', '🅜', '🅝', '🅞', '🅟', '🅠', '🅡', '🅢', '🅣', '🅤', '🅥', '🅦', '🅧', '🅨', '🅩', '🅰', '🅱', '🅲', '🅳', '🅴', '🅵', '🅶', '🅷', '🅸', '🅹', '🅺', '🅻', '🅼', '🅽', '🅾', '🅿', '🆀', '🆁', '🆂', '🆃', '🆄', '🆅', '🆆', '🆇', '🆈', '🆉', '𝗔', '𝗕', '𝗖', '𝗗', '𝗘', '𝗙', '𝗚', '𝗛', '𝗜', '𝗝', '𝗞', '𝗟', '𝗠', '𝗡', '𝗢', '𝗣', '𝗤', '𝗥', '𝗦', '𝗧', '𝗨', '𝗩', '𝗪', '𝗫', '𝗬', '𝗭', 'Ꭿ', 'Ᏸ', 'Ꮸ', 'Ꭰ', 'Ꭼ', 'Ꮀ', 'Ꮆ', 'Ꮋ', 'Ꭸ', 'Ꮰ', 'Ꮶ', 'Ꮭ', 'Ꮇ', 'Ꮑ', 'Ꮎ', 'Ꮲ', 'Ꮕ', 'Ꮢ', 'Ꮥ', 'Ꮏ', 'Ꮼ', 'Ꮙ', 'Ꮿ', 'Ꮂ', 'Ꮍ', 'Ꮓ', '𝐀', '𝐁', '𝐂', '𝐃', '𝐄', '𝐅', '𝐆', '𝐇', '𝐈', '𝐉', '𝐊', '𝐋', '𝐌', '𝐍', '𝐎', '𝐏', '𝐐', '𝐑', '𝐒', '𝐓', '𝐔', '𝐕', '𝐖', '𝐗', '𝐘', '𝐙', '🇦‌', '🇪‌','🇮','🇦‌🇱‌🇱‌🇪‌🇳‌ 🇨‌🇱‌🇦‌🇸‌🇸‌🇷‌🇴‌🇴‌🇲‌🇪‌🇨‌🇹‌🇮‌🇴‌🇳‌-🇦‌','🇸‌🇮‌🇴‌'}
#ALPHABET = {'𝓐', '𝓑', '𝓒', '𝓓', '𝓔', '𝓕', '𝓖', '𝓗', '𝓘', '𝓙', '𝓚', '𝓛', '𝓜', '𝓝', '𝓞', '𝓟', '𝓠', '𝓡', '𝓢', '𝓣', '𝓤', '𝓥', '𝓦', '𝓧', '𝓨', '𝓩', '𝙰', '𝙱', '𝙲', '𝙳', '𝙴', '𝙵', '𝙶', '𝙷', '𝙸', '𝙹', '𝙺', '𝙻', '𝙼', '𝙽', '𝙿', '𝚁', '𝚂', '𝚃', '𝚄', '𝚅', '𝚆', '𝚇', '𝚈', '𝚉', 'ꋬ', 'ꃳ', 'ꉔ', '꒯', 'ꏂ', 'ꊰ', 'ꍌ', 'ꁝ', '꒐', '꒻', 'ꀘ', '꒒', 'ꂵ', 'ꋊ', 'ꄲ', 'ꉣ', 'ꆰ', 'ꋪ', 'ꇙ', '꓄', '꒤', '꒦', 'ꅐ', 'ꉧ', 'ꌦ', 'ꁴ​', '𝘼', '𝘽', '𝘾', '𝘿', '𝙀', '𝙁', '𝙂', '𝙃', '𝙄', '𝙅', '𝙆', '𝙇', '𝙈', '𝙉', '𝙊', '𝙋', '𝙌', '𝙍', '𝙎', '𝙏', '𝙐', '𝙑', '𝙒', '𝙓', '𝙔', '𝙕', '₳', '฿', '₵', 'Đ', 'Ɇ', '₣', '₲', 'Ⱨ', '₭', 'Ⱡ', '₥', '₦', 'Ø', '₱', '₴', '₮', 'Ʉ', '₩', 'Ӿ', 'Ɏ', 'Ⱬ', '𝔸', '𝔹', 'ℂ', '𝔻', '𝔼', '𝔽', '𝔾', 'ℍ', '𝕀', '𝕁', '𝕂', '𝕃', '𝕄', 'ℕ', '𝕆', 'ℙ', 'ℚ', 'ℝ', '𝕊', '𝕋', '𝕌', '𝕍', '𝕎', '𝕏', '𝕐', 'ℤ', 'ል', 'ጌ', 'ር', 'ዕ', 'ቿ', 'ቻ', 'ኗ', 'ዘ', 'ጎ', 'ጋ', 'ጕ', 'ረ', 'ጠ', 'ክ', 'ዐ', 'የ', 'ዒ', 'ዪ', 'ነ', 'ፕ', 'ሁ', 'ሀ', 'ሠ', 'ሸ', 'ሃ', 'ጊ', 'ɐ', 'ɔ', 'ǝ', 'ɟ', 'ƃ', 'ɥ', 'ı', 'ɾ', 'ʞ', 'ן', 'ɯ', 'ɹ', 'ʇ', 'ʌ', 'ʍ', 'ʎ', '🄰', '🄱', '🄲', '🄳', '🄴', '🄵', '🄶', '🄷', '🄸', '🄹', '🄺', '🄻', '🄼', '🄽', '🄾', '🄿', '🅀', '🅁', '🅂', '🅃', '🅄', '🅅', '🅆', '🅇', '🅈', '🅉', 'ᴀ', 'ʙ', 'ᴄ', 'ᴅ', 'ᴇ', 'ғ', 'ɢ', 'ʜ', 'ɪ', 'ᴊ', 'ᴋ', 'ʟ', 'ᴍ', 'ɴ', '𝕬', '𝕭', '𝕮', '𝕯', '𝕰', '𝕱', '𝕲', '𝕳', '𝕴', '𝕵', '𝕶', '𝕷', '𝕸', '𝕹', '𝕺', '𝕻', '𝕼', '𝕽', '𝕾', '𝕿', '𝖀', '𝖁', '𝖂', '𝖃', '𝖄', '𝖅','ᴘ', 'ǫ','𝘈', '𝘉', '𝘊', '𝘋', '𝘌', '𝘍', '𝘎', '𝘏', '𝘐', '𝘑', '𝘒', '𝘓', '𝘔', '𝘕', '𝘖', '𝘗', '𝘘', '𝘙', '𝘚', '𝘛', '𝘜', '𝘝', '𝘞', '𝘟', '𝘠', '𝘡', '₳', '฿', '₵', 'Đ', 'Ɇ', '₣', '₲', 'Ⱨ',  'Ⱡ', '₥', '₦', 'Ø', '₱', 'Q', 'Ɽ', '₴', '₮',  '₩', 'Ӿ', 'Ɏ', 'Ⱬ', 'Ⓐ', 'Ⓑ', 'Ⓒ', 'Ⓓ', 'Ⓔ', 'Ⓕ', 'Ⓖ', 'Ⓗ', 'Ⓘ', 'Ⓙ', 'Ⓚ', 'Ⓛ', 'Ⓜ', 'Ⓝ', 'Ⓞ', 'Ⓟ', 'Ⓠ', 'Ⓡ', 'Ⓢ', 'Ⓣ', 'Ⓤ', 'Ⓥ', 'Ⓦ', 'Ⓧ', 'Ⓨ', 'Ⓩ', '𝔄', '𝔅', 'ℭ', '𝔇', '𝔈', '𝔉', '𝔊', 'ℌ', 'ℑ', '𝔍', '𝔎', '𝔏', '𝔐', '𝔑', '𝔒', '𝔓', '𝔔', 'ℜ', '𝔖', '𝔗', '𝔘', '𝔙', '𝔚', '𝔛', '𝔜', 'ℨ', 'Ａ', 'Ｂ', 'Ｃ', 'Ｄ', 'Ｅ', 'Ｆ', 'Ｇ', 'Ｈ', 'Ｉ', 'Ｊ', 'Ｋ', 'Ｌ', 'Ｍ', 'Ｎ', 'Ｏ', 'Ｐ', 'Ｑ', 'Ｒ', 'Ｓ', 'Ｔ', 'Ｕ', 'Ｖ', 'Ｗ', 'Ｘ', 'Ｙ', 'Ｚ', '🅐', '🅑', '🅒', '🅓', '🅔', '🅕', '🅖', '🅗', '🅘', '🅙', '🅚', '🅛', '🅜', '🅝', '🅞', '🅟', '🅠', '🅡', '🅢', '🅣', '🅤', '🅥', '🅦', '🅧', '🅨', '🅩', '🅰', '🅱', '🅲', '🅳', '🅴', '🅵', '🅶', '🅷', '🅸', '🅹', '🅺', '🅻', '🅼', '🅽', '🅾', '🅿', '🆀', '🆁', '🆂', '🆃', '🆄', '🆅', '🆆', '🆇', '🆈', '🆉', '𝗔', '𝗕', '𝗖', '𝗗', '𝗘', '𝗙', '𝗚', '𝗛', '𝗜', '𝗝', '𝗞', '𝗟', '𝗠', '𝗡', '𝗢', '𝗣', '𝗤', '𝗥', '𝗦', '𝗧', '𝗨', '𝗩', '𝗪', '𝗫', '𝗬', '𝗭', 'Ꭿ', 'Ᏸ', 'Ꮸ', 'Ꭰ', 'Ꭼ', 'Ꮀ', 'Ꮆ', 'Ꮋ', 'Ꭸ', 'Ꮰ', 'Ꮶ', 'Ꮭ', 'Ꮇ', 'Ꮑ', 'Ꮎ', 'Ꮲ', 'Ꮕ', 'Ꮢ', 'Ꮥ', 'Ꮏ', 'Ꮼ', 'Ꮙ', 'Ꮿ', 'Ꮂ', 'Ꮍ', 'Ꮓ', '𝐀', '𝐁', '𝐂', '𝐃', '𝐄', '𝐅', '𝐆', '𝐇', '𝐈', '𝐉', '𝐊', '𝐋', '𝐌', '𝐍', '𝐎', '𝐏', '𝐐', '𝐑', '𝐒', '𝐓', '𝐔', '𝐕', '𝐖', '𝐗', '𝐘', '𝐙', '🇦‌', '🇪‌','🇮','🇦‌🇱‌🇱‌🇪‌🇳‌ 🇨‌🇱‌🇦‌🇸‌🇸‌🇷‌🇴‌🇴‌🇲‌🇪‌🇨‌🇹‌🇮‌🇴‌🇳‌-🇦‌','🇸‌🇮‌🇴‌'}

ALPHABET = {'𝓐', '𝓑', '𝓒', '𝓓', '𝓔', '𝓕', '𝓖', '𝓗', '𝓘', '𝓚', '𝓛', '𝓜', '𝓝',  '𝓟', '𝓠', '𝓡', '𝓢', '𝓣', '𝓤',  '𝓦', '𝓧', '𝓨', '𝓩', '𝙰', '𝙱', '𝙲', '𝙳', '𝙴', '𝙵', '𝙶', '𝙷', '𝙸', '𝙹', '𝙺', '𝙻', '𝙼', '𝙽', '𝙿', '𝚁', '𝚂', '𝚃', '𝚄', '𝚅', '𝚆', '𝚇', '𝚈', '𝚉', 'ꋬ', 'ꃳ', 'ꉔ', '꒯', 'ꏂ', 'ꊰ', 'ꍌ', 'ꁝ', '꒐', '꒻', 'ꀘ', '꒒', 'ꂵ', 'ꋊ', 'ꄲ', 'ꉣ', 'ꆰ', 'ꋪ', 'ꇙ', '꓄', '꒤', '꒦', 'ꅐ', 'ꉧ', 'ꌦ', 'ꁴ​', '𝘼', '𝘽', '𝘾', '𝘿', '𝙀', '𝙁', '𝙂', '𝙃', '𝙄', '𝙅', '𝙆', '𝙇', '𝙈', '𝙉', '𝙊', '𝙋', '𝙌', '𝙍', '𝙎', '𝙏', '𝙐', '𝙑', '𝙒', '𝙓', '𝙔', '𝙕', '₳', '฿', '₵', 'Đ', 'Ɇ', '₣', '₲', 'Ⱨ', '₭', 'Ⱡ', '₥', '₦', 'Ø', '₱', '₴', '₮', 'Ʉ', '₩', 'Ӿ', 'Ɏ', 'Ⱬ', '𝔸', '𝔹', 'ℂ', '𝔻', '𝔼', '𝔽', '𝔾', 'ℍ', '𝕀',  '𝕂', '𝕃', '𝕄', 'ℕ', '𝕆', 'ℙ', 'ℝ', '𝕊', '𝕋', '𝕌', '𝕎', '𝕏', '𝕐', 'ℤ', 'ል', 'ጌ', 'ር', 'ዕ', 'ቿ', 'ቻ', 'ኗ', 'ዘ', 'ጎ', 'ጋ', 'ጕ', 'ረ', 'ጠ', 'ክ', 'ዐ', 'የ', 'ዒ', 'ዪ', 'ነ', 'ፕ', 'ሁ', 'ሀ', 'ሠ', 'ሸ', 'ሃ', 'ጊ', 'ɐ', 'ɔ', 'ǝ', 'ɟ', 'ƃ', 'ɥ', 'ı', 'ɾ', 'ʞ', 'ן', 'ɯ', 'ɹ', 'ʇ', 'ʌ', 'ʍ', 'ʎ', '🄰', '🄱', '🄲', '🄳', '🄴', '🄵', '🄶', '🄷', '🄸', '🄺', '🄻', '🄼', '🄽', '🄾', '🄿', '🅁', '🅂', '🅃', '🅄', '🅆', '🅇', '🅈', '🅉', 'ᴀ', 'ʙ', 'ᴄ', 'ᴅ', 'ᴇ', 'ғ', 'ɢ', 'ʜ', 'ɪ', 'ᴊ', 'ᴋ', 'ʟ', 'ᴍ', 'ɴ', '𝕬', '𝕭', '𝕮', '𝕯', '𝕰', '𝕱', '𝕲', '𝕳', '𝕴', '𝕵', '𝕶', '𝕷', '𝕸', '𝕹', '𝕺', '𝕻', '𝕼', '𝕽', '𝕾', '𝕿', '𝖀', '𝖁', '𝖂', '𝖃', '𝖄', '𝖅','ᴘ', 'ǫ','𝘈', '𝘉', '𝘊', '𝘋', '𝘌', '𝘍', '𝘎', '𝘏', '𝘐', '𝘒', '𝘓', '𝘔', '𝘕', '𝘖', '𝘗', '𝘙', '𝘚', '𝘛', '𝘜', '𝘞', '𝘟', '𝘠', '𝘡', '₳', '฿', '₵', 'Đ', 'Ɇ', '₣', '₲', 'Ⱨ',  'Ⱡ', '₥', '₦', 'Ø', '₱', 'Ɽ', '₴', '₮',  '₩', 'Ӿ', 'Ɏ', 'Ⱬ', 'Ⓐ', 'Ⓑ', 'Ⓒ', 'Ⓓ', 'Ⓔ', 'Ⓕ', 'Ⓖ', 'Ⓗ', 'Ⓘ', 'Ⓚ', 'Ⓛ', 'Ⓜ', 'Ⓝ', 'Ⓞ', 'Ⓟ', 'Ⓡ', 'Ⓢ', 'Ⓣ', 'Ⓤ',  'Ⓦ', 'Ⓧ', 'Ⓨ', 'Ⓩ', '𝔄', '𝔅', 'ℭ', '𝔇', '𝔈', '𝔉', '𝔊', 'ℌ', 'ℑ', '𝔍', '𝔎', '𝔏', '𝔐', '𝔑', '𝔒', '𝔓', '𝔔', 'ℜ', '𝔖', '𝔗', '𝔘', '𝔙', '𝔚', '𝔛', '𝔜', 'ℨ', 'Ａ', 'Ｂ', 'Ｃ', 'Ｄ', 'Ｅ', 'Ｆ', 'Ｇ', 'Ｈ', 'Ｉ', 'Ｋ', 'Ｌ', 'Ｍ', 'Ｎ', 'Ｏ', 'Ｐ', 'Ｒ', 'Ｓ', 'Ｔ', 'Ｕ',  'Ｗ', 'Ｘ', 'Ｙ', 'Ｚ', '🅐', '🅑', '🅒', '🅓', '🅔', '🅕', '🅖', '🅗', '🅘', '🅙', '🅚', '🅛', '🅜', '🅝', '🅞', '🅟', '🅠', '🅡', '🅢', '🅣', '🅤', '🅥', '🅦', '🅧', '🅨', '🅩', '🅰', '🅱', '🅲', '🅳', '🅴', '🅵', '🅶', '🅷', '🅸', '🅹', '🅺', '🅻', '🅼', '🅽', '🅾', '🅿', '🆀', '🆁', '🆂', '🆃', '🆄', '🆅', '🆆', '🆇', '🆈', '🆉', '𝗔', '𝗕', '𝗖', '𝗗', '𝗘', '𝗙', '𝗚', '𝗛', '𝗜', '𝗝', '𝗞', '𝗟', '𝗠', '𝗡', '𝗢', '𝗣', '𝗤', '𝗥', '𝗦', '𝗧', '𝗨', '𝗩', '𝗪', '𝗫', '𝗬', '𝗭', 'Ꭿ', 'Ᏸ', 'Ꮸ', 'Ꭰ', 'Ꭼ', 'Ꮀ', 'Ꮆ', 'Ꮋ', 'Ꭸ', 'Ꮰ', 'Ꮶ', 'Ꮭ', 'Ꮇ', 'Ꮑ', 'Ꮎ', 'Ꮲ', 'Ꮕ', 'Ꮢ', 'Ꮥ', 'Ꮏ', 'Ꮼ', 'Ꮙ', 'Ꮿ', 'Ꮂ', 'Ꮍ', 'Ꮓ', '𝐀', '𝐁', '𝐂', '𝐃', '𝐄', '𝐅', '𝐆', '𝐇', '𝐈', '𝐉', '𝐊', '𝐋', '𝐌', '𝐍', '𝐎', '𝐏', '𝐐', '𝐑', '𝐒', '𝐓', '𝐔', '𝐕', '𝐖', '𝐗', '𝐘', '𝐙', '🇦‌', '🇪‌','🇮','🇦‌🇱‌🇱‌🇪‌🇳‌ 🇨‌🇱‌🇦‌🇸‌🇸‌🇷‌🇴‌🇴‌🇲‌🇪‌🇨‌🇹‌🇮‌🇴‌🇳‌-🇦‌','🇸‌🇮‌🇴‌', '𝙖', '𝙗', '𝙘', '𝙙', '𝙚', '𝙛', '𝙜', '𝙝', '𝙞', '𝙟', '𝙠', '𝙡', '𝙢', '𝙣', '𝙤', '𝙥', '𝙦', '𝙧', '𝙨', '𝙩', '𝙪', '𝙫', '𝙬', '𝙭', '𝙮', '𝙯', '𝗮', '𝗯', '𝗰', '𝗱', '𝗲', '𝗳', '𝗴', '𝗵', '𝗶', '𝗷', '𝗸', '𝗹', '𝗺', '𝗻', '𝗼', '𝗽', '𝗾', '𝗿', '𝘀', '𝘁', '𝘂', '𝘃', '𝘄', '𝘅', '𝘆', '𝘇'}

async def contains_font(text):
    # Check if the message contains non-ASCII characters (indicating it's a font)
    return any(char in ALPHABET for char in text)

@app.on_message(filters.text & filters.group & ~filters.bot)
async def fonts(_, message:Message):
    if await contains_font(message.text):
        sendee = message.from_user.id
        await message.reply(f'{sendee} sending font in chat')
        await message.delete()

app.run()
idle()