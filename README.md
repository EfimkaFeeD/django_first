![pipeline](https://gitlab.crja72.ru/django_2023/students/144959-efimkafeed-47231/badges/main/pipeline.svg)

![](https://media.tenor.com/m7NouMXotJIAAAAd/komaru-gyost576.gif)

# Для успешного запуска проекта:

## Создание и включение venv:
```sh
python -m venv venv
source venv/bin/activate
```

## Установка зависимостей для запуска в продакшене:
```sh
pip install -r requirements/prod.txt
```

![](https://media.tenor.com/i-sLmV90tBsAAAAd/%D0%BA%D0%BE%D0%BC%D0%B0%D1%80%D1%83.gif)

## Установка зависимостей для разработки:
```sh
pip install -r requirements/dev.txt
```

## Установка зависимостей для запуска тестов:
```sh
pip install -r requirements/test.txt
```

![](https://media.tenor.com/X7ZIAriTQpMAAAAC/%D0%BA%D0%BE%D0%BC%D0%B0%D1%80%D1%83-%D1%80%D0%BE%D0%B1%D0%BE%D0%BA%D1%81%D1%85%D1%85%D1%85.gif)

## Файл .env
#### Переименуйте файл "test.env" по пути lyceum/lyceum в ".env" и впишите в переменню "SECRET_KEY" свой ключ

![](https://media.tenor.com/V8Y0245j3YEAAAAC/komaru-cat.gif)

## python manage.py thumbnail clear
#### Команда нужно чтобы корректно отобразились все картинки, ниже указан порядок ввода

## Включение сервера:
```sh
cd lyceum
python manage.py thumbnail clear
python manage.py runserver
```

![](https://media.tenor.com/v6eBVD_YBfEAAAAd/komaru-cat.gif)

# О сайте:

## Структура базы данных
![](ER.jpg)

![](https://media.tenor.com/HENtA3Ut954AAAAd/%D0%BA%D0%BE%D0%BC%D0%B0%D1%80%D1%83.gif)

## Мультиязычность
#### Сайт умеет в русский и английский языки
#### Для создания перевода воспользуйтесь

```sh
django-admin compilemessages
```

## Фикстурчики
#### Лежат в lyceum/fixtures/, стараюсь держать актуальными


З.Ы. 000 дробь это очень-очень локальный мем, поэтому название не случайно :D

![](https://media.tenor.com/96C4AbebWDQAAAAd/%D0%BA%D0%BE%D0%BC%D0%B0%D1%80%D1%83-%D0%BA%D0%BE%D1%82.gif)
