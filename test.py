from selenium import webdriver

# Настройка ChromeOptions
options = webdriver.ChromeOptions()
# Добавление headless опции
options.add_argument("--headless=new")
# Запуск Chrome в headless режиме
driver = webdriver.Chrome(options=options)

# Открытие целевого сайта
driver.get("https://dnevnik.ru/")

# Проверка работы
print(f"URL страницы: {driver.current_url}")
print(f"Заголовок: {driver.title}")
print(f"Заголовок: {driver.}")

# Закрытие драйвера
driver.quit()
