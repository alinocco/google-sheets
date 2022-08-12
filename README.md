# Google Sheets

**Тестовое задание от Каналсервис**

Скрипт для добавления данных с Google Sheets в базу данных PosgreSQL.

## Требования

- python=3.8.10

## Настройка и запуск проекта

1. Склонировать репозиторий с помощью команды:
   ```
   git clone https://github.com/alinocco/google-sheets.git
   ```
2. Перейти в папку с проектом:
   ```
   cd google-sheets
   ```
3. Установить **poetry**:
   ```
   pip install poetry
   ```
4. Активировать виртуальное окружение:
   ```
   poetry shell
   ```
5. Установить зависимости:
   ```
   poetry install
   ```
6. Установить Docker и docker-compose с [официального сайта](https://www.docker.com/products/docker-desktop)
7. Запустить сервисы в Docker (PostgreSQL, Redis, adminer):
   ```
   docker-compose -f basic-compose.yml up -d --build --remove-orphans
   ```
8. Получить креды от внешних сервисов и прикрепить их соответсвенно:

- src/settings/.env
- src/telegram/.env
- credentials.json

9. Применить миграции:
   ```
   python3 src/manage.py migrate
   ```
10. Запустить сервер приложения:
    ```
    python3 src/manage.py runserver
    ```
11. Запустить Celery в другом терминале:
    ```
    cd src && celery -A settings worker -B -l INFO
    ```

_Шаги 5 и 6 можно пропустить и развернуть локально данные сервисы._

## Степень выполненности

- [x] Получение данных, при помощи Google Drive API и Google Sheets API

- Перенос данных в PostgreSQL:
- [x] Подключение PostgreSQL
- [x] Перевод в рубли по курсу ЦБ - "стоимость в руб."

- [x] Обеспечение синхронизации Google Sheets и базы данных
- Дополнительный функционал:
- [ ] Docker-контейнер
- [x] Сообщение через Telegram-бота о "сроках поставки"
- [ ] Django-приложение с фронт-ендом ReactJS 5. GitHub с документом Google Sheets
