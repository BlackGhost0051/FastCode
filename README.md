# Fast Code

# Content

- [Structure](#structure)
- [How add a new language](#how-add-a-new-language)
  - [Make language dir](#make-language-dir)
  - [Modify EXTENSIONS_PATH](#modify-extensions_path)
  - [Add logo](#add-logo)
- [Statistic](#statistic)

## Structure

```
FasrCode/
├── README.md
├── app
│         ├── __init__.py   # Initialize the Flask application
│         ├── database.db   # SQLite database file
│         ├── routes.py     # Define your route handlers
│         ├── static
│         │         ├── css                 # CSS files
│         │         │         ├── code.css
│         │         │         ├── error.css
│         │         │         ├── style.css
│         │         │         └── typing.css
│         │         ├── js                  # JavaScript files
│         │         │         ├── code_list.js
│         │         │         ├── error.js
│         │         │         ├── languages_list.js
│         │         │         ├── random_typing.js
│         │         │         ├── statistics.js
│         │         │         └── typing.js
│         │         ├── languages           # Languages files
│         │         │         ├── c
│         │         │         │   └── test.c
│         │         │         ├── java
│         │         │         │   └── test.java
│         │         │         └── python
│         │         │             └── test.py
│         │         └── logo                # Logo
│         │             ├── c_logo.svg
│         │             ├── java_logo.svg
│         │             └── python_logo.svg
│         └── templates                     # HTML files
│             ├── error.html
│             ├── index.html
│             ├── language.html
│             ├── statistics.html
│             └── typing.html
├── config.py           # Configuration settings for Flask app
├── requirements.txt    # List of dependencies
└── run.py              # Entry point to run the Flask app
```

## DataBase Structure
```
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        login TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        isAdmin BOOLEAN DEFAULT 0
    );

    CREATE TABLE statistics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        login TEXT NOT NULL,
        time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        chars INTEGER,
        typing_speed REAL,
        file_name TEXT,
        FOREIGN KEY (login) REFERENCES users(login)
    );
```

```
  id login password isAdmin
  id login time chars typing_speed file_name
```

## How add a new language

### Make language dir

`
app/static/languages
`

### Modify EXTENSIONS_PATH
Add your language

`
app/routes.py
`

```python
EXTENSIONS_PATH = {
    '.py': 'python',
    '.java': 'java',
    '.c': 'c'
}
```

### Add logo

language + _logo.svg

`
app/static/logo
`

## Statistic
chart.js

make users statistic
make all users statistics
make battle statistic




#### Plan
$$

Global Code
Lieder Board
Statistic
Players VS
Single typing
make xss detect

NEED ADD

js
ts
c++
assembly
matlab
