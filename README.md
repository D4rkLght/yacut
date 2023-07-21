# YaCut

## Оглавление

* [Стек технологий](#stack)
* [Описание проекта](#description)
* [Запуск проекта](#start_project)
* [Примеры запросов](#examples)
* [Автор проекта](#author)


## Стек технологий <a name="stack"></a>

[![Python](https://img.shields.io/badge/-Python-464641?style=flat-square&logo=Python)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/Pytest-464646?style=flat-square&logo=pytest)](https://docs.pytest.org/en/6.2.x/)
[![Flask](https://img.shields.io/badge/-Flask-464641?style=flat-square&logo=Flask)](https://flask.palletsprojects.com/en/2.3.x/)
[![SQLite](https://img.shields.io/badge/-SQLite-464641?style=flat-square&logo=SQLite)](https://www.sqlite.org/index.html)

## Описание проекта <a name="description"></a>

YaCut - это сайт, который предостовляет сервис укорачивания ссылок, а также API. Пользователь может сформировать собственную короткую ссылку, либо сам сервис её сгенерирует. Пользовательский вариант короткой ссылки не должен превышать 16 символов.

Ключевые возможности сервиса:
* генерация коротких ссылок и связь их с исходными длинными ссылками,
* переадресация на исходный адрес при обращении к коротким ссылкам.

Пользовательский интерфейс сервиса — одна страница с формой. Эта форма состоит из двух полей:
* обязательного для длинной исходной ссылки;
* необязательного для пользовательского варианта короткой ссылки.

## Запуск проекта <a name="start_project"></a>

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

## Примеры запросов <a name="examples"></a>

Пример пользовательского варианта короткой ссылки:

* Оригинальная ссылка - https://peps.python.org/pep-3150/#examples
* Короткая ссылка - http://127.0.0.1:5000/Opr

Пример генерации сервиса короткой ссылки:

* Оригинальная ссылка - https://peps.python.org/pep-3150/#lack-of-real-world-impact-assessment
* Короткая ссылка -http://127.0.0.1:5000/9HcXWG

## Над проектом работал: <a name="author"></a>

Разработчик [Ярослав Андреев ](https://github.com/D4rkLght).