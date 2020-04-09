import requests
from bs4 import BeautifulSoup as BS
import telebot
from telebot import types

TOKEN = '1144242422:AAFTVCf6jzmL_Q_7hH-1BI5Z6BriuyI2Jww' # Token из Botfather
url_letters = 'http://www.1000mest.ru/' # Сайт для парсинга

# Настройки и функции для бота
bot = telebot.TeleBot(TOKEN)


# Парсим все название всех городов
r = requests.get('http://www.1000mest.ru/cityA')
html = BS(r.content, 'lxml')
urls_cities = html.find('div', class_='field-item even').find('h4').find_all('a')  # Получаем ссылки на все буквы

city_letters = list()  # Список букв ссылок
city_urls = list()  # Список ссылок на буквы
for i in range(len(urls_cities)):
    city_letters.append(urls_cities[i].get_text())  # Текст ссылок на все буквы
    city_urls.append(urls_cities[i].get('href'))  # Путь ссылки на все буквы

cities_names = list()  # Список списков всех городов на одну букву


def NamesCitiesInitialization():
    for i in range(29):
        req = requests.get(url_letters + city_urls[i])  # Переходим по ссылке буквы
        req_html = BS(req.content, 'lxml')  # Парсим страницу
        all_table = req_html.find('div', class_='field-item even').find('table').find_all(
            'td')  # Находим таблицу с именами городов
        list_names = list()  # Список где хранится все города с одной буквой
        for i in range(len(all_table)):  # Проходимся по всей строкам таблицы
            list_names.append(all_table[i].get_text())  # Получаем текст строки таблицы
        cities_names.append(list_names)  # Все имена городов в общий список

# Параметры игры
isPlay = False
isFirstInput = False
Answers = list()
CityCount = 0
NextLetter = ''


# Функции для игры "Города"
def AnswersInitialization():  # Создаем список списков, где хранятся названные города по индексам
    for index in range(29):
        Answers.append(list())


def InputAI(word): # Автоматический назвать город после игрока
    index_letter = CheckWord(GetNextLetter(word))
    for index in range(len(cities_names[index_letter])):
        if not CheckNameCity(index_letter, cities_names[index_letter][index]):
            Answers[index_letter].append(cities_names[index_letter][index])
            return cities_names[index_letter][index]
    return False


def CheckNameCity(index, name):  # Проверяем был ли назван город
    return isExist(index, name)


def CheckNameInBase(index, name):  # Проверяем имя города в базе
    for j in range(len(cities_names[index])):
        if name == cities_names[index][j]:
            return True
    return False


def GetNextLetter(name): # Узнаем следующию букву по имени города
    for index in range(len(name)):
        check_letter = name[len(name) - 1 - index].lower()
        if check_letter == 'ё' or check_letter == 'ь' or check_letter == 'ъ' or check_letter == 'ы' or check_letter == ')' or check_letter == '(':
            continue
        return name[len(name) - 1 - index].upper()
    return False


def CheckWord(word):  # Проверяем, есть ли заглавная буква в слове
    for index in range(len(city_letters)):
        if city_letters[index] == word[0]:
            return index
    return -1

def EndGame():
    global isPlay
    global isFirstInput
    global CityCount
    isPlay = False
    isFirstInput = False
    CityCount = 0
    for i in range(29):
        Answers[i].clear()

def isExist(index, name):
    for i in range(len(Answers[index])):
        if Answers[index][i] == name:
            return True
    return False


@bot.message_handler(commands=['start'])  # Функция после команды /start
def welcome(message):
    # Загружаем стикер и отправляем в чат
    stick = open('imgs/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, stick)
    # Создаем клавиатурную кнопку под окном ввода
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton('Начать игру 🏘')
    markup.add(btn)
    # Отправляем сообщение и клавиатуру
    bot.send_message(message.chat.id,
                     "Привет, {0.first_name}!\nЯ - <b>{1.first_name}<b>, бот созданный для игры <b>Города<b>.\nЧтобы начать напишите 'Начать игру'.".format(
                         message.from_user, bot.get_me(), parse_mode='html', reply_markup=markup))


@bot.message_handler(content_types=['text'])
def SendMessage(message):
    global isPlay
    global isFirstInput
    global NextLetter
    city_name = message.text
    if isFirstInput: # Город с которого начнется игра
        index_city = CheckWord(city_name)
        if city_name == 'Завершить':
            bot.send_message(message.chat.id, 'Спасибо за игру (Всего названных городов ' + str(CityCount) + ')')
            EndGame()
            return
        elif index_city == -1: # Проверяем ввод имя города на существующию букву
            bot.send_message(message.chat.id, 'Такого города нет!')
        elif not CheckNameInBase(index_city, city_name):  # Проверяем есть ли такой город
            bot.send_message(message.chat.id, 'Такого города нет!')
        else:
            # Прошли все проверки, засчитываем название города и называем ботом
            CityCount += 1
            Answers[index_city].append(city_name)
            isFirstInput = False
            city_name = InputAI(city_name)
            if not city_name:
                bot.send_message(message.chat.id, 'Города закончились\nСпасибо за игру\n(Всего названных городов ' + str(CityCount) + ')')
                EndGame()
            NextLetter = GetNextLetter(city_name)
            bot.send_message(message.chat.id, 'Напишите город на ' + str(NextLetter))
        return

    if isPlay: # Не первый ввод
        index_city = CheckWord(city_name)
        if city_name == 'Завершить':
            bot.send_message(message.chat.id, 'Спасибо за игру (Всего названных городов ' + str(CityCount) + ')')
            EndGame()
            return
        elif city_name[0] != NextLetter:
            bot.send_message(message.chat.id, 'Нужна на букву ' + str(NextLetter))
        elif index_city == -1:  # Проверяем ввод имя города на существующию букву
            bot.send_message(message.chat.id, 'Такого города нет!')
        elif not CheckNameInBase(index_city, city_name):  # Проверяем есть ли такой город
            bot.send_message(message.chat.id, 'Такого города нет!')
        else:
            # Прошли все проверки, засчитываем название города и называем ботом
            CityCount += 1
            Answers[index_city].append(city_name)
            city_name = InputAI(city_name)
            if not city_name:
                bot.send_message(message.chat.id,
                                 'Города закончились\nСпасибо за игру\n(Всего названных городов ' + str(
                                     CityCount) + ')')
                EndGame()
                return
            bot.send_message(message.chat.id, city_name)
            NextLetter = GetNextLetter(city_name)
            bot.send_message(message.chat.id, 'Напишите город на ' + str(NextLetter))
        return

    if message.text == 'Начать игру 🏘' or message.text == 'Начать игру':
        isPlay = True
        isFirstInput = True
        bot.send_message(message.chat.id, 'Введите любой город')
    else:
        bot.send_message(message.chat.id, 'Неизвестная команда')

# Main
NamesCitiesInitialization()
AnswersInitialization()
# Запуск telebot
bot.polling()


