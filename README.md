# Интерактивная карта интересных мест

Проект позволяет добавлять на карту интересные места с их подробным описанием и фотографиями

[Сайт](https://vitia.pythonanywhere.com/) проекта

## Установка проекта

- Необходимо установить интерпретатор python версии 3.10
- Cкопировать содержимое проекта к себе в рабочую директорию
- Активировать внутри рабочей директории виртуальное окружение:

```
python -m venv [название окружения]
```

- Установить зависимости(необходимые библиотеки):

```
pip install -r requirements.txt
```

- Создать базу данных:

```python
python manage.py migrate
```

- Подключить учетную запись администратора сайта:

```python
python manage.py createsuperuser
```

### Настройка переменных окружения:

- Для хранения переменных окружения создаем файл .env:

```
touch .env
```

1. Секретный ключ проекта: 

```
python manage.py shell
```

```
from django.core.management.utils import get_random_secret_key  

get_random_secret_key()
```

```
echo "DJANGO_SECRET_KEY"=<сгенерированный ключ проекта>" >> .env
```

2. Настройка дебага:  

Для разработки:
```
echo "DEBUG"=1 >> .env
```
Для деплоя:
```
echo "DEBUG"=0 >> .env
```


3. Хосты, смотрим [доку](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts):

```
echo "HOSTS"=<список хостов через запятую>" >> .env
```

4. Путь к статике сайта: 

```
echo "DJANGO_STATIC_ROOT_PATH"=<путь к статике>" >> .env
```

## Запуск

```
python manage.py runserver
```


