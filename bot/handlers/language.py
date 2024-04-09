from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.utils.i18n import gettext as _
from bot.services.users import set_language_code
from bot.keyboards.inline.language import language_keyboard
from bot.keyboards.inline.menu import main_keyboard
from bot.handlers.menu import menu_handler
from sqlalchemy.ext.asyncio import AsyncSession
from bot.core.loader import i18n

router = Router(name="language")


@router.callback_query(F.data.startswith("language"))
async def language_handler(callback_query: types.CallbackQuery) -> None:
    await callback_query.message.answer(
        _("choose language"), reply_markup=language_keyboard()
    )


@router.message(Command(commands=["language", "lang"]))
async def language_handler(message: types.Message) -> None:
    await message.answer(_("choose language"), reply_markup=language_keyboard())


@router.callback_query(F.data.startswith("lang_"))
async def set_language(callback_query: types.CallbackQuery, session: AsyncSession):
    language = callback_query.data[len("lang_") :]
    await set_language_code(
        session=session, user_id=callback_query.from_user.id, language_code=language
    )
    i18n.current_locale = language
    await callback_query.message.edit_text(_(f'Language changed to {language}'),reply_markup=main_keyboard())
