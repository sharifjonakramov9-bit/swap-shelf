from random import randint

from django.core.cache import cache

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext


Start_Keyboard = [
    ['📞 Telefon raqamni kiritish'],
    ['❓ Yordam'],   
]

Menu_Keyboard = [
    ['🏠 Bosh sahifa'],
    ['📚 Mening kitoblarim'],
    ['🔍 Kitoblarni qidirish'],
    ['📥 Menga kelgan so‘rovlar'],
    ['📤 Yuborgan so‘rovlar'],
    ['🔄 Almashuvlarim'],
    ['🔢 OTP kod olish'],
    ['🔔 Bildirishnomalar]'],
    ['👤 Profilim'],
    ['❓ Yordam'],
]

def start(update: Update, context: CallbackContext):
    
    update.message.reply_text('Salom, botga xush kelibsiz!')
    

def help(update: Update, context: CallbackContext):
    update.message.reply_text('Yordam uchun /help buyrug\'ini bering.')
    

def login(update: Update, context: CallbackContext):
    
    
    
    opt = randint(100000, 999999)
    
    if cache.get(f'{update.message.chat_id}_opt'):
        opt = cache.get(f'{update.message.chat_id}_opt')
    cache.set(f'{update.message.chat_id}_opt', opt, timeout=120)
    
    update.message.reply_text(f'Telefon raqamingizni kiriting:\n{opt}')