# from gc import callbacks
# from email import message
# from gc import callbacks
from email import message
import telebot
from telebot.types import KeyboardButton,InlineKeyboardButton,ReplyKeyboardMarkup,InlineKeyboardMarkup
import json



TOKEN = "5614084933:AAEGEhavvDUC9eWA9YNh4WXBLyAU0zGLIgg"
bot = telebot.TeleBot(TOKEN,parse_mode=None)

my_dict = {

}
def file_open():
    global my_dict
    with open('my_json.json','r') as f:
        my_dict = json.load(f)
    # return my_dict  
file_open()

def file_save():
    global my_dict
    with open("my_json.json","w",encoding="utf-8") as f:
        json.dump(my_dict,f)

# my_dict["101004"]["dollar"] += 10
# file_save()


@bot.message_handler(commands=['start'])
def my_func(message):
    # bot.send_message(message.chat.id,"salom")
    # markup = ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
    # aboylar = KeyboardButton("Aboylar")  
    # lustiralar = KeyboardButton("Lustra")
    # markup.add(aboylar,lustiralar)  
    bot.send_message(message.chat.id,f' Salom {message.from_user.first_name} Botimizga hush kelibsiz!')  
    bot.send_message(message.chat.id,"Search ...")
    
    print(message.from_user.first_name)
    # bot.send_message(message.chat.id,"Parolni kirgizing -- ")
    # if message.text == "1":
    #     bot.send_message(message.chat.id,"Search ...")
    # else:
    #     bot.send_message(message.chat.id,"parol xato")    

        
# def file_save():
#     global my_dict
#     with open("my_json.json","w",encoding="utf-8") as f:
#         json.dump(my_dict,f) 
#         print(my_dict)
# file_save()        
# def file_open():
#     global my_dict
#     with open("my_json.json","r",encoding="utf-8") as file:
#         my_dict = json.loads(file) 
#         print(my_dict
# file_open()
@bot.message_handler(content_types=['text'])
def text(message):
    for item in my_dict:
        # print(my_dict[item])
        if message.text == item:
            markup = InlineKeyboardMarkup(row_width=2)
            markup.add(InlineKeyboardButton("+",callback_data = '+,'+ message.text),
                InlineKeyboardButton("-",callback_data = '-,'+ message.text),
                InlineKeyboardButton("++",callback_data = '++,'+ message.text),
                InlineKeyboardButton("--",callback_data = '--,'+ message.text),
                InlineKeyboardButton("Narxi",callback_data = 'Narxi,' + message.text))
    # markup.add(InlineKeyboardButton("Foyda",callback_data = 'Foyda'))


            bot.send_message(message.chat.id,"tugmacha yondi !!!",reply_markup=markup)
            bot.send_message(message.chat.id,my_dict[item]["model"] + "=" + str(my_dict[item]["count"]))
                

@bot.callback_query_handler(func=lambda call: True)
def azamat_callback(call): # <- passes a CallbackQuery type object to your function
    change_click = call.data.split(',')   
    # print(str(change_click[1]))
    # print(change_click)
    # print(mess)
    if (change_click[0] == '+'):
        my_dict[str(change_click[1])]["count"] += 1
        bot.send_message(call.from_user.id,str(my_dict[str(change_click[1])])) 
    elif (change_click[0] == '-'):
        my_dict[str(change_click[1])]["count"] -= 1  
        bot.send_message(call.from_user.id,str(my_dict[str(change_click[1])])) 
    elif (change_click[0] == 'Narxi'):
        bot.send_message(call.from_user.id,str(my_dict[str(change_click[1])]["narxi"])+"$")
    elif (change_click[0] == '++'):
        # my_dict[str(change_click[1])]["count"] += 1
        markup = InlineKeyboardMarkup(row_width=2)
        markup.add(InlineKeyboardButton("2",callback_data = '2,'+change_click[1]),
        InlineKeyboardButton("5",callback_data = '5,'+change_click[1]),
        InlineKeyboardButton("10",callback_data = '10,'+change_click[1]),
        InlineKeyboardButton("50",callback_data = '50,'+change_click[1]),
        InlineKeyboardButton("100",callback_data = '100,'+change_click[1])
        )
        # print(change_click[1])
        bot.send_message(call.from_user.id,"tugmacha yondi !!!",reply_markup=markup)
    elif (change_click[0] == '--'):
        # my_dict[str(change_click[1])]["count"] += 1
        markup = InlineKeyboardMarkup(row_width=2)
        markup.add(InlineKeyboardButton("3",callback_data = '3,'+change_click[1]),
        InlineKeyboardButton("6",callback_data = '6,'+change_click[1]),
        InlineKeyboardButton("9",callback_data = '9,'+change_click[1]),
        InlineKeyboardButton("49",callback_data = '49,'+change_click[1]),
        InlineKeyboardButton("99",callback_data = '99,'+change_click[1])
        )
        # print(change_click[1])
        bot.send_message(call.from_user.id,"tugmacha yondi !!!",reply_markup=markup)        
    change_ = call.data.split(',')   
    if (change_click[0] == "2"):
        my_dict[str(change_[1])]["count"] += 2  
        bot.send_message(call.from_user.id,str(my_dict[str(change_click[1])])) 
    elif (change_click[0] == "5"):
        my_dict[str(change_[1])]["count"] += 5
        bot.send_message(call.from_user.id,str(my_dict[str(change_click[1])])) 
    elif (change_click[0] == "10"):
        my_dict[str(change_[1])]["count"] += 10
        bot.send_message(call.from_user.id,str(my_dict[str(change_click[1])]))           
        # print(change_[1])
    elif (change_click[0] == "50"):
        my_dict[str(change_[1])]["count"] += 50
        bot.send_message(call.from_user.id,str(my_dict[str(change_click[1])])) 
    elif (change_click[0] == "100"):
        my_dict[str(change_[1])]["count"] += 100
        bot.send_message(call.from_user.id,str(my_dict[str(change_click[1])]))    

    if (change_click[0] == "3"):
        my_dict[str(change_[1])]["count"] -= 3 
        bot.send_message(call.from_user.id,str(my_dict[str(change_click[1])])) 
    elif (change_click[0] == "6"):
        my_dict[str(change_[1])]["count"] -= 6
        bot.send_message(call.from_user.id,str(my_dict[str(change_click[1])])) 
    elif (change_click[0] == "9"):
        my_dict[str(change_[1])]["count"] -= 9   
        bot.send_message(call.from_user.id,str(my_dict[str(change_click[1])]))        
        # print(change_[1])
    elif (change_click[0] == "49"):
        my_dict[str(change_[1])]["count"] -= 49
        bot.send_message(call.from_user.id,str(my_dict[str(change_click[1])])) 
    elif (change_click[0] == "99"):
        my_dict[str(change_[1])]["count"] -= 99   
        bot.send_message(call.from_user.id,str(my_dict[str(change_click[1])])) 
    
    if my_dict[str(change_[1])]["count"] <= 0:
        bot.send_message(call.from_user.id,"Bu mahsulot qolmadi")
    # file_open() 
    file_save()
#         my_dict[str(change_click[1])]["count"] += 1
#     bot.send_message(call.from_user.id,str(my_dict[str(change_click[1])]))

bot.polling()
