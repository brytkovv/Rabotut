Предполагается, что пользователь находится в корневой директории проекта

#Windows:

Установка необходимых библиотек
pip install -r requirements.txt

Запуск через командную строку, где указывается расположение json
python run.py 'C:\environments\TaskRabotut\IncomingData.json'

Запуск тестов
pytest -v tests/test.py

#macOS/Linux

Установка необходимых библиотек
pip install -r requirements.txt

Запуск через командную строку, где указывается расположение json
python3 run.py 'C:\environments\TaskRabotut\IncomingData.json'

Запуск тестов
pytest -v tests/test.py


