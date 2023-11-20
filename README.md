# OpenApiService

# Структура

Django+Postgre, обернут в Docker и подключен OpenApi 

# Запуск

docker-compose build
docker-compose up

Так же требуется создать базу данных

docker-compose run web-app sh -c  "python manage.py makemigrations"
docker-compose run web-app sh -c  "python manage.py migrate"

# Работа с файлами

/file/ POST - загружает файл openapi и обарабатывает его, выдавая написанные в нем endpoints
/add_methods/ POST - загружает связанные с моделью записи файла модели HTTP методов
/file_detail/{id} GET - Отображает информацию о файла и все связанные с ним модели HTTP запросов 

