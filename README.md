# Куда пойти — Москва глазами Артёма

Сайт о самых интересных местах в Москве. Авторский проект Артёма.
Начальная версия размещена [здесь](http://melwheretogo.pythonanywhere.com/)

## Установка
[Установите Python](https://www.python.org/), если этого ещё не сделали. Требуется Python 3.8 и старше. Код может запуститься на других версиях питона от 3.1 и старше, но на них не тестировался.

Проверьте, что `python` установлен и корректно настроен. Запустите его в командной строке:
```sh
python --version
```
Возможно, вместо команды `python` здесь и в остальных инструкциях этого README придётся использовать `python3`. Зависит это от операционной системы и от того, установлен ли у вас Python старой второй версии.

Скачайте код:
```sh
git clone https://github.com/MelnikovEI/where_to_go
```

Перейдите в каталог проекта:
```sh
cd where_to_go
```

В каталоге проекта создайте виртуальное окружение:
```sh
python -m venv venv
```
Активируйте его. На разных операционных системах это делается разными командами:

- Windows: `.\venv\Scripts\activate`
- MacOS/Linux: `source venv/bin/activate`

Установите зависимости в виртуальное окружение:
```sh
pip install -r requirements.txt
```

Создайте базу данных SQLite

```sh
python manage.py migrate
```

Запустите разработческий сервер

```
python manage.py runserver
```

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 3 переменные:
- `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта
- `DATABASE_FILEPATH` — полный путь к файлу базы данных SQLite, например: `/home/user/schoolbase.sqlite3`
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/4.2/ref/settings/#allowed-hosts)

## Добавить места
Для добавления новых мест можно воспользоваться [страницей администратора](https://melwheretogo.pythonanywhere.com/admin/)
или же сложить json файлы вида\
{\
&emsp;"title": "Водопад Радужный",\
&emsp;"imgs": [\
&emsp;&emsp;"https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/7252a5cbb831eec01d98f3c234f2dfc5.jpg",
&emsp;&emsp;"https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/c0191d876a75c05d72d9845251758b34.jpg",
&emsp;&emsp;"https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/3daa4472d29bc5e3c82a62edb7ea6cfe.jpg",
    ],\
&emsp;"description_short": "Центральная Россия — край водопадов! Не верите? А зря.",\
&emsp;"description_long": "Вас привлекает ром... отпуска.",\
&emsp;"coordinates": {
        "lng": "36.940988",
        "lat": "55.20653999999999"
    }\
}\
в одну папку и запустить команду 'add_places', указав аргументом путь к ней:
```
python3 manage.py add_places /home/melwheretogo/new_places
```
## Цели проекта

Код написан в учебных целях — для курса по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).
