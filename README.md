![pipline](gitlab.crja72.ru:django_2023/students/144959-efimkafeed-47231.git/badges/main/pipeline.svg)

# Создание и включение venv:
```sh
python -m venv venv
source venv/bin/activate
```

# Установка зависимостей:
```sh
pip install -r requirements/prod.txt
```

# Файл .env
### Откройте файл "test.env" в lyceum/lyceum и впишите в переменню "SECRET_KEY" свой ключ

# Включение сервера:
```sh
cd lyceum
python manage.py runserver
```
