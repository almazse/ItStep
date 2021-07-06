import telebot
import config
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(executable_path='drivers/chromedriver', options=options)

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def main(message):
    URL = "https://sinoptik.ua/погода-скадовск"
    driver.get(URL)
    weather = driver.find_element_by_css_selector('div#blockDays')
    min_temp = driver.find_element_by_css_selector('.temperature .min').text.strip().replace('\n', ' ')
    max_temp = driver.find_element_by_css_selector('.temperature .max').text.replace('\n', ' ')
    description = driver.find_element_by_css_selector('.wDescription .description').text

    print(min_temp, max_temp, description)
    bot.send_message(message.chat.id, f'{min_temp}\n{max_temp}\n{description}')


bot.polling()
