import sqlite3

# Подключаемся к БД
con = sqlite3.connect("tutorial.db")
cur = con.cursor()

# Сначала очищаем старые таблицы, чтобы пример запускался одинаково
cur.execute("DROP TABLE IF EXISTS RuTube")
cur.execute("DROP TABLE IF EXISTS movie")

# Создаем таблицу movie
cur.execute("""
    CREATE TABLE movie (
        id INTEGER,
        title TEXT NOT NULL,
        year INTEGER,
        score REAL
    )
""")

# Создаем таблицу RuTube
cur.execute("""
    CREATE TABLE RuTube (
        id INTEGER,
        title TEXT NOT NULL,
        video_url TEXT NOT NULL,
        author TEXT,
        release_date TEXT,
        description TEXT
    )
""")

# Данные для movie
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

# Данные для RuTube
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
con.commit()

print("\nТаблица movie:")
for row in cur.execute("SELECT * FROM movie ORDER BY year"):
    print(row)

print("\nТаблица RuTube:")
for row in cur.execute("SELECT * FROM RuTube ORDER BY id"):
    print(row)

# UPDATE в movie
cur.execute("UPDATE movie SET score = 9.5 WHERE id = 3")
con.commit()
print("\nПосле UPDATE в movie:")
for row in cur.execute("SELECT id, title, score FROM movie WHERE id = 3"):
    print(row)

# UPDATE в RuTube
cur.execute("UPDATE RuTube SET description = 'Обновлённое описание для практики SQLite' WHERE id = 2")
con.commit()
print("\nПосле UPDATE в RuTube:")
for row in cur.execute("SELECT id, title, description FROM RuTube WHERE id = 2"):
    print(row)

# DELETE из movie
cur.execute("DELETE FROM movie WHERE id = 5")
con.commit()
print("\nПосле DELETE из movie:")
for row in cur.execute("SELECT * FROM movie ORDER BY id"):
    print(row)

# DELETE из RuTube
cur.execute("DELETE FROM RuTube WHERE id = 4")
con.commit()
print("\nПосле DELETE из RuTube:")
for row in cur.execute("SELECT * FROM RuTube ORDER BY id"):
    print(row)

con.close()
