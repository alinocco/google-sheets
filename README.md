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
7. Подготовить порты для Docker:
   ```
   sudo service docker start
   /etc/init.d/redis-server stop
   sudo service postgresql stop
   ```
8. Запустить сервисы в Docker (PostgreSQL, Redis, adminer):
   ```
   sudo docker-compose -f basic-compose.yml up -d --build --remove-orphans
   ```
   Для контейнеризации самого приложения:
   ```
   sudo docker-compose -f basic-compose.prod.yml up -d --build --remove-orphans
   ```
9. Получить креды от внешних сервисов и прикрепить их соответсвенно:

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

## Степень выполненности

- [x] 1.0 Получение данных, при помощи Google Drive API и Google Sheets API
- [x] 2.1 Подключение PostgreSQL
- [x] 2.2 Перевод в рубли по курсу ЦБ - "стоимость в руб."
- [x] 3.0 Обеспечение синхронизации Google Sheets и базы данных
- [x] 4.1 Docker-контейнер
- [x] 4.2 Сообщение через Telegram-бота о "сроках поставки"
- [ ] 4.3 Django-приложение с фронт-ендом ReactJS 
- [ ] 5.0 GitHub с документом Google Sheets
