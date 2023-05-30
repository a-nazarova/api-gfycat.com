## Проект
Рассматриваются примеры api-тестов на два метода:
- GET 
- PATCH
из [API Documentation](https://developers.gfycat.com/api/) "Gfycat"

Используемый стэк:
- puthon3
- requests
- pytest
- poetry

## Установка
Склонируйте или скачайте проект 
Установите зависимости -- poetry install
Запустите изолированное окружение -- poetry shell

## Подготовка
Для корректной работы тестов необходимы авторизационные данные
Требуется создать учетную запись на [Gfycat](https://gfycat.com/signup)
Затем, вставьте "username" и "password" в словарь “credentials” в файле  gfycat_auth.py

## Запуск тестов
Для запуска тестов используйте команды pytest к файлу test_api.py, пример для отчета с форматированием -- pytest  -v --tb=line test_api.py
