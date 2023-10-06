![pipeline](https://gitlab.crja72.ru/django_2023/students/144959-efimkafeed-47231/badges/main/pipeline.svg)

# Создание и включение venv:
```sh
python -m venv venv
source venv/bin/activate
```

# Установка зависимостей для запуска в продакшене:
```sh
pip install -r requirements/prod.txt
```

# Установка зависимостей для разработки:
```sh
pip install -r requirements/dev.txt
```

# Установка зависимостей для запуска тестов:
```sh
pip install -r requirements/test.txt
```

# Файл .env
### Переименуйте файл "test.env" по пути lyceum/lyceum в ".env" и впишите в переменню "SECRET_KEY" свой ключ

# Включение сервера:
```sh
cd lyceum
python manage.py runserver
```
