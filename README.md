# SQLite: пример из документации и разбор команд

Пример из документации:

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

Для работы с базой данных в первую очередь нужно создать соединение с ней. Для этого программа должна понимать, где находится база данных или где её создать:

```python
con = sqlite3.connect("tutorial.db")
```

Чтобы выполнять операторы SQL и получать результаты запросов, нужно создать курсор:

```python
cur = con.cursor()
```

В конце соединение закрывается так:

```python
con.close()
```

Взаимодействие с БД происходит через команды:

- `cur.execute()` — выполнение одного SQL-запроса
- `cur.executemany()` — выполнение нескольких запросов

```python
cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")

data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]
cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
```

Все изменения нужно сохранять командой:

```python
con.commit()
```

## SQL-запросы

Самые популярные типы SQL-запросов:

- `CREATE`
- `INSERT`
- `SELECT`
- `UPDATE`
- `DELETE`
- `DROP`

### Создание таблицы

```sql
CREATE TABLE movie(title, year, score)
```

Если таблица уже существует, можно использовать:

```sql
CREATE TABLE IF NOT EXISTS movie(title, year, score)
```

С явным указанием типов данных:

```sql
CREATE TABLE IF NOT EXISTS movie(
    title TEXT,
    year INTEGER,
    score REAL
)
```

### Вставка записей

```sql
INSERT INTO movie VALUES ('Monty Python and the Holy Grail', 1975, 8.2)
```

Можно указывать поля:

```sql
INSERT INTO movie (title, year) VALUES ('The Imitation Game', 2014)
```

Или использовать параметризацию:

```python
cur.execute("INSERT INTO movie (title, year) VALUES (?, ?)", ('The Imitation Game', 2014))
```

### Выборка данных

```sql
SELECT * FROM movie
SELECT year, title FROM movie WHERE year > 2000
SELECT score, title FROM movie ORDER BY score
```

### Обновление данных

```sql
UPDATE movie SET score = 10 WHERE title = 'Monty Python and the Holy Grail'
```

### Удаление данных

```sql
DELETE FROM movie WHERE score < 8
```

### Удаление таблицы

```sql
DROP TABLE movie
```

## Задание

Используй все перечисленные команды для работы с базой данных из документации.
