# YaCut

## Оглавление
[Стек технологий](#Стек_технологий)

### Стек технологий
[![Python](https://img.shields.io/badge/-Python-464641?style=flat-square&logo=Python)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/Pytest-464646?style=flat-square&logo=pytest)](https://docs.pytest.org/en/6.2.x/)
[![Flask](https://img.shields.io/badge/-Flask-464641?style=flat-square&logo=Flask)](https://flask.palletsprojects.com/en/2.3.x/)
[![SQLite](https://img.shields.io/badge/-SQLite-464641?style=flat-square&logo=SQLite)](https://www.sqlite.org/index.html)

## Описание 
YaCut - это сайт, который предостовляет сервис укорачивания ссылок, а также API. Пользователь может сформировать собственную короткую ссылку, либо сам сервис её сгенерирует.

## Запуск проекта
Клонировать репозиторий и перейти в него в командной строке:

```
git clone 
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Миграции

```
flask db upgrade
```

Запустить проект:

```
flask run
```

## Над проектом работал:
Разработчик [Ярослав Андреев ](https://github.com/D4rkLght).