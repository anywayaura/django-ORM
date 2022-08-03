### Website for bank security service (not real)

Tracking passcards and storage activity

**installation:**

```
pip install -r requirements.txt
```

**setup:**

add following env variables
for the database connection:
    `DB_ENGINE`, `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`

for django setting:
    `DJ_SECRET_KEY`, `DJ_DEBUG`, `DJ_ALLOWED_HOSTS`

enter 

**run:**

```
python manage.py runserver 0.0.0.0:8000
```
open browser on page http://127.0.0.1:8000
