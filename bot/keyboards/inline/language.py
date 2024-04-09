from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.i18n import gettext as _
from aiogram.utils.keyboard import InlineKeyboardBuilder


def language_keyboard() -> InlineKeyboardMarkup:
    """Use in main menu."""
    buttons = [
        [InlineKeyboardButton(text=_("ru"), callback_data="lang_ru")],
        [InlineKeyboardButton(text=_("en"), callback_data="lang_en")],
        [InlineKeyboardButton(text=_("uk"), callback_data="lang_uk")],
    ]

    keyboard = InlineKeyboardBuilder(markup=buttons)

    # keyboard.adjust(1, 1, 2)

    return keyboard.as_markup()
