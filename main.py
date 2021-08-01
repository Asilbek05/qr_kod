import os
import telebot
from telebot import types

#Request to the system to receive a variable token
TOKEN =''
bot = telebot.TeleBot(TOKEN)

#Picture output function
def out_qr(in_t,in_c,in_q,mci):
    markup = types.ReplyKeyboardRemove()
    out_url = 'http://api.qrserver.com/v1/create-qr-code/?size=512x512&margin=5&data='+in_t+'&color='+in_c+'&ecc='+in_q
    markup = types.ReplyKeyboardRemove()
    bot.send_photo(mci, out_url, reply_markup=markup, caption='Sizning Qr kodinggiz\n\nSIZ KIRITGAN MATN: {}\n\n Kanalimiz: @robocontest_uz\n\nCretor: @Asilbek_developer_oo1. \n\nYana qr kod yasamoqchi bo`lsanggiz  /running buyrug`ini tanlab yasashinggiz mumkin!!!'.format(in_t))

#Commands for calling /start and /help
@bot.message_handler(commands=['start', 'running','help'])
def send_welcome(message):
    markup = types.ReplyKeyboardRemove()
    if message.text == '/start':
        welcome_photo = open('welcome.png','rb')
        out_start = f"Salom {message.from_user.first_name}.\n\nMenga text yoki url jo'natsanggiz men sizga har xil turdagi va har xil rangdagi QR kod yasab beraman.\n\nBotni ishlatish  uchun 👉 /running 👈  buyru'gini bosishinggiz kerak yoki /help burug`ini bosib botni qanday qilib ishlatishni ko'rib chiqishinggiz mumkin!!!\n\nKanalimiz 👉👉👉 @robocontest_uz"
        bot.send_photo(message.from_user.id,welcome_photo,caption=out_start,reply_markup=markup)
    if message.text == '/running':
        out_start = "Yaxshi . Endi men sizga qanday qilib bu botdan QR kod yasab olishni o'rgataman!!!\n\n"
        out_start += "1) - Matn yoki URL matn kiritamiz - *Salom Dunyo*\n"
        out_start += "2) - Bot yasab beradigan QR kod sifatini tanlang  - *Past/O`rta/Sifatli/Yuqori Sifatli*\n"
        out_start += "3) - Endi esa QR kod rangini tanlang - *Qizil/Yashil/Ko`k/Qora/Boshqalar*\n"
        out_start += "4) - Qr kodinggizni yuklab oling\n\n\n*Shartlar tushunarli bo'lgan bo`lsa , text yoki url kiriting va undan keyin bo'limlarni tanlang!!! *"
        bot.send_message(message.chat.id, out_start,parse_mode="Markdown")
    if(message.text=='/help'):
        help_1_photo= open('help_1.png','rb')
        chat_id = message.from_user.id
        
        bot.send_photo(chat_id,help_1_photo, caption="start bo'limini bosgandan so'ng shu xabar chiqadi va siz bu yerdan ko'rsatilgan joyni ustiga bosasiz!!!\n\n@Asilbek_developer_oo1")
        
        help_2_photo= open('help_2.png','rb')
        bot.send_photo(chat_id,help_2_photo, caption="Keyin esa text yoki url jo'natamiz!!!\n\n@Asilbek_developer_oo1")

        help_3_photo= open('help_3.png','rb')
        bot.send_photo(chat_id,help_3_photo, caption="Ko'rsatilgan bo'limlardan birini tanlaymiz(Bu bo'lim Qr kodinggiz qanchalik maxfiy bo'lishi uchun)!!!\n\n@Asilbek_developer_oo1")

        help_5_photo= open('help_5.png','rb')
        bot.send_photo(chat_id,help_5_photo, caption="Ko'rsatilganlardan birini tanlaymiz(Ranglar)!!!\n\n@Asilbek_developer_oo1")

        help_4_photo= open('help_4.png','rb')
        bot.send_photo(chat_id,help_4_photo, caption="Mana qr kodimiz tayyor bo'ldi va yana running ni bosib yana qr kod tayyorlashinggiz mumkin!!!\n\n@Asilbek_developer_oo1")
#Commands to process the received data from the telegram
@bot.message_handler(content_types = ['text'])
def send_text(message):
    
    ms_quality = ('Past', 'O`rta', 'Sifatli', 'Yuqori Sifatli')
    ms_color = ('Qizil', 'Yashil', 'Ko`k', 'Qora')
    global in_text
    global in_quality
    global in_color 
    if message.text in ms_quality:
        in_quality = message.text
        in_quality = in_quality[0]  
        markup = types.ReplyKeyboardMarkup(row_width=5, resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Qizil')
        itembtn2 = types.KeyboardButton('Yashil')
        itembtn3 = types.KeyboardButton('Ko`k')
        itembtn4 = types.KeyboardButton('Qora')
        itembtn5 = types.KeyboardButton('Boshqalar')
        markup.add(itembtn1, itembtn2, itembtn3,itembtn4,itembtn5)
        bot.send_message(message.chat.id, "QR kodning rangini tanlang", reply_markup=markup)
    
    #3 - got the color value of QR-Code
    elif message.text in ms_color:
        in_color = message.text
        if in_color == 'Qizil':
            in_color = 'FF0000'
        elif in_color == 'Yashil':
            in_color = '00FF00'
        elif in_color == 'Ko`k':
            in_color = '0000FF'
        elif in_color == 'Qora':
            in_color = '000000'
        out_qr(in_text,in_color,in_quality,message.chat.id)

    #4 - custom color request
    elif message.text == 'Boshqalar':
        markup = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, "HTML HEX formatida rangingizni kiriting", reply_markup=markup)

    #5 - output QR Code with custom color
    elif message.text[0] == '#':
        in_color = message.text[1:]
        out_qr(in_text,in_color,in_quality,message.chat.id)

    #1 - came plain text...
    else :
        in_text = message.text
        markup = types.ReplyKeyboardMarkup(row_width=4, resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Past')
        itembtn2 = types.KeyboardButton('O`rta')
        itembtn3 = types.KeyboardButton('Sifatli')
        itembtn4 = types.KeyboardButton('Yuqori Sifatli')
        markup.add(itembtn1, itembtn2, itembtn3,itembtn4)   
        bot.send_message(message.chat.id, "QR kod sifatini tanlang", reply_markup=markup)

bot.polling(timeout = 60)
