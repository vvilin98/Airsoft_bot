import telebot
import threading
import pytz
import schedule
import time
import datetime


bot = telebot.TeleBot('token_bot')
chat_id = 'id_chat'  # type int
message_thread_id = 'id_topic_chat'  # type int


@bot.message_handler(commands=['start', 'help'])
def handle_start(message):
    if message.text == '/start':
        bot.reply_to(message, 'Привет! Я бот команды "Name".\n'
                              'Если хочешь узнать что я могу напиши /help. Если итак знаешь, то давай общаться!')
    elif message.text == '/help':
        bot.reply_to(message, 'Мои команды:\n'
                              '1./start\n'
                              '2./help\n'
                              '3.Привет\n'
                              '4.Хочу опрос\n'
                              '5./time')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == "привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == 'Хочу опрос':
        now = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
        next_sunday = now + datetime.timedelta(days=(6 - now.weekday() + 7) % 7)
        message_1 = ("Привет! На предстоящую воскреску поедет кто?\n"
                     "[ВТК Домодедово 'Патриот'](https://vk.com/airsoft_pd), [Адресс](https://yandex.ru/navi/org/188677143622)")
        bot.send_message(message.from_user.id, message_1, parse_mode='Markdown', disable_web_page_preview=True)
        question = f"Кто поедет на игру {next_sunday.strftime('%d.%m')} 12:00 (в вскр)"
        options = ["Да", "Нет", "Не знаю"]
        bot.send_poll(message.from_user.id, question=question, options=options, is_anonymous=False)
    elif message.text == '/time' or 'воскресная игра' in message.text:
        now = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
        next_sunday = now + datetime.timedelta(days=(6 - now.weekday() + 7) % 7)
        message_2 = (f"Привет! Ближайший наш выезд будет {next_sunday.strftime('%d.%m')} "
                     f"Полигон 'Домодедово' [Адрес](https://yandex.ru/navi/org/188677143622)")
        bot.send_message(message.from_user.id, message_2, parse_mode='Markdown', disable_web_page_preview=True)

    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


def schedule_func_1():
    now = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
    next_sunday = now + datetime.timedelta(days=(6 - now.weekday() + 7) % 7)
    message_1 = ("Привет! На предстоящую воскреску поедет кто?\n"
                 "[ВТК Домодедово 'Патриот'](https://vk.com/airsoft_pd), [Адрес](https://yandex.ru/navi/org/188677143622)")
    bot.send_message(chat_id, message_1, message_thread_id=message_thread_id, parse_mode='Markdown', disable_web_page_preview=True)
    question = f"Кто поедет на игру {next_sunday.strftime('%d.%m')} 12:00 (в вскр)?"
    options = ["Да", "Нет", "Не знаю"]
    bot.send_poll(chat_id, message_thread_id=message_thread_id, question=question, options=options, is_anonymous=False)


def foo():
    schedule.every().saturday.at("09:25").do(schedule_func_1)
    while True:
        schedule.run_pending()
        time.sleep(1)


def main():
    thread = threading.Thread(target=foo)
    thread.start()
    bot.polling(none_stop=True)


if __name__ == '__main__':
    main()
