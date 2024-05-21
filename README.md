# VBlog

VBlog - это блог-приложение, разработанное на Django 5, которое позволяет пользователям создавать и управлять постами, а также загружать и прикреплять изображения к постам.

## Установка

### Требования

- Python 3.11 или новее
- Django 5.0.3
- pillow 10.3.0 или новее

### Шаги установки

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/redtomat87/vblog.git
    cd vblog
    ```

2. Создайте виртуальное окружение и активируйте его:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Для Windows используйте venv\Scripts\activate
    ```

3. Установите зависимости:

    ```bash
    pip install poetry
    poetry install -no-root

    ```

4. Примените миграции:

    ```bash
    python manage.py migrate
    ```

5. Создайте суперпользователя для доступа к административной панели:

    ```bash
    python manage.py createsuperuser
    ```

6. Запустите сервер разработки:

    ```bash
    ython manage.py runserver localhost:8000
    ```

7. Откройте браузер и перейдите по адресу:

    ```
    http://localhost:8000/
    ```

## Функциональность

- **Создание постов:** Пользователи могут создавать посты с заголовком, текстом и тегами.
- **Загрузка изображений:** К каждому посту можно прикрепить одно или несколько изображений.
- **Теги:** Теги можно добавлять вручную при создании поста.
- **Сортировка постов:** Посты отображаются на странице в порядке от последних к более ранним.
- **Пагинация:** На странице отображается ограниченное количество постов с возможностью перехода между страницами.
- **Аутентификация:** Система пользователей с возможностью создания и входа.

## Структура проекта

- `vblog/` - Главная директория проекта Django.
- `posts/` - Приложение для управления постами.
- `writers/` - Приложение для управления пользователями (писателями).
- `templates/` - Директория с HTML-шаблонами.
- `static/` - Директория со статическими файлами (CSS, JS, изображения).
- `media/` - Директория для хранения загруженных изображений.
- `myauth/` - приложение для управление аутентификацией

## Наполнение тестовыми данными
  Скрипт для наполнения тестовыми данными лежит в vblog/src/posts/management/commands/fill_db.py.
  Для его запуска выолните


    ```bash
    python manage.py fill_db
    ```

Вклад
Если вы хотите внести свой вклад в проект, пожалуйста, следуйте следующим шагам:

Форкните репозиторий.
Создайте новую ветку (git checkout -b feature/ваша-фича).
Сделайте коммиты ваших изменений (git commit -m 'Добавил новую фичу').
Запушьте изменения в ветку (git push origin feature/ваша-фича).
Откройте Pull Request.