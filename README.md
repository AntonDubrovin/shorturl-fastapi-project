Разработка и деплой FastAPI-сервисов с использованием Docker

Сервис сокращения URL (Short URL): Позволяет создавать короткие
ссылки для длинных URL, перенаправлять по короткому
идентификатору и предоставлять информацию о ссылке. Также
хранение данных в SQLite

Сервис сокращения URL:
- Эндпоинты:
  - POST /shorten: Принимает полный URL (JSON: {"url":"..."}) и
возвращает короткую ссылку.
  - GET /{short_id}: Перенаправляет на полный URL, если он
существует.
  - GET /stats/{short_id}: Возвращает JSON с информацией о полном
URL.
 - Данные о сокращенных ссылках (short_id -> full_url) хранятся в SQLite.
 - При запуске также автоматически создается таблица.


Docker HUB: https://hub.docker.com/repository/docker/antondubrovin/shorturl_service/general


- docker build -t antondubrovin/shorturl_service:latest . 
- docker login
- docker push antondubrovin/shorturl_service:latest
- docker ps -a
- docker run -d -p 8001:80 antondubrovin/shorturl_service:latest
- docker ps -a

http://localhost:8001/docs
![image](https://github.com/user-attachments/assets/477cb34f-b99e-4121-b98e-1dcede3e826c)


