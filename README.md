# SQLite и практика: movie + RuTube

В этом уроке мы работаем с SQLite и создаём две таблицы:

- `movie` — для хранения информации о фильмах
- `RuTube` — для хранения любимых видео

## 1. Пример из документации

```python
import sqlite3

con = sqlite3.connect("tutorial.db")
cur = con.cursor()

cur.execute("CREATE TABLE movie(title, year, score)")
cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")
con.commit()

for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
    print(row)

con.close()
```

## 2. Как работает подключение к БД

Для начала нужно создать соединение с базой данных:

```python
con = sqlite3.connect("tutorial.db")
```

Это соединение позволяет работать с файлом `tutorial.db`. Если такого файла нет, SQLite создаст его автоматически.

Чтобы выполнять SQL-запросы, нужен курсор:

```python
cur = con.cursor()
```

После завершения работы соединение закрывают:

```python
con.close()
```

## 3. Основные команды SQL

- `CREATE` — создать таблицу
- `INSERT` — вставить данные
- `SELECT` — выбрать данные
- `UPDATE` — изменить запись
- `DELETE` — удалить запись
- `DROP` — удалить таблицу

## 4. Выполнение запросов

```python
cur.execute("INSERT INTO movie VALUES ('Monty Python and the Holy Grail', 1975, 8.2)")
```

Вставка нескольких записей:

```python
data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]
cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
```

Сохранение изменений:

```python
con.commit()
```

## 5. Создание таблицы

```sql
CREATE TABLE movie(title, year, score)
```

Если таблица уже существует:

```sql
CREATE TABLE IF NOT EXISTS movie(title, year, score)
```

Типы данных:

```sql
CREATE TABLE IF NOT EXISTS movie(
    title TEXT,
    year INTEGER,
    score REAL
)
```

## 6. Пример с двумя таблицами

Мы создаём две таблицы: `movie` и `RuTube`.

### Таблица `movie`

```sql
CREATE TABLE movie (
    id INTEGER,
    title TEXT NOT NULL,
    year INTEGER,
    score REAL
)
```

### Таблица `RuTube`

```sql
CREATE TABLE RuTube (
    id INTEGER,
    title TEXT NOT NULL,
    video_url TEXT NOT NULL,
    author TEXT,
    release_date TEXT,
    description TEXT
)
```

## 7. Добавление данных

```python
movies = [
    (1, "The Shawshank Redemption", 1994, 9.3),
    (2, "The Godfather", 1972, 9.2),
    (3, "The Dark Knight", 2008, 9.0),
    (4, "Inception", 2010, 8.8),
    (5, "Interstellar", 2014, 8.7),
]

cur.executemany(
    "INSERT INTO movie (id, title, year, score) VALUES (?, ?, ?, ?)",
    movies,
)
```

```python
videos = [
    (1, "Python для начинающих", "https://rutube.ru/video/1", "CodeSchool", "2024-01-15", "Короткий курс по основам Python."),
    (2, "Git и GitHub за 10 минут", "https://rutube.ru/video/2", "DevMentor", "2023-11-20", "Основы работы с репозиториями."),
    (3, "SQLite для новичков", "https://rutube.ru/video/3", "DataLab", "2024-02-10", "Работа с базами данных через Python."),
    (4, "Как учить программирование", "https://rutube.ru/video/4", "StudyFlow", "2023-09-05", "Советы по эффективному обучению."),
    (5, "HTML и CSS с нуля", "https://rutube.ru/video/5", "WebAcademy", "2024-03-01", "Основы веб-разработки."),
]

cur.executemany(
    "INSERT INTO RuTube (id, title, video_url, author, release_date, description) VALUES (?, ?, ?, ?, ?, ?)",
    videos,
)
```

## 8. Выборка данных

```sql
SELECT * FROM movie
SELECT * FROM RuTube
```

```python
for row in cur.execute("SELECT * FROM movie ORDER BY year"):
    print(row)
```

## 9. Обновление данных

```sql
UPDATE movie SET score = 9.5 WHERE id = 3
UPDATE RuTube SET description = 'Обновлённое описание' WHERE id = 2
```

## 10. Удаление данных

```sql
DELETE FROM movie WHERE id = 5
DELETE FROM RuTube WHERE id = 4
```

## 11. Удаление таблицы

```sql
DROP TABLE movie
DROP TABLE RuTube
```

## 12. Задание для практики

1. Создай таблицу `movie`
2. Создай таблицу `RuTube`
3. Добавь минимум 5 строк в каждую таблицу
4. Выведи все данные из обеих таблиц
5. Измени одну запись через `UPDATE`
6. Удали одну запись через `DELETE`
7. Сохрани результат в базе данных

## 13. Итог

Мы научились:

- создавать соединение с SQLite
- создавать таблицы
- вставлять данные
- выбирать записи
- обновлять записи
- удалять записи
- работать сразу с несколькими таблицами

Если хочешь, я могу ещё сделать для этого урока краткую версию на русском в стиле школьного задания или оформить README в более "красивом" учебном виде.
