## Подготовка
1. Установка Homebrew 
>/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
2. Создание виртуального окружения в папке проекта
>python3 -m venv .venv
3. Активация виртуального окружения
>source .venv/bin/activate
4. Установка зависимостей
>pip install -r requirements.txt

## Структура проекта
- api_framework.base_api - базовый HTTP-клиент (сессия, таймауты, логирование)
- api_framework.models.student_model - модели ответов API
- api_framework.students.students_api - методы create/get/update/delete
- api_framework.students.payloads - фабрика тестовых данных через Faker
- config.config - чтение .env и настройка логирования
- tests.test_student - тесты
- utils.helper - прикрепление ответов к Allure

## Запуск
- pytest - запуск тестов и генерация allure-results
- allure serve allure-results - открытие отчета