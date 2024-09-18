import random

#text to insert in greeting
greeting_text = ("Привет, {}!{}\nЯ помогу найти тебе фильм или сериал по твоему запросу\n\n{}"
                 "Выбери, что ты хочешь найти:\n\n{} фильм или сериал по названию\n{}" 
                 "топ-10 фильмов по стране\n{} топ-10 фильмов определённого жанра")
greeting_emoji = ["\U00002753", "\U0001F3A5", "\U0001F30D", "\U0001F3AD"]
name_emoji = ["\U0001F493", "\U0001F493", "\U0001F495", "\U0001F496", "\U0001F497", 
              "\U0001F498", "\U0001F499","\U0001F49A", "\U0001F49B", "\U0001F49C", "\U0001F49E"]

#produce greeting text according to user's name
def greeting_builder(username, first_name):
    if username == "llenovo":
        return greeting_text.format(first_name, "\U0001F34C", *greeting_emoji)
    elif username == "renallin":
        return greeting_text.format(first_name, "\U0001F423", *greeting_emoji)
    elif username == "yekate228":
        return greeting_text.format(first_name, "\U00002603", *greeting_emoji)
    elif username == "fbuzaev":
        return greeting_text.format(first_name, "\U0001F37B", *greeting_emoji)
    elif username == "Palladain":
        return greeting_text.format(first_name, "\U0001F99C", *greeting_emoji)
    else:
        heart = random.choice(name_emoji)
        return greeting_text.format(first_name, str(heart), *greeting_emoji)
    
check_typos = "Я не нашел такой фильм\U0001F972. Проверь правильность написания пожалуйста\U0000263A"

cannot_handle = ("Такой команды я не знаю \U0001F622\nПроверь правильность написанной команды" 
                 " или просто нажми на /start, чтобы начать работать со мной")

check_satisfaction = ("/link - Супер! Хочу ссылку!\n\n/another - Не тот фильм, " 
                      "введу название ещё раз\n\n/restart - Хочу найти вообще другое")

want_another_option = "/restart - Хочу выбрать другую опцию"