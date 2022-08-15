import json
import urllib.request
from random import randint

import requests
import xmltodict
from bs4 import BeautifulSoup


def humor():
    """
    1 - Анекдот;
    2 - Рассказы;
    3 - Стишки;
    4 - Афоризмы;
    5 - Цитаты;
    6 - Тосты;
    8 - Статусы;
    11 - Анекдот (+18);
    12 - Рассказы (+18);
    13 - Стишки (+18);
    14 - Афоризмы (+18);
    15 - Цитаты (+18);
    16 - Тосты (+18);
    18 - Статусы (+18);
    """

    response = requests.get("http://rzhunemogu.ru/Rand.aspx?CType=2")
    humor_text_xml = xmltodict.parse(response.text)
    humor_text_output = humor_text_xml["root"]["content"]
    return str(humor_text_output)


"""""" """""" """""" """""" """""" """""" """''

""" """""" """""" """""" """""" """""" """""" ""


def random_cat():
    num = int(randint(0, 1600))
    source = requests.get(f"https://aws.random.cat/view/{num}").text
    image = source.split('src="')[1].split('"')[0]
    return image


def nasa_apod():
    response = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
    nasa_photo_url = json.loads(response.text)["url"]
    nasa_photo_title = json.loads(response.text)["title"]
    image = [nasa_photo_url, nasa_photo_title]
    return image


def nasa_epic():
    response = requests.get("https://epic.gsfc.nasa.gov/api/images.php")
    nasa_photo_url = json.loads(response.text)[-1]["image"]
    nasa_photo_cap = json.loads(response.text)[-1]["caption"]
    image = [
        "https://epic.gsfc.nasa.gov/epic-archive/jpg/" + nasa_photo_url + ".jpg",
        nasa_photo_cap,
    ]
    return image


def weather():
    """
    https://www.cyberforum.ru/python-web/thread1884117.html
    """

    url = "https://yandex.by/pogoda/zhlobin"
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    yesterday_temp_val = (
        soup.find("div", class_="fact__time-yesterday-wrap")
        .find("span", class_="temp__value " "temp__value_with-unit" "")
        .get_text()
    )
    # print('Вчера в это время: ' + yesterday_temp_val)
    now_temp_val = (
        soup.find("div", class_="temp fact__temp fact__temp_size_s")
        .find("span", class_="temp__value " "temp__value_with-unit" "")
        .get_text()
    )
    # print('Сейчас: ' + now_temp_val)
    feelings_temp_val = (
        soup.find("div", class_="link__feelings fact__feelings")
        .find("span", class_="temp__value " "temp__value_with-unit" "")
        .get_text()
    )
    # print('Ощущается как : ' + feelings_temp_val)
    wind_speed_val = soup.find(
        "div", class_="term term_orient_v fact__wind-speed"
    ).get_text()
    # print('Ветер: ' + wind_speed_val)
    humidity_val = soup.find(
        "div", class_="term term_orient_v fact__humidity"
    ).get_text()
    # print('Влажность: ' + humidity_val)
    pressure_val = soup.find(
        "div", class_="term term_orient_v fact__pressure"
    ).get_text()
    # print('Давление: ' + pressure_val)
    day_duration_val = soup.find(
        "div", class_="sun-card__day-duration-value"
    ).get_text()
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
    weather_val = [
        yesterday_temp_val,
        now_temp_val,
        feelings_temp_val,
        wind_speed_val,
        humidity_val,
        pressure_val,
        day_duration_val,
        sun_rise_val,
        sun_set_val,
        text_info_val,
    ]
    return weather_val

# print(weather())
# print(humor())
# print(nasa_apod())
# print(nasa_epic())
# print(random_cat())
