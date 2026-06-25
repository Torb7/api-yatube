# API для YaTube

REST API для платформы публикации постов. Пользователи могут создавать публикации, комментировать записи, объединять посты в группы и подписываться на других авторов.

## Технологии

* Python 3.12
* Django
* Django REST Framework
* Djoser
* JWT-аутентификация
* SQLite

## Возможности API

### Публикации

* Получение списка публикаций
* Получение публикации по id
* Создание публикации
* Редактирование собственной публикации
* Удаление собственной публикации

### Комментарии

* Получение списка комментариев к публикации
* Получение комментария по id
* Создание комментария
* Редактирование собственного комментария
* Удаление собственного комментария

### Группы

* Получение списка групп
* Получение информации о группе

### Подписки

* Получение списка своих подписок
* Подписка на автора
* Поиск подписок по имени пользователя

## Установка

Клонировать репозиторий:

```bash
git clone https://github.com/Torb7/api-final-yatube
cd yatube_api
```

Создать виртуальное окружение:

```bash
python -m venv venv
```

Активировать окружение:

Linux/macOS:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

Установить зависимости:

```bash
pip install -r requirements.txt
```

Применить миграции:

```bash
python manage.py migrate
```

Запустить сервер:

```bash
python manage.py runserver
```

## Аутентификация

Проект использует JWT-токены.

Получение токена:

```http
POST /api/v1/jwt/create/
```

Тело запроса:

```json
{
    "username": "username",
    "password": "password"
}
```

Ответ:

```json
{
    "refresh": "refresh_token",
    "access": "access_token"
}
```

Для авторизованных запросов необходимо передавать токен в заголовке:

```http
Authorization: Bearer <access_token>
```

## Основные эндпоинты

### Публикации

```http
GET     /api/v1/posts/
POST    /api/v1/posts/
GET     /api/v1/posts/{id}/
PATCH   /api/v1/posts/{id}/
DELETE  /api/v1/posts/{id}/
```

### Комментарии

```http
GET     /api/v1/posts/{post_id}/comments/
POST    /api/v1/posts/{post_id}/comments/
GET     /api/v1/posts/{post_id}/comments/{id}/
PATCH   /api/v1/posts/{post_id}/comments/{id}/
DELETE  /api/v1/posts/{post_id}/comments/{id}/
```

### Группы

```http
GET     /api/v1/groups/
GET     /api/v1/groups/{id}/
```

### Подписки

```http
GET     /api/v1/follow/
POST    /api/v1/follow/
```

Поиск подписок:

```http
GET /api/v1/follow/?search=username
```

## Права доступа

### Публикации и комментарии

* Неавторизованные пользователи могут просматривать данные.
* Создавать публикации и комментарии могут только авторизованные пользователи.
* Редактировать и удалять объект может только его автор.

### Группы

* Доступны только для чтения.

### Подписки

* Доступны только авторизованным пользователям.
* Нельзя подписаться на самого себя.
* Нельзя повторно подписаться на одного и того же пользователя.

## Документация API

После запуска сервера документация доступна по адресу:

```http
http://127.0.0.1:8000/redoc/
```
