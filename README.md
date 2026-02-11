# TurboMarket

Платформа для онлайн-торговли с поддержкой продавцов, покупателей, управления товарами, скидками и заказами.

## Технологический стек

- **Python 3.10+**
- **Django 4.2**
- **PostgreSQL** 
- **Redis** 
- **Celery** 
- **Flower** 
- **django-simple-captcha**
- **Pillow** 


## Установка

### 1. Клонирование репозитория

```bash
git clone <repository-url>
cd TurboMarket
```

### 2. Установка зависимостей (требуется uv)

```bash
uv sync
```

Если `uv` не установлен:
```bash
pip install uv
uv sync
```

### 3. Конфигурация

Скопируйте `.env_example` в `.env` и установите необходимые переменные окружения:

```bash
cp .env_example .env
```

Основные переменные:
- `SECRET_KEY` — секретный ключ Django
- `DEBUG` — режим разработки (True/False)
- `POSTGRES_*` — параметры базы данных


### 4. Подготовка БД

```bash
uv run python manage.py migrate
uv run python manage.py createsuperuser
```

## Запуск

```bash
# Django сервер
uv run python manage.py runserver

# Celery worker 
uv run celery -A core worker -l info

# Celery Beat для периодических задач 
uv run celery -A core beat -l info

# Flower для мониторинга 
uv run celery -A core flower
```




