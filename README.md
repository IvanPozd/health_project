# Проект HealthProject

Наш совместный проект с TheMihMih для успешного прохождения курсов LearnPython.
HealthProject создавался как проект помогающий Вам следить за рационом своего питания.

## Установка

1. Клонируйте репозиторий.

```bash
git clone https://github.com/IvanPozd/health_project.git
```

2. Создайте виртуальное окружение.

```bash
python3 -m venv env
```

3. Установите зависимости.

```bash
pip install -r requirements.txt
```

4. В папке /webapp создайте файл: `config.py`.

5. В файле `config.py` создайте следующие переменные:

```bash
from datetime import timedelta
import os

basedir = os.path.abspath(os.path.dirname(__file__))
SECRET_KEY = "Ваш секретный ключ"
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "..", "webapp.db")
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, "db_repository")
SQLALCHEMY_TRACK_MODIFICATIONS = False
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
REMEMBER_COOKIE_DURATION = timedelta(days=5)
MEDIA_PATH = f"{basedir}/news/parser/images/"
```

6. Запустите `celery` командой:

```bash
celery -A tasks worker --loglevel=info      #для Linux/MacOs
```

```bash
set FORKED_BY_MULTIPROCESSING=1 && celery -A tasks worker --loglevel=info   #для Windows
```
