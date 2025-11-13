from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# Passing a List as an Argument to send any data types of argument to a function (string, number, list, dictionary etc.),
# and it will be treated as the same data type inside the function.

# language option for start section

def language_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🇺🇸 English", callback_data="lang_en"),
                InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru"),
            ]
        ]
    )


def main_menu(lang: str = "en") -> InlineKeyboardMarkup:
    if lang == "ru":
        keyboard = [
            [InlineKeyboardButton(text="🌌 О чем этот бот?", callback_data="about")],
            [
                InlineKeyboardButton(text="📞 Связь", callback_data="contact"),
                InlineKeyboardButton(text="🔗 Официальные ссылки", callback_data="links"),
            ],
        ]
    else:
        keyboard = [
            [InlineKeyboardButton(text="🌌 What is this bot about?", callback_data="about")],
            [
                InlineKeyboardButton(text="📞 Contact", callback_data="contact"),
                InlineKeyboardButton(text="🔗 Official Links", callback_data="links"),
            ],
        ]

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def channels_menu(lang: str = "en") -> InlineKeyboardMarkup:
    if lang == "ru":
        keyboard = [
            [InlineKeyboardButton(text="📖 Teletype Профиль", url="https://teletype.in/@mak_sjr")],
            [InlineKeyboardButton(text="📢 Telegram Канал", url="https://t.me/DeFi_Mirror")],
            [InlineKeyboardButton(text="⬅️ Назад", callback_data="back")],
        ]
    else:
        keyboard = [
            [InlineKeyboardButton(text="📖 Teletype Profile", url="https://teletype.in/@mak_sjr")],
            [InlineKeyboardButton(text="📢 Telegram Channel", url="https://t.me/DeFi_Mirror")],
            [InlineKeyboardButton(text="⬅️ Back", callback_data="back")],
        ]

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def back_menu(lang: str = "en") -> InlineKeyboardMarkup:
    text = "🔙 Назад в меню" if lang == "ru" else "🔙 Back to menu"
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=text, callback_data="back_menu")]
        ]
    )
