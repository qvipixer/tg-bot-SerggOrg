import urllib.request

from bs4 import BeautifulSoup

"""
Yande pogoda Zhlobin
"""

"""https://www.cyberforum.ru/python-web/thread1884117.html"""
url = "https://yandex.by/pogoda/zhlobin"

response = urllib.request.urlopen(url)
html = response.read()
soup = BeautifulSoup(html, "html.parser")
yesterday_temp_val = (
    soup.find("div", class_="fact__time-yesterday-wrap")
    .find("span", class_="temp__value temp__value_with-unit")
    .get_text()
)
# print('Вчера в это время: ' + yesterday_temp_val)
now_temp_val = (
    soup.find("div", class_="temp fact__temp fact__temp_size_s")
    .find("span", class_="temp__value temp__value_with-unit")
    .get_text()
)
# print('Сейчас: ' + now_temp_val)
feelings_temp_val = (
    soup.find("div", class_="link__feelings fact__feelings")
    .find("span", class_="temp__value temp__value_with-unit")
    .get_text()
)
# print('Ощущается как : ' + feelings_temp_val)
wind_speed_val = soup.find(
    "div", class_="term term_orient_v fact__wind-speed"
).get_text()
# print('Ветер: ' + wind_speed_val)
humidity_val = soup.find("div", class_="term term_orient_v fact__humidity").get_text()
# print('Влажность: ' + humidity_val)
pressure_val = soup.find("div", class_="term term_orient_v fact__pressure").get_text()
# print('Давление: ' + pressure_val)
day_duration_val = soup.find("div", class_="sun-card__day-duration-value").get_text()
# print('Световой день: ' + day_duration_val)
sun_rise_val = soup.find(
    "div",
    class_="sun-card__sunrise-sunset-info sun-card__sunrise-sunset-info_value_rise-time",
).get_text()
# print('Восход: ' + sun_rise_val)
sun_set_val = soup.find(
    "div",
    class_="sun-card__sunrise-sunset-info sun-card__sunrise-sunset-info_value_set-time",
).get_text()
# print('Закат: ' + sun_set_val)
text_info_val = soup.find("div", class_="sun-card__text-info").get_text()
# print('Инфо: ' + text_info_val)


"""
Kinopoisk
"""
url = "https://www.kinopoisk.ru/afisha/city/6957/cinema/281384/"
response = urllib.request.urlopen(url)
html = response.read()
soup = BeautifulSoup(html, "html.parser")

val = soup.find_all(
    "div"
)  # .find('span', class_='temp__value temp__value_with-unit').get_text()

print(val)

# print(temp.temperature)
# print(temperature)
import sqlite3

conn = sqlite3.connect("mydatabase.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()

# Создание таблицы
cursor.execute(
    """CREATE TABLE albums
                  (title text, artist text, release_date text,
                   publisher text, media_type text)
               """
)
