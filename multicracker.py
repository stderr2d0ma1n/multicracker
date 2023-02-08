from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import urlparse
import time
import argparse
import datetime
import os


# Создание и получение аргументов

parser = argparse.ArgumentParser()
parser.add_argument(
    '-xl', '--x_login', default=None,
    type=str, help='Provide xpath for username field with single quotes'
)
parser.add_argument(
    '-xp', '--x_password', default=None,
    type=str, help='Provide xpath for password field with single quotes'
)
parser.add_argument(
    '-xb', '--x_button', default=None,
    type=str, help='Provide xapth for button/submit with single quotes'
)
parser.add_argument(
    '-l', '--login', default=None,
    type=str, help='Provide username for auth'
)
parser.add_argument(
    '-p', '--password', default=None,
    type=str, help='Provide password for auth'
)
parser.add_argument(
    '-ul', '--url_list', default=None,
    type=str, help='Provide testing URL list'
)
parser.add_argument(
    '-o', '--output', default=datetime.datetime.now().strftime("%d-%m-%Y_%H:%M"),
    type=str, help='Provide output directory'
)
args = parser.parse_args()

# Таймаут
timeout = 2
# Инициалазация браузера
driver = webdriver.Firefox()

if args.url_list:
    with open(args.url_list, "r") as url_file:
        for url in url_file:
            driver.get(url)
            time.sleep(timeout)
            # Получение элементов ввода и кнопки
            username_field = driver.find_element(By.XPATH, args.x_login)
            password_field = driver.find_element(By.XPATH, args.x_password)
            submit_button = driver.find_element(By.XPATH, args.x_button)
            # Ввод данных в поле
            username_field.send_keys(args.login)
            password_field.send_keys(args.password)
            submit_button.click()
            # Создание скриншота и вывод
            output_domain = urlparse(url).netloc
            os.mkdir(args.output)
            driver.save_screenshot(args.output + '/' + output_domain + '.png')
            time.sleep(timeout)
else:
    print("[!] - Enter URL list")
