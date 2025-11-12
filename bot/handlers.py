import logging
import asyncio
from aiogram import Bot, Dispatcher, F, Router
from aiogram.types import Message, CallbackQuery, FSInputFile, BotCommand 
from aiogram.filters import Command

# from /bot сonfig.py file 
from config import settings

# from /bot keyboards.py
from keyboards import language_menu, main_menu, channels_menu, back_menu

logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()

# Temporary memory for user language 
user_languages = {}

# Load translations from translate folder 
import os 
import json
translate_path = os.path.join(os.path.dirname(__file__), '..', 'translate', 'translation.json')

# Opening the json file 
with open(translate_path, "r", encoding="utf-8") as file:
    translations = json.load(file)

# Loading /db execute.py file for postgres data 
from db.execute import insert_users, update_language_code

# Start command handler
@dp.message(Command("start"))
async def start(message: Message):

    # for database from execute.py
    user_id = message.from_user.id
    username = message.from_user.username or "None"
    language_code = message.from_user.language_code or "NULL"

    insert_users(user_id, username, language_code)

    await message.answer(        
        text="👋 Welcome to Docker Example Bot!\n\nPlease select your language / Пожалуйста, выберите язык:",
        reply_markup=language_menu()
    )
    
# Option to choose a language at the start
@dp.callback_query(F.data.in_({"lang_en", "lang_ru"}))
async def language_options(callback: CallbackQuery):
    lang = "en" if callback.data == "lang_en" else "ru"

    # Database
    update_language_code(callback.from_user.id, lang)

    # Local cache
    user_languages[callback.from_user.id] = lang

    welcome_text = translations["welcome_message"][lang]

    await callback.message.edit_text(
        text=welcome_text,
        reply_markup=main_menu(lang),
        parse_mode="Markdown"
        )
    await callback.answer()

# About section: 
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

# Telegram channel url:
@dp.callback_query(F.data == "join")
async def join(callback: CallbackQuery):
    lang = user_languages.get(callback.from_user.id, "en")

    await callback.message.answer(
        reply_markup=back_menu(lang)
    )
    await callback.answer()

# Contact section:
@dp.callback_query(F.data == "contact")
async def contact(callback: CallbackQuery):
    lang = user_languages.get(callback.from_user.id, "en")
    contact_text = translations["contact"][lang]

    text_contact = contact_text.format(
        admin=settings.LEAD_ADMIN_USERNAME,
        website="Not Available atm"
    )

    await callback.message.edit_text(
        text=text_contact,
        reply_markup=back_menu(lang)
    )
    await callback.answer()

# Links section: 
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

# Links back to main menu handler:
@dp.callback_query(F.data == "back")
async def back(callback: CallbackQuery):
    lang = user_languages.get(callback.from_user.id, "en")

    menu_back = translations["back_menu_text"][lang]

    await callback.message.edit_text(
        text=menu_back,
        reply_markup=main_menu(lang)
    )
    await callback.answer()

# Back to menu handler:
@dp.callback_query(F.data == "back_menu")
async def back(callback: CallbackQuery):
    lang = user_languages.get(callback.from_user.id, "en")

    text = translations["back_menu_text"][lang]

    await callback.message.edit_text(
        text=text,
        reply_markup=main_menu(lang),
    )
    await callback.answer()

# Non-command message handler
@dp.message()
async def no_text(message: Message):
    lang = user_languages.get(message.from_user.id, "en")
    reply_text = translations["no_text_allowed"][lang]
    if not message.text.startswith("/"):
        await message.answer(
            text=reply_text,
            reply_markup=language_menu()
        )