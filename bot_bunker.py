import requests
import telebot
from telebot import types


def upd():
    info2 = requests.get("https://randomall.ru/api/custom/gen/758/")
    info = info2.json()
    return info['text']


def obr():
    resp = res[:res.index('Карта') - 1] + ';' + res[res.index('Карта') - 1:]
    lst = resp.split(';')
    num = 0
    for i in lst:
        ii = i.rstrip()
        lst[num] = ii.split(':')
        num += 1
    for par in lst[:-1]:
        if par[0][0] == '\n':
            par[0] = par[0][1:]
        if par[1][0] == ' ':
            par[1] = par[1][1:]
        if par[0] in x:
            if par[1] not in x[par[0]]:
                x[par[0]].append(par[1])
        else:
            x[par[0]] = [par[1]]


x = {}
res = upd()
bot = telebot.TeleBot('1258279495:AAHyGtr00uahTB0C7oql2LkchosKlEiDRek')


@bot.message_handler(content_types=['text'])
def randoma(message):
    if message.text == 'Рандом':
        final = upd()
    else:
        final = 'Хотите сыграть?'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        butt = types.KeyboardButton('Рандом')
        markup.add(butt)
        send_messs = 'Что-то пошло не так'
        bot.send_message(message.chat.id, send_messs, parse_mode='html', reply_markup=markup)
    bot.send_message(message.chat.id, final, parse_mode='html')


@bot.message_handler(commands=['start'])
def start(message):
    send_messs = 'Хотите сыграть?'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    butt = types.KeyboardButton('Рандом')
    markup.add(butt)
    bot.send_message(message.chat.id, send_messs, parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)
