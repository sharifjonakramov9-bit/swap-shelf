from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import CallbackContext

from apps.users.models import User

Menu_Keyboard = [
    ['🏠 Bosh sahifa', '📚 Mening kitoblarim'],
    ['🔍 Kitoblarni qidirish', '📥 Menga kelgan so‘rovlar'],
    ['📤 Yuborgan so‘rovlar', '🔄 Almashuvlarim'],
    ['🔢 OTP kod olish', '🔔 Bildirishnomalar'],
    ['👤 Profilim', '❓ Yordam'],
]

def contact_save(update: Update, context: CallbackContext):
    contact = update.message.contact
    contact_user_id = update.message.contact.user_id
    telegram_id = update.message.from_user.id
    
    user = User.objects.filter(telegram_id=telegram_id, phone=contact.phone_number).first()
    if user:
        print(f'User {user} with phone number {contact.phone_number} already exists in database.')
        return
    else:
        user = User.objects.filter(telegram_id=telegram_id).first()
    
    if contact_user_id != telegram_id:
        print(f'Contact user_id {contact_user_id} does not match telegram_id {telegram_id}. Ignoring contact.')
        return
    
    user.phone = contact.phone_number
    user.save()
    
    update.message.reply_text(
        'Telefon raqamingiz saqlandi!',
        parse_mode='Markdown',
        reply_markup=ReplyKeyboardMarkup(
            Menu_Keyboard,
            resize_keyboard=True,
        )
    )