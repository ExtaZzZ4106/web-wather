# web-wather

# Django Weather App

## Описание проекта
Django-приложение для получения и отображения текущей погоды в заданном городе с использованием API OpenWeatherMap.

## Функционал
- Получение данных о погоде по названию города.
- Отображение температуры, скорости ветра, влажности, видимости и других параметров.
- Поддержка описания погодных условий на русском языке.
- Определение иконок погоды в зависимости от условий и времени суток.

## Установка и настройка

### 1. Клонирование репозитория
```bash
git clone https://github.com/ExtaZzZ4106/web-wather.git
```

### 2. Создание и активация виртуального окружения
```bash
python -m venv venv
source venv/bin/activate  # для Linux и macOS
venv\Scripts\activate  # для Windows
```

### 3. Установка зависимостей
```bash
pip install django requests 
```

### 4. Настройка переменных окружения
Создайте файл `.venv` в корневой директории и добавьте ваш API-ключ OpenWeatherMap:
```
OPENWEATHER_API_KEY=your_api_key_here
```

### 5. Запуск сервера
```bash
python manage.py runserver
```

После запуска сервер будет доступен по адресу:
```
http://127.0.0.1:8000/
```
## API Используемые
Приложение использует API OpenWeatherMap:
```
https://api.openweathermap.org/data/2.5/weather?q={city}&lang=ru&units=metric&appid={API_KEY}
```

## Разработчик
**Ваше Имя** - [GitHub](https://github.com/ExtaZzZ4106)

