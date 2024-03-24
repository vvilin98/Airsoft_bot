#
### Airsoft bot 
Создавался для отправки сообщение с опросом раз в неделю в нужный чат. В будущем будем дополняться различными фичами.

Перед работой с ботом требуется :

1. Уставновить зависимости 
```bash
pip install -r requirements.txt
```
2. Добавить бота в требуемый чат 
3. Проставить в переменную `bot` токен своего бота
3. Проставить в переменную `chat_id` id чата/группы/канала
4. Проставить в переменную `message_thread_id` id топика/подгруппы (если требуетсы)

Чтобы узнать id из пунктов 3,4 можно воспользоваться данной заготовкой (обязательное условие шаг 2 done)
> После добавлении бота в канал, при написании сообщения в чате или в одном из топиков чата,
бот отправляет в ответ на отправленное сообщение требуемые id чата и топика откуда было направлено сообщение.
``` python
@bot.message_handler(func=lambda message: True)
def echo_message(message):
     chat_id = message.chat.id
     try:
        msg_thread_id = message.reply_to_message.message_thread_id
     except AttributeError:
        msg_thread_id = "General"
     bot.reply_to(message, f"Chat ID этого чата: {chat_id}\nИ message_thread_id: {msg_thread_id}")
```
