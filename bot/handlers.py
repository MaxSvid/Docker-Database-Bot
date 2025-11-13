import logging
import os
import json
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from config import settings
from keyboards import language_menu, main_menu, channels_menu, back_menu

logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()

# Import DB functions
from db.execute import insert_users, update_language_code

# Temporary memory for user language
user_languages = {}

# Load translations
translate_path = os.path.join(os.path.dirname(__file__), '..', 'translate', 'translation.json')
with open(translate_path, "r", encoding="utf-8") as file:
    translations = json.load(file)


# Start command
@dp.message(Command("start"))
async def start(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username or "None"
    language_code = message.from_user.language_code or "NULL"

    # Storing in database
    insert_users(user_id, username, language_code)

    # Normalize language for local memory
    lang = "ru" if language_code and language_code.startswith("ru") else "en"
    user_languages[user_id] = lang

    await message.answer(
        text="👋 Welcome to Docker Example Bot!\n\nPlease select your language / Пожалуйста, выберите язык:",
        reply_markup=language_menu()
    )
    

# Language Option
@dp.callback_query(F.data.in_({"lang_en", "lang_ru"}))
async def language_options(callback: CallbackQuery):
    lang = "en" if callback.data == "lang_en" else "ru"

    # Update DB
    update_language_code(callback.from_user.id, lang)

    # Update local memory
    user_languages[callback.from_user.id] = lang

    welcome_text = translations["welcome_message"][lang]

    await callback.message.edit_text(
        text=welcome_text,
        reply_markup=main_menu(lang),
        parse_mode="Markdown"
    )
    await callback.answer()


# About section
@dp.callback_query(F.data == "about")
async def about(callback: CallbackQuery):
    lang = user_languages.get(callback.from_user.id, "en")
    about_text = translations["about"][lang]

    await callback.message.edit_text(
        text=about_text,
        reply_markup=back_menu(lang),
        parse_mode="Markdown"
    )
    await callback.answer()


# Contact section
@dp.callback_query(F.data == "contact")
async def contact(callback: CallbackQuery):
    lang = user_languages.get(callback.from_user.id, "en")
    contact_text = translations["contact"][lang]

    text_contact = contact_text.format(
        admin=settings.LEAD_ADMIN_USERNAME,
        website="Not Available atm"
    )

    # No parse_mode
    await callback.message.edit_text(
        text=text_contact,
        reply_markup=back_menu(lang)
    )
    await callback.answer()



# Links section
@dp.callback_query(F.data == "links")
async def links(callback: CallbackQuery):
    lang = user_languages.get(callback.from_user.id, "en")
    text_links = translations["links"][lang]

    await callback.message.edit_text(
        text=text_links,
        reply_markup=channels_menu(lang),
        parse_mode="Markdown"
    )
    await callback.answer()


# Back to main menu
@dp.callback_query(F.data.in_({"back", "back_menu"}))
async def back_to_main(callback: CallbackQuery):
    lang = user_languages.get(callback.from_user.id, "en")
    text = translations["back_menu_text"][lang]

    await callback.message.edit_text(
        text=text,
        reply_markup=main_menu(lang),
        parse_mode="Markdown"
    )
    await callback.answer()


# Unknown message
@dp.message()
async def no_text(message: Message):
    lang = user_languages.get(message.from_user.id, "en")
    reply_text = translations["no_text_allowed"][lang]

    if not message.text.startswith("/"):
        await message.answer(
            text=reply_text,
            reply_markup=language_menu()
        )
