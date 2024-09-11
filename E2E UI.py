from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Настройка WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Открытие страницы SauceDemo
driver.get('https://www.saucedemo.com/')

# Шаг 1: Авторизация
username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

# Вводим логин и пароль
username.send_keys("standard_user")
password.send_keys("secret_sauce")

# Нажимаем кнопку входа
login_button.click()

# Шаг 2: Выбор товара и добавление в корзину
time.sleep(2)  # Задержка для загрузки страницы
item = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
item.click()

# Шаг 3: Переход в корзину и проверка наличия товара
cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
cart.click()

time.sleep(2)  # Задержка для загрузки корзины
cart_item = driver.find_element(By.CLASS_NAME, "inventory_item_name")
assert cart_item.text == "Sauce Labs Backpack", "Товар в корзине не соответствует ожидаемому"

# Шаг 4: Оформление покупки
checkout_button = driver.find_element(By.ID, "checkout")
checkout_button.click()

# Заполнение полей для оформления заказа
first_name = driver.find_element(By.ID, "first-name")
last_name = driver.find_element(By.ID, "last-name")
postal_code = driver.find_element(By.ID, "postal-code")

first_name.send_keys("Test")
last_name.send_keys("User")
postal_code.send_keys("12345")

# Нажимаем "Продолжить"
continue_button = driver.find_element(By.ID, "continue")
continue_button.click()

# Шаг 5: Завершение покупки
finish_button = driver.find_element(By.ID, "finish")
finish_button.click()

# Шаг 6: Проверка успешного завершения покупки
confirmation_message = driver.find_element(By.CLASS_NAME, "complete-header")
assert confirmation_message.text == "Thank you for your order!", "Покупка не была завершена успешно"

# Завершение работы WebDriver
driver.quit()
