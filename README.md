# STRIPE_TEST

Тестовое задание по работе платёжной системы Stripe.

## Описание

С помощью python библиотеки stripe можно удобно создавать платежные формы разных видов, сохранять данные клиента, и реализовывать прочие платежные функции. 
В этом проекте реализован простой сервер с одной html страничкой, который общается со Stripe и создает платёжные формы для товаров. 
Для решения использован Django.

### Технологии
 - _Python 3.7.9
 - _Django 3.2.17
 - _Stripe 5.1.1
 - _Unittest

## Запуск с помощью Docker

Установите докер: https://www.docker.com/products/docker-desktop

### Соберите приложение:

Клонируйте репозиторий с проектом на свой компьютер:

### В терминале из рабочей директории выполните команду:
```
git clone https://github.com/genpoplevin/stripe_test.git
```

### Перейдите в папку stripe_test
```
cd stripe_test
```

### Выполните команды:
```
docker build -t stripe_test .
```
docker run --name stripe_test_container -it -p 8000:8000 stripe_test
```
Теперь приложение будет доступно в браузере по адресу localhost:8000/admin/
Логин: admin
пароль: admin
Будет установлена база данных с двумя товарами и суперпользователем admin.
```

## Запуск без Docker:

Клонировать репозиторий:

```
git clone https://github.com/genpoplevin/stripe_test.git
```

Перейти в папку stripe_test/
```
cd stripe_test
```

Cоздать виртуальное окружение:
```
python -m venv venv
```

Активировать виртуальное окружение:
```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```

Создать и запустить миграции:
```
python manage.py makemigrations
python manage.py migrate
```

Запустить локальный сервер:
```
python manage.py runserver
```
Теперь проект будет доступен по адресу http://127.0.0.1:8000/ в браузере


### Набор доступных адресов:
* ```admin/``` - Панель управления администратора (login: admin; password: admin).
* ```items/{id}``` - Получение товара с соответствующим id.
* ```buy/{id}``` - Покупка товара с соответствующим id.

#### Автор
Поплевин Геннадий